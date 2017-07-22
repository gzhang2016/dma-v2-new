#################################################################
# Copyright (c) 2000-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao (raghavendra.rao@enterprisedb.com)
#################################################################

# DMA modules
# ----------
from templates.misc.precheck import *

# Antlr4 Modules
# --------------
from antlr4.error.ErrorListener import *

# Global variables those are used through out
# DMA program for storing assessment details

dma_object_logs = []                # main list variable that captures object_logs class objects
dma_object_logs_tmp = []            # mock of obect_logs for temporary purpose
dma_code = []                       # main list which holds all the code of DMACodebase
v_schema_level_summary = []         # store schemal level summary table in html report
v_schema_incompatible_summary = []  # store schemal incompatibility summary table in html report
v_schema_object_summary = []        # store schemal object summary table in html report
v_schema_object_status_summary = [] # store schemal object status summary table in html report
v_migration_stage_summary = ''      # store schemal migration stage summary table in html report
v_number_of_lines_parsed = 0        # To capture number of lines processed
v_company_name = 'XYZ'
v_total_objects = 0                 # Capture total objects of assessment
v_total_storage_objects = 0         # Capture total storage objects
v_total_code_objects = 0            # Capture total code objects
headers_for_logs = ['Schema Name', 'Object Type', 'Name', 'Status',
                    'Error Code', 'Code Description','Failed Context',
                    'Failed Line Details','Failed at Line', 'Migration Stage']

object_logs_columns = ['object_schema_name', 'object_type', 'object_name', 'object_status',
                       'object_failed_code', 'object_failed_code_description',
                       'object_failed_context', 'object_failed_line_details',
                       'object_failed_at_line_number', 'object_migration_stage']

#--------------
# List of Object Types that DMA can do Assessment
#--------------
assessment_objects_list = ['ALL',
                           #'CLUSTER',
                           'FUNCTION',
                           'INDEX',
                           #'JAVA_CLASS',
                           'PACKAGE',
                           'PACKAGE BODY',
                           'PROCEDURE',
                           #'PROGRAM',
                           'SEQUENCE',
                           'SYNONYM',
                           'TABLE',
                           'TRIGGER',
                           'TYPE',
                           #'TYPE BODY',
                           'VIEW',
                           #'MATERIALIZED VIEW'
                           #'SQL'
                         ]

call_object_rulename = {'ALL': 'unit_statement',
                        'INDEX': 'create_index',
                        'FUNCTION': 'create_function_body',
                        'PACKAGE': 'create_package',
                        'PACKAGE BODY': 'create_package_body',
                        'PROCEDURE': 'create_procedure_body',
                        'SEQUENCE': 'create_sequence',
                        'SYNONYM': 'create_synonym',
                        'TABLE': 'create_table',
                        'TRIGGER': 'create_trigger',
                        'TYPE': 'create_type',
                        'VIEW': 'create_view',
                        'MATERIALIZED VIEW': 'create_materialized_view'
                        }

#-------------------------------------------------------------------
#  Object_Logs is the main class object which stores all
# information gathered from extractor and parser. This class object
# can be used for further detailed filetering to write Logging
# & HTML report generation.
#
# Object_Logs
#      object_schema_name - Assessment Schema name
#      object_type - Object type (table,view,function,package)
#      object_name - Object name
#      object_status - Object status (valid/invalid
#      object_failed_code - Retrieve code from DMACodebase(code)
#      object_failed_code_description - Retrieve code from DMACodebase(description)
#      object_failed_context - Object Failed error context
#      object_failed_line_details - Object Failed error context
#      object_failed_at_line_number - Object Failed  at line number
#      object_migration_stage - Object Migration Stage DMACodebase(stage)
#-------------------------------------------------------------------

