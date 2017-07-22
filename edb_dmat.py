#!/usr/bin/env python3
###############################################################################
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
#
# Tool designed to do Database Migration Assessment [DMA] of Oracle Database to
# migrate it to EnterpriseDB Postgres Advanced Server. Its uses cx_Oracle module
# to connect to Oracle Database to scan the object by generating SQL file of
# object definition.
###############################################################################

# Python modules
# --------------
from datetime import datetime
from collections import Counter

# DMA modules
# -----------
# Perform prechecks before running using CLI options
from extract.sql_from_db import *
from extract.sql_from_file import *
from parse.parse_object import *
from generate.assessment_html_writer import *
from generate.assessment_log_writer import *
from src.codelist import *

# Variables
#----------
v_number_of_lines_parsed = 0
sys.path.append (__file__)


# set the assessment objects list to Cli object -o option
if assessment_flag == 'sql':
    if cli_object_type != 'ALL':
        assessment_objects_list[:] = list ()
        assessment_objects_list.append (cli_object_type)

# Remove 'ALL' keyword
if assessment_flag == 'connection':
    if not cli_object_type:
        assessment_objects_list.remove ('ALL')
    else:
        assessment_objects_list[:] = list ()
        assessment_objects_list.append (cli_object_type)



# Main loop to scan all objects in a SQL file or
# connecting to the database as per the assessment_object_list
#-------------------------------------------------------------
for assessment_object_type in assessment_objects_list:
    v_object_type = assessment_object_type
    if assessment_flag == 'connection':
        try:
            object_cursor = connection.cursor ()
            object_cursor.execute ((ddl_query % (v_object_type, DMA_schema)))
            v_object_schema_name = DMA_schema
            logger.info ('-------------------------------')
            logger.info('Extracting Object %s' % v_object_type)
            logger.info('--------------------------------')
            for obj in object_cursor:
                v_object_name = obj[0]
                v_object_status = obj[1]
                logger.info ('Extracting %s - %s.%s' % (v_object_type,
                                                        v_object_schema_name,
                                                        v_object_name))

                # ---Extract the DDL of object and write to file
                obj_ddl_file_name = extract_ddl_from_db_and_write_to_file (v_object_type,
                                                                           v_object_name,
                                                                           v_object_schema_name)

                ## Collect count of lines in a file sent for parsing
                v_number_of_lines_parsed = (v_number_of_lines_parsed +
                                           (sum(1 for line in open(obj_ddl_file_name))))

                # Pass the file to Parser and catch incompatible rule in exception
                try:
                    logger.info("Parsing %s" % obj_ddl_file_name)
                    rulename = call_object_rulename[v_object_type]
                    tree = parse_ddl_object (obj_ddl_file_name,rulename)
                    # If no exception in parsing the object is pushed as good
                    push_into_dma_object_logs(v_object_schema_name,
                                              v_object_type,
                                              v_object_name,
                                              v_object_status)
                    try:
                        os.remove(obj_ddl_file_name)
                    except OSError as e:
                        logger.error("%s - %s" % (e.filename,e.strerror))
                        sys.exit(0)

                except RuntimeError as e:
                    # If object found as incompatible, then push as not good
                    push_into_dma_object_logs (v_object_schema_name,
                                               v_object_type,
                                               v_object_name,
                                               v_object_status,
                                               e)
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            logger.error ("Oracle ERROR: %s - %s" % (error.code, error.message))
            print ("Oracle Error: %s - %s " % (error.code, error.message))
            sys.exit (0)

    if assessment_flag == 'sql':
        print ('Failed to extract SQL!!..')
        exit(0)
        obj_schema = 'DUMMY'  # Since we are parsing the SQL file no schema name.
        obj_name = get_object_name_from_sqlfile (sqlfilename, assessment_object_type)
        obj_status = 'VALID'  # Since user passing the object its assumed as VALID object
        logger.info ('Extracting DDL... %s,%s' % (obj_name, obj_schema))
        obj_ddl_file_name = extract_ddl_from_sqlfile_and_write_to_file (v_object_schema_name,
                                                                        v_object_type,
                                                                        v_object_name,
                                                                        sqlfilename)

# After completing extracting and parsing the objects by gathering
# incompatibility information in dma_object_logs, generate report
# in two forms 1) Assessment Log and 2) HTML report

# 1) write assessment log file
#-----------------------------

#generate_assessment_log(dma_object_logs,v_number_of_lines_parsed)


# 2) Writing HTMl Report
# Before writing to HTML we need to classify the data and make it
# Migration related information which can define the migration
# efforts. To classify the data, we need to generate a groupby/subgroupby
# on dma_object_logs collected and next we need to publish into the
# html report.
#------------------------------------------------------------------------
logger.info('Generating HTML file - %s ' % dma_html_report_file_name)

#Summarize the data as per the data collected from the assessment.
#and then publish the data to html template.

generate_html_report(dma_object_logs,v_number_of_lines_parsed)
