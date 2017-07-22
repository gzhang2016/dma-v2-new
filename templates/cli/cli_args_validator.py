#!/usr/bin/env python
###############################################################################
#
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
#
# This module validates all the CLI option processed in cli_options module
# and does the sanity check of the values to pass on.
###############################################################################
# Python Modules
import os
import sys
import cx_Oracle
from datetime import datetime

# DMA Modules
from templates.cli.cli_options import *

assessment_flag = ''

# Validating Mandatory cli options
#---------------------------------
# Either Oracle or SQL option check
if not cli_args.sql_file and not cli_args.ora_conn_string:
    print ("Either Oracle Connection or SQL file option should be passed")
    sys.exit (1)
if cli_args.sql_file and cli_args.ora_conn_string:
    print ('\nBoth SQL and Oracle Connect model cannot be used together\n'
           'Check ./edb-dmat.py --help')
    sys.exit (1)

if cli_args.ora_conn_string:
    assessment_flag = 'connection'
    # Oracle Connection String Check
    conn_string = cli_args.ora_conn_string
    if conn_string.count ('@') == 1 and conn_string.count ('/') == 2 and conn_string.count (':') == 1:
        DBA_user = conn_string.split ('@', 1)[0].split ('/', 1)[0]
        DBA_password = conn_string.split ('@', 1)[0].split ('/', 1)[1]
        ORACLE_host = conn_string.split ('@', 1)[1].split (':', 1)[0]
        ORACLE_port = conn_string.split ('@', 1)[1].split (':', 1)[1].split ('/', 1)[0]
        ORACLE_sid_or_service = conn_string.split ('@', 1)[1].split (':', 1)[1].split ('/', 1)[1]
        if not DBA_user or not DBA_password or not ORACLE_host or not ORACLE_port or not ORACLE_sid_or_service:
            print ('''Not a valid Oralce connection String !!\n
                     pass "username/password@host:port/sid-or-service"''')
            sys.exit (1)
    else:
        print ('''Pass Oracle connection string as \n
        "username/password@host:port/sid-or-service"''')
        sys.exit (1)

    # Schema value check
    if not cli_args.assessment_schema:
        print ('Assessment schema name is mandatory. Check edb-dmat --help')
        sys.exit (1)
    DMA_schema = cli_args.assessment_schema.upper ()
    cli_object_type = cli_args.object_type

if cli_args.sql_file:
    assessment_flag = 'sql'
    # SQL file check
    sqlfilename = cli_args.sql_file
    if not os.path.isfile (sqlfilename):
        print ('File do not exists!! Pass valid one')
        sys.exit (1)

    # Oracle object check
    if not cli_args.object_type:
        print ("\'ALL\' or Specific Oracle Object %s should be used with -S option!!" % objects_list)
        sys.exit (1)
    cli_object_type = cli_args.object_type.upper ()
    if not cli_object_type in (objects_list):
        print ("Not a valid Object!!..Pass any of objects:- \n")
        for items in objects_list:
            print (items)
        print ()
        sys.exit (1)

# Any Assessment log location is must..check
if not cli_args.assessment_logs_location:
    print ('Assessment Logs Location is mandatory. Check edb-dmat --help')
    sys.exit (1)
    # Check if location exists and valid
if not os.path.isdir (cli_args.assessment_logs_location):
    print ("%s not a valid log location" % cli_args.assessment_logs_location)
    sys.exit (1)

    # Check the location is writeable
if not os.access (cli_args.assessment_logs_location,
                  os.W_OK):
    print ("No write access on directory. Tool user should have write access.")
    sys.exit (1)

# Optional parameter report format check
report_format = cli_args.dma_report_format.upper ()
formats = ['HTML', 'LOG', 'BOTH']
if not report_format in (formats):
    print ("Formats can be HTML or LOG. Default is BOTH")
    sys.exit (1)

## Produce the Oracle connection if -conn option passed
if assessment_flag == 'connection':
    dma_user_check_query = ("select count(*) from dba_users "
                            "where username = '%s'")
    assess_start_time = datetime.now ()
    dsnStr = cx_Oracle.makedsn (ORACLE_host, ORACLE_port, service_name=ORACLE_sid_or_service)

    try:
        connection = cx_Oracle.Connection (user=DBA_user, password=DBA_password, dsn=dsnStr)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print ("Oracle-Error-Code:", error.code, file=sys.stderr)
        print ("Oracle-Error-Message:", error.message, file=sys.stderr)
        sys.exit (1)

    ORACLE_cursor = connection.cursor ()
    ORACLE_version = int (connection.version[:2])

    if not isinstance (ORACLE_version, int):
        print ("Not a valid Oracle Version. Please reach out to EDB consultant.")
        ORACLE_cursor.close ()
        connection.close ()
        sys.exit (1)

    if ORACLE_version < 9:
        print ("DMA Tool running against %s version. Tool may or may not work." % (ORACLE_version))

    try:
        DMA_schema_check = ORACLE_cursor.execute (dma_user_check_query % DMA_schema).fetchall ()[0][0]
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print ("Oracle-Error-Code:", error.code, file=sys.stderr)
        print ("Oracle-Error-Message:", error.message, file=sys.stderr)
        connection.close ()
        sys.exit (1)

    # Validating DMA schema
    if DMA_schema_check == 0:
        print ("Schema %s doesn't exist. Please give valid schema." % (DMA_schema))
        ORACLE_cursor.close ()
        connection.close ()
        sys.exit (1)

assessment_files_write_location = cli_args.assessment_logs_location
# add '/' to the assessment_log_location value passed
if not assessment_files_write_location.endswith (os.path.sep):
    assessment_files_write_location += os.path.sep
