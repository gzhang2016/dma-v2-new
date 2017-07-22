#!/usr/bin/env python
###############################################################################
#
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
#
# This module validates all the CLI option processed in cli_options module
# and does the sanity check of the values to pass on.
###############################################################################

# Python module
import os
import sys
import re

# DMA module

from templates.misc.dma_regex import *
from templates.cli.cli_args_validator import *
from templates.misc.precheck import *


def get_object_name_from_sqlfile(sqlfile, obj_type):
    name = 'xyz'
    return name


def extract_ddl_from_sqlfile_and_write_to_file(otype,
                                               sqlfile,
                                               ):
    obj_tmp_filename = '%s%s_%s_%s.sql' % \
                       (assessment_files_write_location,
                        obj_schema,
                        obj_type,
                        obj_name)
    logger.info ("Writing to file...%s" % obj_tmp_filename)
    ofile = open (obj_tmp_filename, 'w')
    with open (sqlfile, 'r') as f:
        gen = object_section (f)
        for line in gen:
            ofile.write (line)
    ofile.close ()
    return obj_tmp_filename
