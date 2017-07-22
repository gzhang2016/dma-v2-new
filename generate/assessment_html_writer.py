###############################################################
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavendra Ra
#
# This module is to build the html related data and publish the
# data into html sections.
###############################################################
# Python Modules
import pandas as pd
from contextlib import redirect_stdout

# DMA Modules
from templates.classes.object_structure import *
from templates.misc.precheck import *
from templates.html.html_structure import *


# Collecting total object count
# ------------------------------
def gather_total_assessment_objects(odf):
    uname = (odf.object_type + odf.object_name)
    return len (uname.unique ())


# Collecting Migration Stages of objects
# ---------------------------------------
def collect_migration_stages_data(odf):
    x = odf.groupby (['object_type',
                      'object_name']).object_migration_stage.agg (['max'])
    y = dict (x.groupby ('max').size ())
    return y


# Collecting Schema Level Summary of the objects
# -----------------------------------------------
def collect_schema_level_summary(ol):
    tuple_list = []
    assessed_obj = 0
    incmptble_obj = 0
    obj_name = ''
    obj_type = ol[0].object_type
    for i in ol:
        if i.object_type == obj_type:
            if i.object_name != obj_name:
                assessed_obj = assessed_obj + 1
                if i.object_failed_code != 0:
                    incmptble_obj = incmptble_obj + 1

        if i.object_type != obj_type:
            per = (100 - round (incmptble_obj / assessed_obj * 100, 2))
            tuple_list.append (SchemaLevelSummary (obj_type,
                                                   assessed_obj,
                                                   incmptble_obj,
                                                   per))
            assessed_obj = 0
            incmptble_obj = 0
            if i.object_name != obj_name:
                assessed_obj = assessed_obj + 1
                if i.object_failed_code != 0:
                    incmptble_obj = incmptble_obj + 1
        obj_name = i.object_name
        obj_type = i.object_type

    per = (100 - round (incmptble_obj / assessed_obj * 100, 2))
    tuple_list.append (SchemaLevelSummary (obj_type,
                                           assessed_obj,
                                           incmptble_obj,
                                           per))
    return tuple_list

# Schema Level Incompatibility summary
#------------------------------------
def collect_schema_incompatible_summary_data(odf):
    sl = odf.groupby(['object_type','object_failed_context']).size()
    return sl

# Schema Object Level Summary
#----------------------------
def collect_schema_object_level_summary(odf):
    cols = ['object_type',
            'object_name',
            'object_failed_context',
            'object_failed_line_details',
            'object_failed_at_line_number']
    sol = odf[cols]
    return sol

# Schema Object Status summary
#-----------------------------
def collect_schema_object_status_summary_data(odf):
    cols = ['object_type',
            'object_unique'
            ]
    odf['object_unique'] = (odf.object_type + odf.object_name)
    osl = odf[cols]
    osl.drop_duplicates('object_unique')
    return osl.groupby('object_type').count()

# Generating the HTML report

def generate_html_report(ologs, nol):
    # Before writing the report, classify the data required for the
    # HTML report tables and then publish.
    # Call function to collect data and write into class objects list
    # ---------------------------------------------------------------
    # Push all dma_object_logs into pandas dataframe
    objectlogs_df = pd.DataFrame ([vars (f) for f in ologs],
                                  columns=object_logs_columns)
    # Get the total objects assessed - Returns inteter
    v_total_objects = gather_total_assessment_objects (objectlogs_df)
    #print (v_total_objects)

    # get the migration stage_summary - Returns Dict
    v_migration_stage_summary = collect_migration_stages_data (objectlogs_df)
    #print (v_migration_stage_summary)

    # get the schema level summary - Returns List of Objects(SchemaLevelSummary class)
    v_schema_level_summary = collect_schema_level_summary (ologs)
    #for i in v_schema_level_summary: print (i)

    # Collect schema incompatibility summary - Returns Pandas Series
    v_schema_incompatible_summary = collect_schema_incompatible_summary_data(objectlogs_df)
    """
    x = ''
    for i, v in v_schema_incompatible_summary.iteritems ():
        if i[0] != x:
            print (i[0], i[1], v)
            x = i[0]
        else:
            print(i[1],v)
    """
    # Collect schema object Level summary - Returns Data Frame
    v_schema_object_summary = collect_schema_object_level_summary(objectlogs_df)
    """
    for index, row in v_schema_object_summary.iterrows ():
        print (row[0], row[1], row[2], row[3], row[4])
    """
    # Collect schema object status summary - Returns DataFrame
    v_schema_object_status_summary = collect_schema_object_status_summary_data(objectlogs_df)
    """
    for i, v in v_schema_object_status_summary.iterrows ():
        print ("O - %s Tot - %d V - %d I - %d" % (i, v,v,0))
    """
    #Write HTML report
    #-----------------
    with open(dma_html_report_file_name,'w') as html_report_file:
        with redirect_stdout(html_report_file):
            print(html_css_style)
            print(html_header)
            print(html_sidebar)
            # Print executive summary
            #------------------------
            print(middle_content_executive_summary % (str(assess_start_time),
                                                      ORACLE_sid_or_service,
                                                      DMA_schema,
                                                      str(v_total_objects),
                                                      "N/a",
                                                      str(nol)))
            #Print Migration status summary
            #-----------------------------
            mlist = []
            for i in range(0,5):
                if i in v_migration_stage_summary:
                    mlist.append(v_migration_stage_summary[i])
                else:
                    mlist.append(0)
            print(migration_stage_summary % (mlist[0],
                                             mlist[1],
                                             mlist[2],
                                             mlist[3],
                                             mlist[4]))
            #Print Schema level Summary
            #--------------------------
            print(schema_level_summary_table_header)
            for i in v_schema_level_summary:
                print (schema_level_summary_table_rowiterator % (i.object_type,
                                                                        i.no_of_objects_assessed,
                                                                        i.no_of_incompatible_objects,
                                                                        i.migration_ratio))
            # Print Schema Incompatibility summary
            #-------------------------------------
            print(schema_incompatible_summary_header)
            x = ''
            for i, v in v_schema_incompatible_summary.iteritems ():
                if i[0] != x:
                    print (schema_incompatible_summary_rowiterator % (i[0],
                                                                      i[1],
                                                                      v))
                    x = i[0]
                else:
                    print (schema_incompatible_summary_rowiterator % ('',
                                                                      i[1],
                                                                      v))
            #Print Schema Objects Summary
            #----------------------------
            print(schema_object_level_summary_header)
            x = ''
            for index, row in v_schema_object_summary.iterrows ():
                if (row[2] != ''):
                    if (row[1] != x):
                        print (schema_object_level_summary_rowiterator % (row[0],
                                                                          row[1],
                                                                          row[2],
                                                                          row[3].strip (),
                                                                          row[4]))
                    x = row[1]
            # Print Object Status summary
            #---------------------------
            print(schema_object_status_summary_header)
            for i, v in v_schema_object_status_summary.iterrows ():
                print (schema_object_status_summary_rowiterator % (i,
                                                                   v,
                                                                   v,
                                                                   0))

            # Print closure of html and bottom tag
            #-------------------------------------
            print(html_tags_closure)
            print(html_bottom)

