#!/usr/bin/env python
###############################################################################
#
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
#
# This module validates all the CLI option processed in cli_options module
# and does the sanity check of the values to pass on.
###############################################################################

import re

# compile few regularex for file search

table_pattern = r'\bCREATE TABLE\b(.*?)\b\;'
function_pattern = r'CREATE FUNCTION(.*?)\/'
package_pattern = r'CREATE PACKAGE(.*?)\b\/'
clearpattern = '[^a-zA-Z]+' #clearing the pattern special characheter
