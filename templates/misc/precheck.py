#!/usr/bin/env python
###############################################################################
## Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
###############################################################################

# Python Modules

import os
import sys
import logging
from datetime import datetime

# DMA moduels
from templates.cli.cli_args_validator import *

# Variables Declaration
file_timestamp = str (datetime.now ().strftime ("%Y%m%d_%H%M%S"))

#
if assessment_flag == 'sql':
    filename_tag = cli_object_type
else:
    filename_tag = DMA_schema

# Defining the DMA files with Schema Name/Time
dma_html_report_file_name = assessment_files_write_location \
                            + '%s_%s_report.html' % (filename_tag,
                                                     file_timestamp)

dma_assess_log_file_name = assessment_files_write_location \
                           + '%s_%s_assessment.log' % (filename_tag,
                                                       file_timestamp)

dma_logs_file_name = assessment_files_write_location \
                     + '%s_%s_%s.log' % ('DMA',
                                         filename_tag,
                                         file_timestamp)

logging.basicConfig (filename=dma_logs_file_name,
                     level=logging.DEBUG,
                     format='%(asctime)s %(levelname)s %(message)s'
                     )
logger = logging.getLogger (__name__)
logger.info('Starting Migration Assessment of %s..[Schema or Object Type] ..' % filename_tag)
if assessment_flag != 'sql':
    logger.info('Database connection %s ' % conn_string)