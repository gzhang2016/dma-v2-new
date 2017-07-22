#################################################################
# Copyright (c) 2000-2017 EnterpriseDB - All rights reserved.
# Author: Raghavedra Rao (raghavendra.rao@enterprisedb.com)
#################################################################

# DMA modules
# ----------
from templates.classes.object_structure import *

# Generate a code list for Oracle to EPAS migration

dma_code.append(DMACodebase(0,'','',0))
dma_code.append(DMACodebase(9999,'Unknown Rule','Unknown Error',4))
dma_code.append(DMACodebase(1001,'create_table_stmt','CREATE TABLE syntax error',0))
dma_code.append(DMACodebase(1002,'datatype','DATA TYPE not supported in EPAS',3))
dma_code.append(DMACodebase(1003,'column_name','TABLE Column name is incorrect',3))
dma_code.append(DMACodebase(1004,'create_package_body','Package Error',3))
dma_code.append(DMACodebase(1005,'create_procedure_body','Procedure Error',3))
dma_code.append(DMACodebase(1006,'create_sequnce','Sequence syntax error',0))
dma_code.append(DMACodebase(1007,'create_trigger','Trigger syntax error',0))
dma_code.append(DMACodebase(1008,'create_synonym','Synonym syntax error',0))
dma_code.append(DMACodebase(1009,'create_view','View syntax error',0))
dma_code.append(DMACodebase(1010,'create_package','Package syntax error',3))
dma_code.append(DMACodebase(1011,'procedure_spec','Procedure specification syntax error',3))
dma_code.append(DMACodebase(1012,'function_spec','Fucntion specification syntax error',0))
dma_code.append(DMACodebase(1013,'function_body','Function Body syntax error',0))
dma_code.append(DMACodebase(1014,'procedure_body','Procedure Body syntax error',0))
dma_code.append(DMACodebase(1015,'attribute_definition','Variable Declaration syntax error',3))
dma_code.append(DMACodebase(1016,'subprogram_spec','Sub Program syntax error',3))
dma_code.append(DMACodebase(1017,'java_spec','Java object syntax error',4))
dma_code.append(DMACodebase(1018,'create_materialized_view','MV syntax error',3))
dma_code.append(DMACodebase(1019,'sql_statements','DML statement syntax error',3))
dma_code.append(DMACodebase(1020,'raise_statement','Exception syntax error',4))
dma_code.append(DMACodebase(1021,'between_bound','Bound syntax error',4))
dma_code.append(DMACodebase(1022,'select_statement','SELECT syntax error',3))
dma_code.append(DMACodebase(1023,'merge_statement','Unsupported DML error',3))
dma_code.append(DMACodebase(1024,'update_statement','UPDATE syntax error',3))
dma_code.append(DMACodebase(1025,'delete_statement','DELETE syntax error',3))
dma_code.append(DMACodebase(1026,'insert_statement','INSERT syntax error',3))
dma_code.append(DMACodebase(1027,'create_index','Index syntax error',3))
dma_code.append(DMACodebase(1028,'partition_by_clause','Partition syntax error',3))
dma_code.append(DMACodebase(1029,'pragma_declaration','PRAGMA syntax error',3))
dma_code.append(DMACodebase(1030,'type_declaration','TYPE body syntax error',3))
