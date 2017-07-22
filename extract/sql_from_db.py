#!/usr/bin/env python
###############################################################################
#
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
#
# This module extracts Object METADATA in form of SQL File to help
# parser to find incompatibilities. It uses Oracle Connection
###############################################################################

# Python Modules
# --------------
import sys
import os
import cx_Oracle

# DMA modules
# -----------
from templates.cli.cli_args_validator import *
from templates.sql.oracle_queries import *
from templates.misc.precheck import *
from templates.classes.object_structure import *


def extract_ddl_from_db_and_write_to_file(obj_type, obj_name, obj_schema):
    dbms_command = 'dbms_metadata.get_ddl'
    try:
        if obj_type == 'PACKAGE BODY':
            obj_type = 'PACKAGE_BODY'
        ORACLE_ddlcursor = connection.cursor ()
        ORACLE_ddlcursor.execute (ddl_transform)
        ddl_clob = ORACLE_ddlcursor.callfunc (dbms_command,
                                              cx_Oracle.CLOB,
                                              (obj_type, obj_name, obj_schema))
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        logger.error("Oracle ERROR: %s - %s" % (error.code,error.message))
        print ("Oracle Error: %s - %s " % (error.code,error.message))
        sys.exit (0)

    obj_tmp_filename = '%s%s_%s_%s.sql' % \
                       (assessment_files_write_location,
                        obj_schema,
                        obj_type,
                        obj_name)
    logger.info ("Writing to file - %s" % obj_tmp_filename)
    with open (obj_tmp_filename, 'w') as f:
        try:
            f.write (str (ddl_clob.read ()).replace ('"', '').upper())
        except IOError:
            logger.error("Could not able to write to file")
            print ("Error: Could not able to write.. ")
            sys.exit (0)
    return obj_tmp_filename


"""
logs = []
i = 0
try:
    for row in ORACLE_cursor.execute (table_query % DMA_schema).fetchall ():
        logs.append (object_logs (row[0], 'TABLE', row[1], row[2], '', '', 0, 0))
        # print (logs[i].oname)
        ORACLE_ddlcursor.execute (ddl_transform)
        clob = ORACLE_ddlcursor.callfunc ("dbms_metadata.get_ddl",
                                          cx_Oracle.CLOB,
                                          (logs[i].otype, logs[i].oname))
        print (str (clob.read ()).replace ('"', ''))
        i += 1

except cx_Oracle.DatabaseError as e:
    print(logger.error(e))
    print('Failed')
    sys.exit(1)
"""