class Object_Logs (object):
    def __init__(self,
                 object_schema_name,
                 object_type,
                 object_name,
                 object_status,
                 object_failed_code,
                 object_failed_code_description,
                 object_failed_context,
                 object_failed_line_details,
                 object_failed_at_line_number,
                 object_migration_stage
                 ):
        self.object_schema_name = object_schema_name
        self.object_type = object_type
        self.object_name = object_name
        self.object_status = object_status
        self.object_failed_code = object_failed_code
        self.object_failed_code_description = object_failed_code_description
        self.object_failed_context = object_failed_context
        self.object_failed_line_details = object_failed_line_details
        self.object_failed_at_line_number = object_failed_at_line_number
        self.object_migration_stage = object_migration_stage

    def __str__(self):
        return "{0:15}{1:15}{2:25}{3:8}{4:^4}{5:50}{6:20}{7:100}{8:^3}{9:1}".format(self.object_schema_name,
                                                             self.object_type,
                                                             self.object_name,
                                                             self.object_status,
                                                             self.object_failed_code,
                                                             self.object_failed_code_description,
                                                             self.object_failed_context,
                                                             self.object_failed_line_details,
                                                             self.object_failed_at_line_number,
                                                             self.object_migration_stage)

    def __repr__(self):
        return '\t%s\t%s\t%s\t%s\t%d\t%s\t%s\t%s\t%d\t%d' % (self.object_schema_name,
                                                             self.object_type,
                                                             self.object_name,
                                                             self.object_status,
                                                             self.object_failed_code,
                                                             self.object_failed_code_description,
                                                             self.object_failed_context,
                                                             self.object_failed_line_details,
                                                             self.object_failed_at_line_number,
                                                             self.object_migration_stage)

#-------------------------------------------------------------------
# DMAErrorListener
#   This is the main listener that parser scanns the object with
#   a defined rule and throw error when it encounteres mismatch.
#   In such case, we need to capture rule_name, line, context and
#   line text of the file. Using that information we can match rule_name
#   with DMAErrorCodebase for migration information and to push object
#   under stages.
#-------------------------------------------------------------------

class DMAErrorListener (ErrorListener):
    #Catch the Error encountered in the rule with
    #Rule Name, Line Number, incompatible token & Context
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # incompabible token is "offendingSymbol.text"
        # Line nuber is "line"
        # Capture Rule name
        #---------------------------------------------
        rule_stack = recognizer.getRuleInvocationStack()
        rule_stack.reverse()
        error_caught_in_rule = (str(rule_stack[-1]))

        # Capture incompatible line as context
        #----------------------------------------------
        line_tokens = recognizer.getInputStream()
        input_tokens = str(line_tokens.tokenSource._input)
        lines = input_tokens.split('\n')
        errorline = lines[line -1]
        context = offendingSymbol.text
        # return the Rule name,line number, incompatible token & context
        raise RuntimeError(line, error_caught_in_rule, context.strip(), errorline.strip())


#-------------------------------------------------------------------
# DMACodebase class will hold the migration infomration about
# the object migratable to EPAS or not from any Database. However
# one should write ErrorCodebase manually on the compatibility.
#
# DMACodebase
#   code - code for an error encountered on specific rule
#   rule_name - parser rule name
#   description - rule description
#   stage - An incompatible object migration category classification
#           which can be any (0,1,2,3,4).
#           0 - Automatic migration. No changes are needed
#           1 - A manual intervention is needed to change the syntax.
#               The functionality remain the same.
#           2 - Behaviorally difference, hence application logic
#               need to be changed
#           3 - Solution exist to achieve the similar functionality
#               in EPAS
#           4 - Not Supported, alternative solution need to be used
#               either rewrite or alternative method.
#-------------------------------------------------------------------

class DMACodebase(object):
    def __init__(self,
                 code,
                 rule_name,
                 description,
                 stage):
        self.code = code
        self.rule_name = rule_name
        self.description = description
        self.stage = stage

#-------------------------------------------------------------------
# HTML and Log supportive Classes for reporting and logging
#-------------------------------------------------------------------

# Schema Level Summary
class SchemaLevelSummary (object):
    def __init__(self,
                 object_type,
                 no_of_objects_assessed,
                 no_of_incompatible_objects,
                 migration_ratio):
        self.object_type = object_type
        self.no_of_objects_assessed = no_of_objects_assessed
        self.no_of_incompatible_objects = no_of_incompatible_objects
        self.migration_ratio = migration_ratio

    def __str__(self):
        return "\t%s\t%d\t%d\t%d" % (self.object_type,
                                     self.no_of_objects_assessed,
                                     self.no_of_incompatible_objects,
                                     self.migration_ratio)

