#!/bin/bash

#export ORACLE_HOME=/opt/oracle/instantclient_12_2
#export LD_LIBRARY_PATH=$ORACLE_HOME
#export PATH=$PATH:$ORACLE_HOME


### Setting Oracle client on the Mac
#
export ORACLE_HOME=/opt/oracle/instantclient_12_1
export PYTHONPATH=/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
export DYLIB_LIBRARY_PATH=$ORACLE_HOME
export DYLD_FALLBACK_LIBRARY_PATH=/opt/oracle/instantclient_12_1
export LD_LIBRARY_PATH=$ORACLE_HOME
export PATH=$PYTHONPATH:$ORACLE_HOME:$PATH