#!/usr/bin/env python
###############################################################################
#
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao
#
# This module is used to run queries agains Oracle Database to extract the
# METADATA of the object using DBMS_METADATA.GET_DDL() function
###############################################################################

ddl_transform = """
    BEGIN
    DBMS_METADATA.SET_TRANSFORM_PARAM( DBMS_METADATA.SESSION_TRANSFORM, 'PRETTY',             TRUE );
    DBMS_METADATA.SET_TRANSFORM_PARAM( DBMS_METADATA.SESSION_TRANSFORM, 'SQLTERMINATOR',      TRUE );
    DBMS_METADATA.SET_TRANSFORM_PARAM( DBMS_METADATA.SESSION_TRANSFORM, 'REF_CONSTRAINTS',    FALSE);
    DBMS_METADATA.SET_TRANSFORM_PARAM( DBMS_METADATA.SESSION_TRANSFORM, 'OID',                FALSE);
    DBMS_METADATA.SET_TRANSFORM_PARAM( DBMS_METADATA.SESSION_TRANSFORM, 'SEGMENT_ATTRIBUTES', FALSE);
    DBMS_METADATA.SET_TRANSFORM_PARAM( DBMS_METADATA.SESSION_TRANSFORM, 'TABLESPACE',         FALSE);
    DBMS_METADATA.SET_TRANSFORM_PARAM( DBMS_METADATA.SESSION_TRANSFORM, 'EMIT_SCHEMA',        FALSE);
    END;"""

ddl_query = ("select object_name,status "
             "from dba_objects "
             "where object_type = '%s'"
             "and OWNER='%s' "
             "ORDER BY object_NAME ")
