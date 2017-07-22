#!/usr/bin/env python
###############################################################################
## Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
###############################################################################

# Python Modules
import os

#DMA Modules
from templates.classes.object_structure import *

# Antlr4 modules
# At this place you can plug any database Parser to import with
# if condition for each database. Here we are using for Oracle
# to EPAS parsing

from antlr4 import *
from antlr4.error.ErrorListener import *
from parse.ora2epas.ora2epasLexer import ora2epasLexer as Lexer
from parse.ora2epas.ora2epasParser import ora2epasParser as Parser


# A DDL file passed from edb_dmat will be parsed by the function as
# per the parse rules defined in ora2epas
#--------------------------------------------------------------
def parse_ddl_object(v_obj_ddl_file,rule_to_call='program'):
    source = FileStream(v_obj_ddl_file)
    lexer = Lexer(source)  #lexer.removeErrorListeners()
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(DMAErrorListener ())
    parseTree = getattr(parser,rule_to_call)()
    return parseTree


# Function to push objects parsing information into Object_Logs
# list dma_object_logs
#--------------------------------------------------------------
def push_into_dma_object_logs(os,ot,on,oss,is_good_object=None):
    if is_good_object is None:
        # If object has no incompatibility found then mark it as
        # good in Object_Logs with Migration Stage '0'
        dma_object_logs.append (Object_Logs (os,ot,on,oss,0,'','','',0,0))
    else:
        # retrieve the rule code,description and migration stage
        # from DMACodebase objects list dma_code(codelist.py)
        for c in dma_code:
            v_rule_name = str(is_good_object.args[1])
            if c.rule_name == v_rule_name:
                dma_object_logs.append(Object_Logs(os,ot,on,oss,
                                                   c.code,
                                                   c.description,
                                                   str(is_good_object.args[2]),
                                                   str(is_good_object.args[3]),
                                                   is_good_object.args[0],
                                                   c.stage))
            else:
                dma_object_logs.append (Object_Logs (os, ot, on, oss,
                                                     c.code,
                                                     c.description,
                                                     str (is_good_object.args[2]),
                                                     str (is_good_object.args[3]),
                                                     is_good_object.args[0],
                                                     c.stage))
        logger.error ('DMA-%s [%s] %s Context: %s' % (c.code,
                                                      is_good_object.args[1],
                                                      str (is_good_object.args[2]),
                                                      c.description
                                                      ))
    return

