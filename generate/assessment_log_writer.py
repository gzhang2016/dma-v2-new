###############################################################
#
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavendra Rao
#
# This module handles the writting of Assessment logs of DMA
###############################################################
# Python Modules
from contextlib import redirect_stdout
import pandas as pd
pd.set_option('display.expand_frame_repr', False)

#DMA Modules
from templates.misc.precheck import *


# Write the header part of the DMA assessment logs
#-------------------------------------------------
def print_log_header(a,v,ov,ds,linesparsed):
    header = """
Summary
-------
Date/Time               : %s
EDB Postgres Version    : %s
Oracle Version          : %s
Asessment Schema        : %s
Number of Parsing Lines : %s
""" % (a.strftime ("%B %d, %Y %H:%M:%S"),
       v,
       ov,
       ds,
       linesparsed)
    stage_txt = """
Migration Stages Summary
------|----------------------------------------------------------------------------------------------
|Stage|    Description                                                                              |
------|----------------------------------------------------------------------------------------------
|  0  |    Automatic migration. No changes are needed                                               |
------|----------------------------------------------------------------------------------------------
|  1  |    A manual intervention is needed to change the syntax. The functionality remain the same  |
------|----------------------------------------------------------------------------------------------
|  2  |    Behaviorally difference, hence application logic need to be changed                      |
------|----------------------------------------------------------------------------------------------
|  3  |    Solution exist to achieve the similar functionality in EPAS                              |
------|----------------------------------------------------------------------------------------------
|  4  |    Not Supported, alternative solution need to be used either rewrite or alternative method |
-----------------------------------------------------------------------------------------------------
    """
    print(header)
    print(stage_txt)
    return

#Print Header for every new Object Type
#--------------------------------------
def print_log_object_header(oname):
    print (oname)
    print ("=" * 140)
    print ("{0:25} {1:8} {2:20} {3:30} {4:10} {5:10} {6:50} ".format ('Name',
                                                                      'Mig-Stage',
                                                                      'Failed Reason',
                                                                      'Description',
                                                                      'Line Number',
                                                                      'Status',
                                                                      'Details'
                                                                      ))
    print ("=" * 140)


#Write to the assessment log file by using the object_logs list and
# the assessment log file name
#------------------------------------------------------------------
def generate_assessment_log(ologs,nol):
    logger.info ('Generating DMA Assessment Log file %s' % dma_assess_log_file_name)
    object_dataframe = pd.DataFrame ([vars (f) for f in ologs],columns=['object_type',
                                                                        'object_name',
                                                                        'object_migration_stage',
                                                                        'object_failed_context',
                                                                        'object_failed_code_description',
                                                                        'object_failed_at_line_number',
                                                                        'object_status',
                                                                        'object_failed_line_details'])


    with open(dma_assess_log_file_name,'w') as assess_log_file:
        with redirect_stdout(assess_log_file):
            print_log_header(assess_start_time,'9.6',ORACLE_version,DMA_schema,nol)
            print(object_dataframe.set_index("object_type"))
    """
            # Print DMA assessment Logs Summary
            print_log_header(assess_start_time,'9.6',ORACLE_version,DMA_schema,nol)
            type_tmp = ''
            for o in ologs:
                if o.object_type != type_tmp:
                    print_log_object_header(o.object_type)
                    type_tmp = o.object_type
                if o.object_failed_code != 0:
                    print ("{0:25} "
                           "{1:^8} "
                           "{2:20} "
                           "{3:30} "
                           "{4:^10} "
                           "{5:^10} "
                           "{6:50} ".format (o.object_name,
                                             o.object_migration_stage,
                                             o.object_failed_context,
                                             o.object_failed_code_description,
                                             o.object_failed_at_line_number,
                                             o.object_status,
                                             o.object_failed_line_details
                                             ))
    """
    logger.info ('Writing to DMA Assessment Log file...Completed!')
    return


