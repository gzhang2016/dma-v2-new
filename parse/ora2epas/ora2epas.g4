/**
 * EnterpriseDB Corporation(c) EDB-SPL/SQL Parser
 * Author: Raghavendra Rao
 *
 * EDB-SPL/SQL Grammar file written using the Antlr site published
 * Oracle Plsql/SQL Grammar files.
 *
 * Every rule in the Antlr4 Plsql grammar files has been revisited
 * and modified according to EDB Postgres. Each rule in this grammar
 * file is the representation of the EDB Postgres. This grammar files
 * purely written to parse the SQL/PLSQL objects that is suitable to
 * create in EDB Postgres. EDB owns this grammar file and has complete
 * distribution/modification writes.
 *
 * Few important points on the grammar files brought from Antlr4 Site
 *  1) Antlr4 Site grammar files has NO KNOWLEDGE OF SUPPORTED PACKAGES
 *  2) KEYWORDS are not tracked completely
 *  3) PLSQL objects are written as per Oracle which won't fit for EDB Postgres
 */

grammar ora2epas;

options
{
    language=Python3;
}

swallow_to_semi
    : ~';'+
    ;

compilation_unit
    : unit_statement* EOF
    ;

sql_script
    : ((unit_statement | sql_plus_command) SEMICOLON?)* EOF
    ;

unit_statement
    : create_cluster_table
    | create_database_links
    | create_function_body
    | create_index
    | create_package
    | create_package_body  //treating as individual object
    | create_procedure_body
    | create_table
    | create_sequence
    | create_synonym
    | create_trigger
    | create_type //it includes type_body
    | create_view
    | create_materialized_view
    | sql_statements //Parse DMLs and Select Statements
    | anonymous_block
//  | create_java_objects //todo
    ;


/* Cluster Tables */
create_cluster_table
    : .
    ;

/* Database Links */

create_database_links
    : dblink_name
    ;

/* CREATE FUNCTION statement */

create_function_body
    : CREATE (OR REPLACE)? FUNCTION function_name ('(' parameter (',' parameter)*  ')')?
      RETURN type_spec (invoker_rights_clause | parallel_enable_clause | DETERMINISTIC)*
      (((IS | AS)
        (DECLARE?
         declare_spec*
         body
         | call_spec))
      | (AGGREGATE) USING implementation_type_name) ';'?
    ;

parallel_enable_clause
    : PARALLEL_ENABLE partition_by_clause?
    ;

partition_by_clause
    : '(' PARTITION expression BY (ANY | (HASH | RANGE) '(' column_name (',' column_name)* ')')streaming_clause? ')'
    ;

streaming_clause
    : (ORDER | CLUSTER) expression BY '(' column_name (',' column_name)* ')'
    ;

// Indexes

create_index
    : index_name
    ;

// $<Package DDLs

create_package
    : CREATE (OR REPLACE)? PACKAGE package_name invoker_rights_clause? (IS | AS) package_obj_spec* END package_name? ';'
    ;

create_package_body
    : CREATE (OR REPLACE)? PACKAGE BODY package_name (IS | AS) package_obj_body* (BEGIN seq_of_statements | END package_name?) ';'
    ;

// $<Create Package - Specific Clauses

package_obj_spec
    : variable_declaration
    | subtype_declaration
    | cursor_declaration
    | exception_declaration
    | pragma_declaration
    | type_declaration
    | procedure_spec
    | function_spec
    ;

procedure_spec
    : PROCEDURE identifier ('(' parameter ( ',' parameter )* ')')? ';'
    ;

function_spec
    : FUNCTION identifier ('(' parameter ( ',' parameter)* ')')? RETURN type_spec (DETERMINISTIC)? ';'
    ;

package_obj_body
    : variable_declaration
    | subtype_declaration
    | cursor_declaration
    | exception_declaration
    | type_declaration
    | procedure_body
    | function_body
    | procedure_spec
    | function_spec
    ;

// $<Procedure DDLs

function_body
    : FUNCTION identifier ('(' parameter (',' parameter)* ')')?
      RETURN type_spec (invoker_rights_clause|parallel_enable_clause|DETERMINISTIC)*
      ((PIPELINED? (IS | AS) (DECLARE? declare_spec* body | call_spec)) | (PIPELINED | AGGREGATE) USING implementation_type_name) ';'
    ;

procedure_body
    : PROCEDURE identifier ('(' parameter (',' parameter)* ')')?
      (IS | AS)
      (DECLARE? declare_spec* body | call_spec | EXTERNAL) ';'
    ;

create_procedure_body
    : CREATE (OR REPLACE)? PROCEDURE procedure_name ('(' parameter (',' parameter)* ')')?
      invoker_rights_clause? (IS | AS)
      (DECLARE? declare_spec* body | call_spec | EXTERNAL) ';'
    ;

// $>

// $<Trigger DDLs

create_trigger
    : CREATE ( OR REPLACE )? TRIGGER trigger_name
    (simple_dml_trigger | compound_dml_trigger | non_dml_trigger)
    trigger_follows_clause? (ENABLE | DISABLE)? trigger_when_clause? trigger_body ';'
    ;

trigger_follows_clause
    : FOLLOWS trigger_name (',' trigger_name)*
    ;

trigger_when_clause
    : WHEN '(' condition ')'
    ;

// $<Create Trigger- Specific Clauses

simple_dml_trigger
    : (BEFORE | AFTER | INSTEAD OF) dml_event_clause referencing_clause? for_each_row?
    ;

for_each_row
    : FOR EACH ROW
    ;

compound_dml_trigger
    : FOR dml_event_clause referencing_clause?
    ;

non_dml_trigger
    : (BEFORE | AFTER) non_dml_event (OR non_dml_event)* ON (DATABASE | (schema_name '.')? SCHEMA)
    ;

trigger_body
    : COMPOUND TRIGGER
    | CALL identifier
    | trigger_block
    ;

routine_clause
    : routine_name function_argument?
    ;

compound_trigger_block
    : COMPOUND TRIGGER declare_spec* timing_point_section+ END trigger_name
    ;

timing_point_section
    : bk=BEFORE STATEMENT IS trigger_block BEFORE STATEMENT ';'
    | bk=BEFORE EACH ROW IS trigger_block BEFORE EACH ROW ';'
    | ak=AFTER STATEMENT IS trigger_block AFTER STATEMENT ';'
    | ak=AFTER EACH ROW IS trigger_block AFTER EACH ROW ';'
    ;

non_dml_event
    : ALTER
    | ANALYZE
    | AUDIT
    | COMMENT
    | CREATE
    | DROP
    | GRANT
    | NOAUDIT
    | RENAME
    | REVOKE
    | TRUNCATE
    | DDL
    | STARTUP
    | SHUTDOWN
    | DB_ROLE_CHANGE
    | LOGON
    | LOGOFF
    | SERVERERROR
    | SUSPEND
    | DATABASE
    | SCHEMA
    | FOLLOWS
    ;

dml_event_clause
    : dml_event_element (OR dml_event_element)* ON dml_event_nested_clause? tableview_name
    ;

dml_event_element
    : (DELETE|INSERT|UPDATE) (OF column_name (',' column_name)*)?
    ;

dml_event_nested_clause
    : NESTED TABLE tableview_name OF
    ;

referencing_clause
    : REFERENCING referencing_element+
    ;

referencing_element
    : (NEW | OLD | PARENT) column_alias
    ;

// $<Type DDLs

create_type
    : CREATE (OR REPLACE)? TYPE (type_definition | type_body) ';'
    ;

// $<Create Type - Specific Clauses
type_definition
    : type_name (OID CHAR_STRING)? object_type_def?
    ;

object_type_def
    : invoker_rights_clause? (object_as_part | object_under_part) sqlj_object_type?
      ('(' object_member_spec (',' object_member_spec)* ')')? modifier_clause*
    ;

object_as_part
    : (IS | AS) (OBJECT | varray_type_def | nested_table_type_def)
    ;

object_under_part
    : UNDER type_spec
    ;

nested_table_type_def
    : TABLE OF type_spec (NOT NULL)?
    ;

sqlj_object_type
    : EXTERNAL NAME expression LANGUAGE JAVA USING (SQLDATA|CUSTOMDATUM|ORADATA)
    ;

type_body
    : BODY type_name (IS | AS) (type_body_elements)+ END
    ;

type_body_elements
    : map_order_func_declaration
    | subprog_decl_in_type
    ;

map_order_func_declaration
    : (MAP | ORDER) MEMBER func_decl_in_type
    ;

subprog_decl_in_type
    : (MEMBER | STATIC) (proc_decl_in_type | func_decl_in_type | constructor_declaration)
    ;

proc_decl_in_type
    : PROCEDURE procedure_name '(' type_elements_parameter (',' type_elements_parameter)* ')'
      (IS | AS) (call_spec | DECLARE? declare_spec* body ';')
    ;

func_decl_in_type
    : FUNCTION function_name ('(' type_elements_parameter (',' type_elements_parameter)* ')')?
      RETURN type_spec (IS | AS) (call_spec | DECLARE? declare_spec* body ';')
    ;

constructor_declaration
    : FINAL? INSTANTIABLE? CONSTRUCTOR FUNCTION type_spec
      ('(' (SELF IN OUT type_spec ',') type_elements_parameter (',' type_elements_parameter)*  ')')?
      RETURN SELF AS RESULT (IS | AS) (call_spec | DECLARE? declare_spec* body ';')
    ;

// $> Views

create_view
    : view_name
    ;

// Materialized view

create_materialized_view
    : mview_name
    ;

// $<Common Type Clauses

modifier_clause
    : NOT? (INSTANTIABLE | FINAL | OVERRIDING)
    ;

object_member_spec
    : identifier type_spec sqlj_object_type_attr?
    | element_spec
    ;

sqlj_object_type_attr
    : EXTERNAL NAME expression
    ;

element_spec
    : modifier_clause? element_spec_options+ (',' pragma_clause)?
    ;

element_spec_options
    : subprogram_spec
    | constructor_spec
    | map_order_function_spec
    ;

subprogram_spec
    : (MEMBER|STATIC) (type_procedure_spec|type_function_spec)
    ;

type_procedure_spec
    : PROCEDURE procedure_name '(' type_elements_parameter (',' type_elements_parameter)* ')' ((IS | AS) call_spec)?
    ;

type_function_spec
    : FUNCTION function_name ('(' type_elements_parameter (',' type_elements_parameter)* ')')?
      RETURN (type_spec | SELF AS RESULT) ((IS | AS) call_spec | EXTERNAL VARIABLE? NAME expression)?
    ;

constructor_spec
    : FINAL? INSTANTIABLE? CONSTRUCTOR FUNCTION type_spec ('(' (SELF IN OUT type_spec ',') type_elements_parameter (',' type_elements_parameter)*  ')')?  RETURN SELF AS RESULT ((IS | AS) call_spec)?
    ;

map_order_function_spec
    : (MAP | ORDER) MEMBER type_function_spec
    ;

pragma_clause
    : PRAGMA RESTRICT_REFERENCES '(' pragma_elements (',' pragma_elements)* ')'
    ;

pragma_elements
    : identifier
    | DEFAULT
    ;

type_elements_parameter
    : parameter_name type_spec
    ;

// $<Sequence DDLs


create_sequence
    : CREATE SEQUENCE sequence_name (sequence_start_clause | sequence_spec)* ';'
    ;

// $<Common Sequence

sequence_spec
    : INCREMENT BY UNSIGNED_INTEGER
    | MAXVALUE UNSIGNED_INTEGER
    | NOMAXVALUE
    | MINVALUE UNSIGNED_INTEGER
    | NOMINVALUE
    | CYCLE
    | NOCYCLE
    | CACHE UNSIGNED_INTEGER
    | NOCACHE
    | ORDER
    | NOORDER
    ;

sequence_start_clause
    : START WITH UNSIGNED_INTEGER
    ;

// $<Table DDL Clauses

create_table
    : CREATE TABLE tableview_name LEFT_PAREN column_name datatype (COMMA column_name datatype)* RIGHT_PAREN SEMICOLON
    ;


comment_on_column
    : COMMENT ON COLUMN tableview_name PERIOD column_name IS quoted_string
    ;

// $<Synonym DDL Clauses

create_synonym
    // Synonym's schema cannot be specified for public synonyms
    : CREATE (OR REPLACE)? PUBLIC SYNONYM synonym_name FOR (schema_name PERIOD)? schema_object_name (AT_SIGN link_name)?
    | CREATE (OR REPLACE)? SYNONYM (schema_name PERIOD)? synonym_name FOR (schema_name PERIOD)? schema_object_name (AT_SIGN link_name)?
    ;

comment_on_table
    : COMMENT ON TABLE tableview_name IS quoted_string
    ;

// $<Anonymous PL/SQL code block

anonymous_block
    : BEGIN seq_of_statements END SEMICOLON
    ;

// $<Common DDL Clauses

invoker_rights_clause
    : AUTHID (CURRENT_USER|DEFINER)
    ;

compiler_parameters_clause
    : identifier '=' expression
    ;

call_spec
    : LANGUAGE (java_spec | c_spec)
    ;

// $<Call Spec - Specific Clauses

java_spec
    : JAVA NAME CHAR_STRING
    ;

c_spec
    : C_LETTER (NAME CHAR_STRING)? LIBRARY identifier c_agent_in_clause? (WITH CONTEXT)? c_parameters_clause?
    ;

c_agent_in_clause
    : AGENT IN '(' expression (',' expression)* ')'
    ;

c_parameters_clause
    : PARAMETERS '(' (expression (',' expression)* | '.' '.' '.') ')'
    ;

// $>

parameter
    : parameter_name (IN | OUT | INOUT | NOCOPY)* type_spec? default_value_part?
    ;

default_value_part
    : (ASSIGN_OP | DEFAULT) expression
    ;

// $<PL/SQL Elements Declarations

declare_spec
    : variable_declaration
    | subtype_declaration
    | cursor_declaration
    | exception_declaration
    | pragma_declaration
    | type_declaration
    | procedure_spec
    | function_spec
    | procedure_body
    | function_body
    ;

//incorporates constant_declaration
variable_declaration
    : identifier CONSTANT? type_spec (NOT NULL)? default_value_part? ';'
    | identifier
    ;

subtype_declaration
    : SUBTYPE identifier IS type_spec (RANGE expression '..' expression)? (NOT NULL)? ';'
    ;

//cursor_declaration incorportates curscursor_body and cursor_spec
cursor_declaration
    : CURSOR identifier ('(' parameter_spec (',' parameter_spec)* ')' )? (RETURN type_spec)? (IS select_statement)? ';'
    ;

parameter_spec
    : parameter_name (IN? type_spec)? default_value_part?
    ;

exception_declaration
    : identifier EXCEPTION ';'
    ;

pragma_declaration
    : PRAGMA (SERIALLY_REUSABLE
    | AUTONOMOUS_TRANSACTION
    | EXCEPTION_INIT '(' exception_name ',' numeric_negative ')'
    | INLINE '(' id1=identifier ',' expression ')'
    | RESTRICT_REFERENCES '(' (identifier | DEFAULT) (',' identifier)+ ')') ';'
    ;

// $<Record Declaration - Specific Clauses

//incorporates ref_cursor_type_definition
record_type_def
    : RECORD '(' field_spec (',' field_spec)* ')'
    ;

field_spec
    : column_name type_spec? (NOT NULL)? default_value_part?
    ;

ref_cursor_type_def
    : REF CURSOR (RETURN type_spec)?
    ;

// $>

type_declaration
    :  TYPE identifier IS (table_type_def | varray_type_def | record_type_def | ref_cursor_type_def) ';'
    ;

table_type_def
    : TABLE OF type_spec table_indexed_by_part? (NOT NULL)?
    ;

table_indexed_by_part
    : (idx1=INDEXED | idx2=INDEX) BY type_spec
    ;

varray_type_def
    : (VARRAY | VARYING ARRAY) '(' expression ')' OF type_spec (NOT NULL)?
    ;

// $>

// $<PL/SQL Statements

seq_of_statements
    : (statement (';' | EOF) | label_declaration)+
    ;

label_declaration
    : ltp1= '<' '<' label_name '>' '>'
    ;

statement
    : CREATE swallow_to_semi
    | ALTER swallow_to_semi
    | GRANT ALL? swallow_to_semi
    | TRUNCATE swallow_to_semi
    | body
    | block
    | assignment_statement
    | continue_statement
    | exit_statement
    | goto_statement
    | if_statement
    | loop_statement
    | forall_statement
    | null_statement
    | raise_statement
    | return_statement
    | case_statement/*[true]*/
    | sql_statement
    | function_call
    ;

assignment_statement
    : (general_element | bind_variable) ASSIGN_OP expression
    ;

continue_statement
    : CONTINUE label_name? (WHEN condition)?
    ;

exit_statement
    : EXIT label_name? (WHEN condition)?
    ;

goto_statement
    : GOTO label_name
    ;

if_statement
    : IF condition THEN seq_of_statements elsif_part* else_part? END IF
    ;

elsif_part
    : ELSIF condition THEN seq_of_statements
    ;

else_part
    : ELSE seq_of_statements
    ;

loop_statement
    : label_name? (WHILE condition | FOR cursor_loop_param)? LOOP seq_of_statements END LOOP label_name?
    ;

// $<Loop - Specific Clause

cursor_loop_param
    : index_name
    | index_name IN REVERSE?
    | index_name IN UNSIGNED_INTEGER DOUBLE_PERIOD UNSIGNED_INTEGER
    | index_name IN UNSIGNED_INTEGER DOUBLE_PERIOD index_name
    | record_name IN (cursor_name expression_list? | '(' select_statement ')')
    ;
// $>

forall_statement
    : FORALL index_name IN bounds_clause sql_statement (SAVE EXCEPTIONS)?
    ;

bounds_clause
    : lower_bound '..' upper_bound
    | INDICES OF collection_name between_bound?
    | VALUES OF index_name
    ;

between_bound
    : BETWEEN lower_bound AND upper_bound
    ;

lower_bound
    : concatenation
    ;

upper_bound
    : concatenation
    ;

null_statement
    : NULL
    ;

raise_statement
    : RAISE exception_name?
    ;

return_statement
    : RETURN expression?
    ;

function_call
    : CALL? routine_name function_argument?
    ;

body
    : BEGIN seq_of_statements (EXCEPTION exception_handler+)? END label_name?
    ;

// $<Body - Specific Clause

exception_handler
    : WHEN exception_name (OR exception_name)* THEN seq_of_statements
    ;

// $>

trigger_block
    : (DECLARE? declare_spec+)? body
    ;

block
    : DECLARE? declare_spec+ body
    ;

// $>

// $<SQL PL/SQL Statements

sql_statement
    : execute_immediate
    | sql_statements
    | cursor_manipulation_statements
    | transaction_control_statements
    ;

execute_immediate
    : EXECUTE IMMEDIATE expression (into_clause using_clause? | using_clause dynamic_returning_clause? | dynamic_returning_clause)?
    ;

// $<Execute Immediate - Specific Clause
dynamic_returning_clause
    : (RETURNING | RETURN) into_clause
    ;
// $>


// $<DML SQL PL/SQL Statements

sql_statements
    : select_statement
    | update_statement
    | delete_statement
    | insert_statement
    ;

// $>

// $<Cursor Manipulation SQL PL/SQL Statements

cursor_manipulation_statements
    : close_statement
    | open_statement
    | fetch_statement
    | open_for_statement
    ;

close_statement
    : CLOSE cursor_name
    ;

open_statement
    : OPEN cursor_name expression_list?
    ;

fetch_statement
    : FETCH cursor_name (it1=INTO variable_name (',' variable_name )* | BULK COLLECT INTO variable_name (',' variable_name )*)
    ;

open_for_statement
    : OPEN variable_name FOR (select_statement | expression) using_clause?
    ;

// $>

// $<Transaction Control SQL PL/SQL Statements

transaction_control_statements
    : set_transaction_command
    | set_constraint_command
    | commit_statement
    | rollback_statement
    | savepoint_statement
    ;

set_transaction_command
    : SET TRANSACTION
      (READ (ONLY | WRITE) | ISOLATION LEVEL (SERIALIZABLE | READ COMMITTED) | USE ROLLBACK SEGMENT rollback_segment_name)?
      (NAME quoted_string)?
    ;

set_constraint_command
    : SET (CONSTRAINT | CONSTRAINTS) (ALL | constraint_name (',' constraint_name)*) (IMMEDIATE | DEFERRED)
    ;

commit_statement
    : COMMIT WORK?
      (COMMENT expression | FORCE (CORRUPT_XID expression| CORRUPT_XID_ALL | expression (',' expression)?))?
      write_clause?
    ;

write_clause
    : WRITE (WAIT|NOWAIT)? (IMMEDIATE|BATCH)?
    ;

rollback_statement
    : ROLLBACK WORK? (TO SAVEPOINT? savepoint_name | FORCE quoted_string)?
    ;

savepoint_statement
    : SAVEPOINT savepoint_name
    ;

// Dml

/* TODO
//SHOULD BE OVERRIDEN!
compilation_unit
    :  seq_of_statements* EOF
    ;

//SHOULD BE OVERRIDEN!
seq_of_statements
    : select_statement
    | update_statement
    | delete_statement
    | insert_statement
    | lock_table_statement
    | merge_statement
    | explain_statement
//    | case_statement[true]
    ;
*/

explain_statement
    : EXPLAIN PLAN (SET STATEMENT_ID '=' quoted_string)? (INTO tableview_name)?
      FOR (select_statement | update_statement | delete_statement | insert_statement | merge_statement)
    ;

select_statement
    : subquery_factoring_clause? subquery (for_update_clause | order_by_clause)*
    ;

// $<Select - Specific Clauses
subquery_factoring_clause
    : WITH factoring_element (',' factoring_element)*
    ;

factoring_element
    : query_name ('(' column_name (',' column_name)* ')')? AS '(' subquery order_by_clause? ')'
      search_clause? cycle_clause?
    ;

search_clause
    : SEARCH (DEPTH | BREADTH) FIRST BY column_name ASC? DESC? (NULLS FIRST)? (NULLS LAST)?
      (',' column_name ASC? DESC? (NULLS FIRST)? (NULLS LAST)?)* SET column_name
    ;

cycle_clause
    : CYCLE column_name (',' column_name)* SET column_name TO expression DEFAULT expression
    ;

subquery
    : subquery_basic_elements subquery_operation_part*
    ;

subquery_operation_part
    : (UNION ALL? | INTERSECT | MINUS) subquery_basic_elements
    ;

subquery_basic_elements
    : query_block
    | '(' subquery ')'
    ;

query_block
    : SELECT (DISTINCT | UNIQUE | ALL)? ('*' | selected_element (',' selected_element)*)
      into_clause? from_clause where_clause? hierarchical_query_clause? group_by_clause? model_clause?
    ;

selected_element
    : select_list_elements column_alias?
    ;

from_clause
    : FROM table_ref_list
    ;

select_list_elements
    : tableview_name '.' '*'
    | expression
    ;

table_ref_list
    : table_ref (',' table_ref)*
    ;

// NOTE to PIVOT clause
// according the SQL reference this should not be possible
// according to he reality it is. Here we probably apply pivot/unpivot onto whole join clause
// eventhough it is not enclosed in parenthesis. See pivot examples 09,10,11
table_ref
    : table_ref_aux join_clause* (pivot_clause | unpivot_clause)?
    ;

table_ref_aux
    : table_ref_aux_internal flashback_query_clause* (/*{isTableAlias()}?*/ table_alias)?
    ;

table_ref_aux_internal
    :  dml_table_expression_clause (pivot_clause | unpivot_clause)?                # table_ref_aux_internal_one
    | '(' table_ref subquery_operation_part* ')' (pivot_clause | unpivot_clause)?  # table_ref_aux_internal_two
    | ONLY '(' dml_table_expression_clause ')'                                     # table_ref_aux_internal_three
    ;

join_clause
    : query_partition_clause? (CROSS | NATURAL)? (INNER | outer_join_type)?
      JOIN table_ref_aux query_partition_clause? (join_on_part | join_using_part)*
    ;

join_on_part
    : ON condition
    ;

join_using_part
    : USING '(' column_name (',' column_name)* ')'
    ;

outer_join_type
    : (FULL | LEFT | RIGHT) OUTER?
    ;

query_partition_clause
    : PARTITION BY ('(' subquery ')' | expression_list | expression (',' expression)*)
    ;

flashback_query_clause
    : VERSIONS BETWEEN (SCN | TIMESTAMP) expression
    | AS OF (SCN | TIMESTAMP | SNAPSHOT) expression
    ;

pivot_clause
    : PIVOT XML? '(' pivot_element (',' pivot_element)* pivot_for_clause pivot_in_clause ')'
    ;

pivot_element
    : aggregate_function_name '(' expression ')' column_alias?
    ;

pivot_for_clause
    : FOR (column_name | '(' column_name (',' column_name)* ')')
    ;

pivot_in_clause
    : IN '(' (subquery | ANY (',' ANY)* | pivot_in_clause_element (',' pivot_in_clause_element)*) ')'
    ;

pivot_in_clause_element
    : pivot_in_clause_elements column_alias?
    ;

pivot_in_clause_elements
    : expression
    | expression_list
    ;

unpivot_clause
    : UNPIVOT ((INCLUDE | EXCLUDE) NULLS)?
    '(' (column_name | '(' column_name (',' column_name)* ')') pivot_for_clause unpivot_in_clause ')'
    ;

unpivot_in_clause
    : IN '(' unpivot_in_elements (',' unpivot_in_elements)* ')'
    ;

unpivot_in_elements
    : (column_name | '(' column_name (',' column_name)* ')')
      (AS (constant | '(' constant (',' constant)* ')'))?
    ;

hierarchical_query_clause
    : CONNECT BY NOCYCLE? condition start_part?
    | start_part CONNECT BY NOCYCLE? condition
    ;

start_part
    : START WITH condition
    ;

group_by_clause
    : GROUP BY group_by_elements (',' group_by_elements)* having_clause?
    | having_clause (GROUP BY group_by_elements (',' group_by_elements)*)?
    ;

group_by_elements
    : grouping_sets_clause
    | rollup_cube_clause
    | expression
    ;

rollup_cube_clause
    : (ROLLUP|CUBE) '(' grouping_sets_elements (',' grouping_sets_elements)* ')'
    ;

grouping_sets_clause
    : GROUPING SETS '(' grouping_sets_elements (',' grouping_sets_elements)* ')'
    ;

grouping_sets_elements
    : rollup_cube_clause
    | expression_list
    | expression
    ;

having_clause
    : HAVING condition
    ;

model_clause
    : MODEL cell_reference_options* return_rows_clause? reference_model* main_model
    ;

cell_reference_options
    : (IGNORE | KEEP) NAV
    | UNIQUE (DIMENSION | SINGLE REFERENCE)
    ;

return_rows_clause
    : RETURN (UPDATED | ALL) ROWS
    ;

reference_model
    : REFERENCE reference_model_name ON '(' subquery ')' model_column_clauses cell_reference_options*
    ;

main_model
    : (MAIN main_model_name)? model_column_clauses cell_reference_options* model_rules_clause
    ;

model_column_clauses
    : model_column_partition_part? DIMENSION BY model_column_list MEASURES model_column_list
    ;

model_column_partition_part
    : PARTITION BY model_column_list
    ;

model_column_list
    : '(' model_column (',' model_column)*  ')'
    ;

model_column
    : (expression | query_block) column_alias?
    ;

model_rules_clause
    : model_rules_part? '(' (model_rules_element (',' model_rules_element)*)? ')'
    ;

model_rules_part
    : RULES (UPDATE | UPSERT ALL?)? ((AUTOMATIC | SEQUENTIAL) ORDER)? model_iterate_clause?
    ;

model_rules_element
    : (UPDATE | UPSERT ALL?)? cell_assignment order_by_clause? '=' expression
    ;

cell_assignment
    : model_expression
    ;

model_iterate_clause
    : ITERATE '(' expression ')' until_part?
    ;

until_part
    : UNTIL '(' condition ')'
    ;

order_by_clause
    : ORDER SIBLINGS? BY order_by_elements (',' order_by_elements)*
    ;

order_by_elements
    : expression (ASC | DESC)? (NULLS (FIRST | LAST))?
    ;

for_update_clause
    : FOR UPDATE for_update_of_part? for_update_options?
    ;

for_update_of_part
    : OF column_name (',' column_name)*
    ;

for_update_options
    : SKIP_ LOCKED
    | NOWAIT
    | WAIT expression
    ;

// $>

update_statement
    : UPDATE general_table_ref update_set_clause where_clause? static_returning_clause? error_logging_clause?
    ;

// $<Update - Specific Clauses
update_set_clause
    : SET
      (column_based_update_set_clause (',' column_based_update_set_clause)* | VALUE '(' identifier ')' '=' expression)
    ;

column_based_update_set_clause
    : column_name '=' expression
    | '(' column_name (',' column_name)* ')' '=' subquery
    ;

// $>

delete_statement
    : DELETE FROM? general_table_ref where_clause? static_returning_clause? error_logging_clause?
    ;

insert_statement
    : INSERT (single_table_insert | multi_table_insert)
    ;

// $<Insert - Specific Clauses

single_table_insert
    : insert_into_clause (values_clause static_returning_clause? | select_statement) error_logging_clause?
    ;

multi_table_insert
    : (ALL multi_table_element+ | conditional_insert_clause) select_statement
    ;

multi_table_element
    : insert_into_clause values_clause? error_logging_clause?
    ;

conditional_insert_clause
    : (ALL | FIRST)? conditional_insert_when_part+ conditional_insert_else_part?
    ;

conditional_insert_when_part
    : WHEN condition THEN multi_table_element+
    ;

conditional_insert_else_part
    : ELSE multi_table_element+
    ;

insert_into_clause
    : INTO general_table_ref ('(' column_name (',' column_name)* ')')?
    ;

values_clause
    : VALUES expression_list
    ;

// $>
merge_statement
    : MERGE INTO tableview_name table_alias? USING selected_tableview ON '(' condition ')'
      (merge_update_clause merge_insert_clause? | merge_insert_clause merge_update_clause?)?
      error_logging_clause?
    ;

// $<Merge - Specific Clauses

merge_update_clause
    : WHEN MATCHED THEN UPDATE SET merge_element (',' merge_element)* where_clause? merge_update_delete_part?
    ;

merge_element
    : column_name '=' expression
    ;

merge_update_delete_part
    : DELETE where_clause
    ;

merge_insert_clause
    : WHEN NOT MATCHED THEN INSERT ('(' column_name (',' column_name)* ')')? VALUES expression_list where_clause?
    ;

selected_tableview
    : (tableview_name | '(' select_statement ')') table_alias?
    ;

// $>

lock_table_statement
    : LOCK TABLE lock_table_element (',' lock_table_element)* IN lock_mode MODE wait_nowait_part?
    ;

wait_nowait_part
    : WAIT expression
    | NOWAIT
    ;

// $<Lock - Specific Clauses

lock_table_element
    : tableview_name partition_extension_clause?
    ;

lock_mode
    : ROW SHARE
    | ROW EXCLUSIVE
    | SHARE UPDATE?
    | SHARE ROW EXCLUSIVE
    | EXCLUSIVE
    ;

// $<Common DDL Clauses

general_table_ref
    : (dml_table_expression_clause | ONLY '(' dml_table_expression_clause ')') table_alias?
    ;

static_returning_clause
    : (RETURNING | RETURN) expression (',' expression)* into_clause
    ;

error_logging_clause
    : LOG ERRORS error_logging_into_part? expression? error_logging_reject_part?
    ;

error_logging_into_part
    : INTO tableview_name
    ;

error_logging_reject_part
    : REJECT LIMIT (UNLIMITED | expression)
    ;

dml_table_expression_clause
    : table_collection_expression
    | '(' select_statement subquery_restriction_clause? ')'
    | tableview_name sample_clause?
    ;

table_collection_expression
    : (TABLE | THE) ('(' subquery ')' | '(' expression ')' ('(' '+' ')')?)
    ;

subquery_restriction_clause
    : WITH (READ ONLY | CHECK OPTION (CONSTRAINT constraint_name)?)
    ;

sample_clause
    : SAMPLE BLOCK? '(' expression (',' expression)? ')' seed_part?
    ;

seed_part
    : SEED '(' expression ')'
    ;

// $>

// $<Expression & Condition
cursor_expression
    : CURSOR '(' subquery ')'
    ;

expression_list
    : '(' expression? (',' expression)* ')'
    ;

condition
    : expression
    ;

expression
    : cursor_expression
    | logical_or_expression
    ;

logical_or_expression
    : logical_and_expression
    | logical_or_expression OR logical_and_expression
    ;

logical_and_expression
    : negated_expression
    | logical_and_expression AND negated_expression
    ;

negated_expression
    : NOT negated_expression
    | equality_expression
    ;

equality_expression
    : multiset_expression (IS NOT?
      (NULL | NAN | PRESENT | INFINITE | A_LETTER SET | EMPTY | OF TYPE? '(' ONLY? type_spec (',' type_spec)* ')'))*
    ;

multiset_expression
    : relational_expression (multiset_type OF? concatenation)?
    ;

multiset_type
    : MEMBER
    | SUBMULTISET
    ;

relational_expression
    : relational_expression relational_operator relational_expression
    | compound_expression
    ;

compound_expression
    : concatenation
      (NOT? (IN in_elements | BETWEEN between_elements | like_type concatenation like_escape_part?))?
    ;
relational_operator
    : '=' | not_equal_op | '<' | '>' | less_than_or_equals_op | greater_than_or_equals_op
    ;
like_type
    : LIKE
    | LIKEC
    | LIKE2
    | LIKE4
    ;

like_escape_part
    : ESCAPE concatenation
    ;

in_elements
    : '(' subquery ')'
    | '(' concatenation (',' concatenation)* ')'
    | constant
    | bind_variable
    | general_element
    ;

between_elements
    : concatenation AND concatenation
    ;

concatenation
    : additive_expression (concatenation_op additive_expression)*
    ;

additive_expression
    : multiply_expression (op+=('+' | '-') multiply_expression)*
    ;

multiply_expression
    : datetime_expression (op+=('*' | '/') datetime_expression)*
    ;

datetime_expression
    : model_expression
      (AT (LOCAL | TIME ZONE concatenation) | interval_expression)?
    ;

interval_expression
    : DAY ('(' concatenation ')')? TO SECOND ('(' concatenation ')')?
    | YEAR ('(' concatenation ')')? TO MONTH
    ;

model_expression
    : unary_expression ('[' model_expression_element ']')?
    ;

model_expression_element
    : (ANY | expression) (',' (ANY | expression))*
    | single_column_for_loop (',' single_column_for_loop)*
    | multi_column_for_loop
    ;

single_column_for_loop
    : FOR column_name
      (IN expression_list | for_like_part? FROM ex1=expression TO ex2=expression for_increment_decrement_type ex3=expression)
    ;

for_like_part
    : LIKE expression
    ;

for_increment_decrement_type
    : INCREMENT
    | DECREMENT
    ;

multi_column_for_loop
    : FOR
      '(' column_name (',' column_name)* ')' IN '(' (subquery | '(' expression_list (',' expression_list)* ')') ')'
    ;

unary_expression
    : ('-' | '+') unary_expression
    | PRIOR unary_expression
    | CONNECT_BY_ROOT unary_expression
    | /*TODO {input.LT(1).getText().equalsIgnoreCase("new") && !input.LT(2).getText().equals(".")}?*/ NEW unary_expression
    |  DISTINCT unary_expression
    |  ALL unary_expression
    |  /*TODO{(input.LA(1) == CASE || input.LA(2) == CASE)}?*/ case_statement/*[false]*/
    |  quantified_expression
    |  standard_function
    |  atom
    ;

case_statement /*TODO [boolean isStatementParameter]
TODO scope    {
    boolean isStatement;
}
@init    {$case_statement::isStatement = $isStatementParameter;}*/
    : searched_case_statement
    | simple_case_statement
    ;

// $<CASE - Specific Clauses

simple_case_statement
    : label_name? ck1=CASE atom simple_case_when_part+  case_else_part? END CASE? label_name?
    ;

simple_case_when_part
    : WHEN expression THEN (/*TODO{$case_statement::isStatement}?*/ seq_of_statements | expression)
    ;

searched_case_statement
    : label_name? ck1=CASE searched_case_when_part+ case_else_part? END CASE? label_name?
    ;

searched_case_when_part
    : WHEN expression THEN (/*TODO{$case_statement::isStatement}?*/ seq_of_statements | expression)
    ;

case_else_part
    : ELSE (/*{$case_statement::isStatement}?*/ seq_of_statements | expression)
    ;
// $>

atom
    : table_element outer_join_sign
    | bind_variable
    | constant
    | general_element
    | '(' (subquery ')' subquery_operation_part* | expression_or_vector ')')
    ;

expression_or_vector
    : expression (vector_expr)?
    ;

vector_expr
    : ',' expression (',' expression)*
    ;

quantified_expression
    : (SOME | EXISTS | ALL | ANY) ('(' subquery ')' | '(' expression ')')
    ;

string_function
    : SUBSTR '(' expression COMMA expression (COMMA expression)? ')'
    | TO_CHAR '(' (table_element|standard_function) (COMMA quoted_string)? ')'
    | DECODE '(' expression (COMMA expression)*  ')'
    | CHR '(' concatenation USING NCHAR_CS ')'
    | NVL '(' expression COMMA expression ')'
    | TRIM '(' ((LEADING | TRAILING | BOTH)? quoted_string? FROM)? concatenation ')'
    ;

standard_function
    : string_function
    | numeric_function_wrapper
    | other_function
    ;

numeric_function_wrapper
    : numeric_function (single_column_for_loop | multi_column_for_loop)?
    ;

numeric_function
   : SUM '(' (DISTINCT|ALL)? expression ')'
   | COUNT '(' ( '*' | ((DISTINCT | UNIQUE | ALL)? concatenation)? ) ')' over_clause?
   | ROUND '(' expression (COMMA UNSIGNED_INTEGER)?  ')'
   | AVG '(' (DISTINCT | ALL)? expression ')'
   | MAX '(' (DISTINCT | ALL)? expression ')'
   ;

other_function
    : over_clause_keyword function_argument_analytic over_clause?
    | /*TODO stantard_function_enabling_using*/ regular_id function_argument_modeling using_clause?
    | COUNT '(' ( '*' | (DISTINCT | UNIQUE | ALL)? concatenation) ')' over_clause?
    | (CAST | XMLCAST) '(' (MULTISET '(' subquery ')' | concatenation) AS type_spec ')'
    | COALESCE '(' table_element (COMMA (numeric|quoted_string))? ')'
    | COLLECT '(' (DISTINCT | UNIQUE)? concatenation collect_order_by_part? ')'
    | within_or_over_clause_keyword function_argument within_or_over_part+
    | cursor_name ( PERCENT_ISOPEN | PERCENT_FOUND | PERCENT_NOTFOUND | PERCENT_ROWCOUNT )
    | DECOMPOSE '(' concatenation (CANONICAL | COMPATIBILITY)? ')'
    | EXTRACT '(' regular_id FROM concatenation ')'
    | (FIRST_VALUE | LAST_VALUE) function_argument_analytic respect_or_ignore_nulls? over_clause
    | standard_prediction_function_keyword
      '(' expression (',' expression)* cost_matrix_clause? using_clause? ')'
    | TRANSLATE '(' expression (USING (CHAR_CS | NCHAR_CS))? (',' expression)* ')'
    | TREAT '(' expression AS REF? type_spec ')'
    | TRIM '(' ((LEADING | TRAILING | BOTH)? quoted_string? FROM)? concatenation ')'
    | XMLAGG '(' expression order_by_clause? ')' ('.' general_element_part)?
    | (XMLCOLATTVAL|XMLFOREST)
      '(' xml_multiuse_expression_element (',' xml_multiuse_expression_element)* ')' ('.' general_element_part)?
    | XMLELEMENT
      '(' (ENTITYESCAPING | NOENTITYESCAPING)? (NAME | EVALNAME)? expression
       (/*TODO{input.LT(2).getText().equalsIgnoreCase("xmlattributes")}?*/ ',' xml_attributes_clause)?
       (',' expression column_alias?)* ')' ('.' general_element_part)?
    | XMLEXISTS '(' expression xml_passing_clause? ')'
    | XMLPARSE '(' (DOCUMENT | CONTENT) concatenation WELLFORMED? ')' ('.' general_element_part)?
    | XMLPI
      '(' (NAME identifier | EVALNAME concatenation) (',' concatenation)? ')' ('.' general_element_part)?
    | XMLQUERY
      '(' concatenation xml_passing_clause? RETURNING CONTENT (NULL ON EMPTY)? ')' ('.' general_element_part)?
    | XMLROOT
      '(' concatenation (',' xmlroot_param_version_part)? (',' xmlroot_param_standalone_part)? ')' ('.' general_element_part)?
    | XMLSERIALIZE
      '(' (DOCUMENT | CONTENT) concatenation (AS type_spec)?
      xmlserialize_param_enconding_part? xmlserialize_param_version_part? xmlserialize_param_ident_part? ((HIDE | SHOW) DEFAULTS)? ')'
      ('.' general_element_part)?
    | XMLTABLE
      '(' xml_namespaces_clause? concatenation xml_passing_clause? (COLUMNS xml_table_column (',' xml_table_column))? ')' ('.' general_element_part)?
    ;

over_clause_keyword
    : AVG
    | CORR
    | LAG
    | LEAD
    | MAX
    | MEDIAN
    | MIN
    | NTILE
    | RATIO_TO_REPORT
    | ROW_NUMBER
    | SUM
    | VARIANCE
    | REGR_
    | STDDEV
    | VAR_
    | COVAR_
    ;

within_or_over_clause_keyword
    : CUME_DIST
    | DENSE_RANK
    | LISTAGG
    | PERCENT_RANK
    | PERCENTILE_CONT
    | PERCENTILE_DISC
    | RANK
    ;

standard_prediction_function_keyword
    : PREDICTION
    | PREDICTION_BOUNDS
    | PREDICTION_COST
    | PREDICTION_DETAILS
    | PREDICTION_PROBABILITY
    | PREDICTION_SET
    ;

over_clause
    : OVER '(' query_partition_clause? (order_by_clause windowing_clause?)? ')'
    ;

windowing_clause
    : windowing_type
      (BETWEEN windowing_elements AND windowing_elements | windowing_elements)
    ;

windowing_type
    : ROWS
    | RANGE
    ;

windowing_elements
    : UNBOUNDED PRECEDING
    | CURRENT ROW
    | concatenation (PRECEDING|FOLLOWING)
    ;

using_clause
    : USING ('*' | using_element (',' using_element)*)
    ;

using_element
    : (IN OUT? | OUT)? select_list_elements column_alias?
    ;

collect_order_by_part
    : ORDER BY concatenation
    ;

within_or_over_part
    : WITHIN GROUP '(' order_by_clause ')'
    | over_clause
    ;

cost_matrix_clause
    : COST (MODEL AUTO? | '(' cost_class_name (',' cost_class_name)* ')' VALUES expression_list)
    ;

xml_passing_clause
    : PASSING (BY VALUE)? expression column_alias? (',' expression column_alias?)
    ;

xml_attributes_clause
    : XMLATTRIBUTES
     '(' (ENTITYESCAPING | NOENTITYESCAPING)? (SCHEMACHECK | NOSCHEMACHECK)?
     xml_multiuse_expression_element (',' xml_multiuse_expression_element)* ')'
    ;

xml_namespaces_clause
    : XMLNAMESPACES
      '(' (concatenation column_alias)? (',' concatenation column_alias)*
      xml_general_default_part? ')'
    ;

xml_table_column
    : xml_column_name
      (FOR ORDINALITY | type_spec (PATH concatenation)? xml_general_default_part?)
    ;

xml_general_default_part
    : DEFAULT concatenation
    ;

xml_multiuse_expression_element
    : expression (AS (id_expression | EVALNAME concatenation))?
    ;

xmlroot_param_version_part
    : VERSION (NO VALUE | expression)
    ;

xmlroot_param_standalone_part
    : STANDALONE (YES | NO VALUE?)
    ;

xmlserialize_param_enconding_part
    : ENCODING concatenation
    ;

xmlserialize_param_version_part
    : VERSION concatenation
    ;

xmlserialize_param_ident_part
    : NO INDENT
    | INDENT (SIZE '=' concatenation)?
    ;

// SqlPlus

sql_plus_command
    : ('/' | whenever_command | exit_command | prompt_command | set_command | show_errors_command | start_command) ';'?
    ;

whenever_command
    : WHENEVER (SQLERROR | OSERROR)
      (EXIT (SUCCESS | FAILURE | WARNING) (COMMIT | ROLLBACK) | CONTINUE (COMMIT|ROLLBACK|NONE))
    ;

set_command
    : SET regular_id (CHAR_STRING | ON | OFF | /*EXACT_NUM_LIT*/numeric | regular_id) // TODO
    ;

exit_command
    : EXIT
    ;

prompt_command
    : PROMPT
    ;

show_errors_command
    : SHOW ERR
    | SHOW ERRORS
    ;

start_command
    : START_CMD
    ;

// Common

partition_extension_clause
    : (SUBPARTITION | PARTITION) FOR? expression_list
    ;

column_alias
    : AS? (identifier | alias_quoted_string)
    | AS
    ;

table_alias
    : (identifier | alias_quoted_string)
    ;

alias_quoted_string
    : quoted_string
    ;

where_clause
    : WHERE (current_of_clause | expression)
    ;

current_of_clause
    : CURRENT OF cursor_name
    ;

into_clause
    : INTO variable_name (',' variable_name)*
    | BULK COLLECT INTO variable_name (',' variable_name)*
    ;

// $>

// $<Common PL/SQL Named Elements

xml_column_name
    : identifier
    | quoted_string
    ;

cost_class_name
    : identifier
    ;

attribute_name
    : identifier
    ;

savepoint_name
    : identifier
    ;

rollback_segment_name
    : identifier
    ;

table_var_name
    : identifier
    ;

schema_name
    : identifier
    ;

routine_name
    : identifier ('.' id_expression)* ('@' link_name)?
    ;

package_name
    : identifier
    ;

implementation_type_name
    : identifier ('.' id_expression)?
    ;

parameter_name
    : identifier
    ;

reference_model_name
    : identifier
    ;

main_model_name
    : identifier
    ;

aggregate_function_name
    : identifier ('.' id_expression)*
    ;

query_name
    : identifier
    ;

constraint_name
    : identifier ('.' id_expression)* ('@' link_name)?
    ;

label_name
    : id_expression
    ;

type_name
    : id_expression ('.' id_expression)*
    ;

sequence_name
    : id_expression ('.' id_expression)*
    ;

exception_name
    : identifier ('.' id_expression)*
    ;

view_name
    : identifier ('.' id_expression)?
    ;

mview_name
    : identifier ('.' id_expression)?
    ;


dblink_name
    : identifier ('.' id_expression)?
    ;

function_name
    : identifier ('.' id_expression)?
    ;

procedure_name
    : identifier ('.' id_expression)?
    ;

trigger_name
    : identifier ('.' id_expression)?
    ;

variable_name
    : (INTRODUCER char_set_name)? id_expression ('.' id_expression)?
    | bind_variable
    ;

index_name
    : identifier
    ;

cursor_name
    : identifier
    | bind_variable
    ;

record_name
    : identifier
    | bind_variable
    ;

collection_name
    : identifier ('.' id_expression)?
    ;

link_name
    : identifier
    ;

column_name
    : identifier ('.' id_expression)*
    ;

tableview_name
    : identifier ('.' id_expression)?
      ('@' link_name | /*TODO{!(input.LA(2) == BY)}?*/ partition_extension_clause)?
    ;

char_set_name
    : id_expression ('.' id_expression)*
    ;

synonym_name
    : identifier
    ;

// Represents a valid DB object name in DDL commands which are valid for several DB (or schema) objects.
// For instance, create synonym ... for <DB object name>, or rename <old DB object name> to <new DB object name>.
// Both are valid for seuqences, tables, views etc.
schema_object_name
    : id_expression
    ;

// $>

// $<Common PL/SQL Specs

// NOTE: In reality this applies to aggregate functions only
keep_clause
    : KEEP '(' DENSE_RANK (FIRST | LAST) order_by_clause ')' over_clause?
    ;

function_argument
    : '(' argument? (',' argument )* ')' keep_clause?
    ;

function_argument_analytic
    : '(' (argument respect_or_ignore_nulls?)? (',' argument respect_or_ignore_nulls?)* ')' keep_clause?
    ;

function_argument_modeling
    : '(' column_name (',' (numeric | NULL) (',' (numeric | NULL))?)?
      USING (tableview_name '.' '*' | '*' | expression column_alias? (',' expression column_alias?)*)
      ')' keep_clause?
    ;

respect_or_ignore_nulls
    : (RESPECT | IGNORE) NULLS
    ;

argument
    : (identifier '=' '>')? expression
    ;

type_spec
    : datatype
    | REF? type_name (PERCENT_ROWTYPE | PERCENT_TYPE)?
    ;

datatype
    : native_datatype_element precision_part? (WITH LOCAL? TIME ZONE | CHARACTER SET char_set_name | DEFAULT ',')?
    | INTERVAL (YEAR | DAY) ('(' expression ')')? TO (MONTH | SECOND) ('(' expression ')')?
    ;

precision_part
    : '(' numeric (',' numeric)? (CHAR | BYTE)? ')'
    ;

native_datatype_element
    : BINARY_INTEGER
    | PLS_INTEGER
    | SIGNTYPE
    | SIMPLE_INTEGER
    | NVARCHAR2
    | DEC
    | INTEGER
    | INT
    | NUMERIC
    | SMALLINT
    | NUMBER
    | DECIMAL
    | DOUBLE PRECISION?
    | FLOAT
    | REAL
    | CHAR
    | CHARACTER
    | VARCHAR2
    | VARCHAR
    | STRING
    | RAW
    | BOOLEAN
    | DATE
    | ROWID
    | YEAR
    | MONTH
    | DAY
    | HOUR
    | MINUTE
    | TIMESTAMP
    | BLOB
    | CLOB
    ;

bind_variable
    : (BINDVAR | ':' UNSIGNED_INTEGER)
      // Pro*C/C++ indicator variables
      (INDICATOR? (BINDVAR | ':' UNSIGNED_INTEGER))?
      ('.' general_element_part)*
    ;

general_element
    : general_element_part ('.' general_element_part)*
    ;

general_element_part
    : (INTRODUCER char_set_name)? id_expression ('.' id_expression)* function_argument?
    ;

table_element
    : (INTRODUCER char_set_name)? id_expression ('.' id_expression)*
    ;

// $>

// $<Lexer Mappings

constant
    : TIMESTAMP (quoted_string | bind_variable) (AT TIME ZONE quoted_string)?
    | INTERVAL (quoted_string | bind_variable | general_element_part)
      (DAY | HOUR | MINUTE | SECOND)
      ('(' (UNSIGNED_INTEGER | bind_variable) (',' (UNSIGNED_INTEGER | bind_variable) )? ')')?
      (TO ( DAY | HOUR | MINUTE | SECOND ('(' (UNSIGNED_INTEGER | bind_variable) ')')?))?
    | numeric
    | DATE quoted_string
    | quoted_string
    | NULL
    | TRUE
    | FALSE
    | DBTIMEZONE
    | SESSIONTIMEZONE
    | MINVALUE
    | MAXVALUE
    | DEFAULT
    ;

numeric
    : UNSIGNED_INTEGER
    | APPROXIMATE_NUM_LIT
    ;

numeric_negative
    : MINUS_SIGN numeric
    ;

quoted_string
    : CHAR_STRING
    //| CHAR_STRING_PERL
    | NATIONAL_CHAR_STRING_LIT
    ;

identifier
    : (INTRODUCER char_set_name)? id_expression
    ;

id_expression
    : regular_id
    | DELIMITED_ID
    ;

not_equal_op
    : NOT_EQUAL_OP
    | '<' '>'
    | '!' '='
    | '^' '='
    ;

greater_than_or_equals_op
    : '>='
    | '>' '='
    ;

less_than_or_equals_op
    : '<='
    | '<' '='
    ;

concatenation_op
    : '||'
    | '|' '|'
    ;

outer_join_sign
    : '(' '+' ')'
    ;

regular_id
    : REGULAR_ID
    | A_LETTER
    | ADD
    | AFTER
    | AGENT
    | AGGREGATE
    //| ALL
    //| ALTER
    | ANALYZE
    //| AND
    //| ANY
    | ARRAY
    // | AS
    //| ASC
    | ASSOCIATE
    | AT
    | ATTRIBUTE
    | AUDIT
    | AUTHID
    | AUTO
    | AUTOMATIC
    | AUTONOMOUS_TRANSACTION
    | BATCH
    | BEFORE
    | BINARY_INTEGER
    | BLOB
    | BLOCK
    | BODY
    | BOOLEAN
    | BOTH
    | BULK
    | BYTE
    | C_LETTER
    // | CACHE
    | CALL
    | CANONICAL
    | CASCADE
    //| CASE
    | CAST
    | CHAR
    | CHAR_CS
    | CHARACTER
    //| CHECK
    | CHR
    | CLOB
    | CLOSE
    | CLUSTER
    | COLLECT
    | COLUMNS
    | COMMENT
    | COMMIT
    | COMMITTED
    | COMPATIBILITY
    | COMPILE
    | COMPOUND
    //| CONNECT
    //| CONNECT_BY_ROOT
    | CONSTANT
    | CONSTRAINT
    | CONSTRAINTS
    | CONSTRUCTOR
    | CONTENT
    | CONTEXT
    | CONTINUE
    | CONVERT
    | CORRUPT_XID
    | CORRUPT_XID_ALL
    | COST
    | COUNT
    //| CREATE
    | CROSS
    | CUBE
    //| CURRENT
    | CURRENT_USER
    | CURSOR
    | CUSTOMDATUM
    | CYCLE
    | DATA
    | DATABASE
    //| DATE
    | DAY
    | DB_ROLE_CHANGE
    | DBTIMEZONE
    | DDL
    | DEBUG
    | DEC
    | DECIMAL
    //| DECLARE
    | DECOMPOSE
    | DECREMENT
    //| DEFAULT
    | DEFAULTS
    | DEFERRED
    | DEFINER
    // | DELETE
    // | DEPTH
    //| DESC
    | DETERMINISTIC
    | DIMENSION
    | DISABLE
    | DISASSOCIATE
    //| DISTINCT
    | DOCUMENT
    | DOUBLE
    //| DROP
    | DSINTERVAL_UNCONSTRAINED
    | EACH
    | ELEMENT
    //| ELSE
    //| ELSIF
    | EMPTY
    | ENABLE
    | ENCODING
    //| END
    | ENTITYESCAPING
    | ERR
    | ERRORS
    | ESCAPE
    | EVALNAME
    | EXCEPTION
    | EXCEPTION_INIT
    | EXCEPTIONS
    | EXCLUDE
    //| EXCLUSIVE
    | EXECUTE
    //| EXISTS
    | EXIT
    | EXPLAIN
    | EXTERNAL
    | EXTRACT
    | FAILURE
    //| FALSE
    //| FETCH
    | FINAL
    | FIRST
    | FIRST_VALUE
    | FLOAT
    | FOLLOWING
    | FOLLOWS
    //| FOR
    | FORALL
    | FORCE
    // | FROM
    | FULL
    | FUNCTION
    //| GOTO
    //| GRANT
    //| GROUP
    | GROUPING
    | HASH
    //| HAVING
    | HIDE
    | HOUR
    //| IF
    | IGNORE
    | IMMEDIATE
    // | IN
    | INCLUDE
    | INCLUDING
    | INCREMENT
    | INDENT
    //| INDEX
    | INDEXED
    | INDICATOR
    | INDICES
    | INFINITE
    | INLINE
    | INNER
    | INOUT
    //| INSERT
    | INSTANTIABLE
    | INSTEAD
    | INT
    | INTEGER
    //| INTERSECT
    | INTERVAL
    // | INTO
    | INVALIDATE
    //| IS
    | ISOLATION
    | ITERATE
    | JAVA
    | JOIN
    | KEEP
    | LANGUAGE
    | LAST
    | LAST_VALUE
    | LEADING
    | LEFT
    | LEVEL
    | LIBRARY
    // | LIKE
    | LIKE2
    | LIKE4
    | LIKEC
    | LIMIT
    | LOCAL
    //| LOCK
    | LOCKED
    | LOG
    | LOGOFF
    | LOGON
    | LONG
    | LOOP
    | MAIN
    | MAP
    | MATCHED
    | MAXVALUE
    | MEASURES
    | MEMBER
    | MERGE
    //| MINUS
    | MINUTE
    | MINVALUE
    | MLSLABEL
    //| MODE
    | MODEL
    | MODIFY
    | MONTH
    | MULTISET
    | NAME
    | NAN
    | NATURAL
    | NATURALN
    | NAV
    | NCHAR
    | NCHAR_CS
    | NCLOB
    | NESTED
    | NEW
    | NO
    | NOAUDIT
    // | NOCACHE
    | NOCOPY
    | NOCYCLE
    | NOENTITYESCAPING
    //| NOMAXVALUE
    //| NOMINVALUE
    | NONE
    // | NOORDER
    | NOSCHEMACHECK
    //| NOT
    //| NOWAIT
    // | NULL
    | NULLS
    | NUMBER
    | NUMERIC
    | NVARCHAR2
    | OBJECT
    //| OF
    | OFF
    | OID
    | OLD
    //| ON
    | ONLY
    | OPEN
    //| OPTION
    //| OR
    | ORADATA
    //| ORDER
    | ORDINALITY
    | OSERROR
    | OUT
    | OUTER
    | OVER
    | OVERRIDING
    | PACKAGE
    | PARALLEL_ENABLE
    | PARAMETERS
    | PARENT
    | PARTITION
    | PASSING
    | PATH
    //| PERCENT_ROWTYPE
    //| PERCENT_TYPE
    | PIPELINED
    //| PIVOT
    | PLAN
    | PLS_INTEGER
    | POSITIVE
    | POSITIVEN
    | PRAGMA
    | PRECEDING
    | PRECISION
    | PRESENT
    //| PRIOR
    //| PROCEDURE
    | RAISE
    | RANGE
    | RAW
    | READ
    | REAL
    | RECORD
    | REF
    | REFERENCE
    | REFERENCING
    | REJECT
    | RENAME
    | REPLACE
    | RESPECT
    | RESTRICT_REFERENCES
    | RESULT
    | RETURN
    | RETURNING
    | REUSE
    | REVERSE
    //| REVOKE
    | RIGHT
    | ROLLBACK
    | ROLLUP
    | ROW
    | ROWID
    | ROWS
    | RULES
    | SAMPLE
    | SAVE
    | SAVEPOINT
    | SCHEMA
    | SCHEMACHECK
    | SCN
    // | SEARCH
    | SECOND
    | SEED
    | SEGMENT
    // | SELECT
    | SELF
    // | SEQUENCE
    | SEQUENTIAL
    | SERIALIZABLE
    | SERIALLY_REUSABLE
    | SERVERERROR
    | SESSIONTIMEZONE
    | SET
    | SETS
    | SETTINGS
    //| SHARE
    | SHOW
    | SHUTDOWN
    | SIBLINGS
    | SIGNTYPE
    | SIMPLE_INTEGER
    | SINGLE
    //| SIZE
    | SKIP_
    | SMALLINT
    | SNAPSHOT
    | SOME
    | SPECIFICATION
    | SQLDATA
    | SQLERROR
    | STANDALONE
    //| START
    | STARTUP
    | STATEMENT
    | STATEMENT_ID
    | STATIC
    | STATISTICS
    | STRING
    | SUBMULTISET
    | SUBPARTITION
    | SUBSTITUTABLE
    | SUBTYPE
    | SUCCESS
    | SUSPEND
    //| TABLE
    //| THE
    //| THEN
    | TIME
    | TIMESTAMP
    | TIMESTAMP_LTZ_UNCONSTRAINED
    | TIMESTAMP_TZ_UNCONSTRAINED
    | TIMESTAMP_UNCONSTRAINED
    | TIMEZONE_ABBR
    | TIMEZONE_HOUR
    | TIMEZONE_MINUTE
    | TIMEZONE_REGION
    //| TO
    | TRAILING
    | TRANSACTION
    | TRANSLATE
    | TREAT
    | TRIGGER
    | TRIM
    //| TRUE
    | TRUNCATE
    | TYPE
    | UNBOUNDED
    | UNDER
    //| UNION
    //| UNIQUE
    | UNLIMITED
    //| UNPIVOT
    | UNTIL
    //| UPDATE
    | UPDATED
    | UPSERT
    | UROWID
    | USE
    //| USING
    | VALIDATE
    | VALUE
    //| VALUES
  //  | VARCHAR
 //   | VARCHAR2
    | VARIABLE
    | VARRAY
    | VARYING
    | VERSION
    | VERSIONS
    | WAIT
    | WARNING
    | WELLFORMED
    // | WHEN
    | WHENEVER
    // | WHERE
    | WHILE
    //| WITH
    | WITHIN
    | WORK
    | WRITE
    | XML
    | XMLAGG
    | XMLATTRIBUTES
    | XMLCAST
    | XMLCOLATTVAL
    | XMLELEMENT
    | XMLEXISTS
    | XMLFOREST
    | XMLNAMESPACES
    | XMLPARSE
    | XMLPI
    | XMLQUERY
    | XMLROOT
    | XMLSERIALIZE
    | XMLTABLE
    | YEAR
    | YES
    | YMINTERVAL_UNCONSTRAINED
    | ZONE
    | PREDICTION
    | PREDICTION_BOUNDS
    | PREDICTION_COST
    | PREDICTION_DETAILS
    | PREDICTION_PROBABILITY
    | PREDICTION_SET
    | CUME_DIST
    | DENSE_RANK
    | LISTAGG
    | PERCENT_RANK
    | PERCENTILE_CONT
    | PERCENTILE_DISC
    | RANK
    | AVG
    | CORR
    | LAG
    | LEAD
    | MAX
    | MEDIAN
    | MIN
    | NTILE
    | RATIO_TO_REPORT
    | ROW_NUMBER
    | SUM
    | VARIANCE
    | REGR_
    | STDDEV
    | VAR_
    | COVAR_
    | DBMS_ALERT
    |DBMS_AQ
    |DBMS_AQADM
    |DBMS_CRYPTO
    |DBMS_JOB
    |DBMS_LOB
    |DBMS_LOCK
    |DBMS_MVIEW
    |DBMS_OUTPUT
    |DBMS_PIPE
    |DBMS_PROFILER
    |DBMS_RANDOM
    |DBMS_RLS
    |DBMS_SCHEDULER
    |DBMS_SESSION
    |DBMS_SQL
    |DBMS_UTILITY
    |EMP_ADMIN
    |UTL_ENCODE
    |UTL_FILE
    |UTL_HTTP
    |UTL_MAIL
    |UTL_RAW
    |UTL_SMTP
    |UTL_TCP
    |UTL_URL
    ;

string_function_name
    : CHR
    | DECODE
    | SUBSTR
    | TO_CHAR
    | TRIM
    ;

numeric_function_name
    : AVG
    | COUNT
    | NVL
    | ROUND
    | SUM
    ;

supported_packages
    :DBMS_ALERT
    |DBMS_AQ
    |DBMS_AQADM
    |DBMS_CRYPTO
    |DBMS_JOB
    |DBMS_LOB
    |DBMS_LOCK
    |DBMS_MVIEW
    |DBMS_OUTPUT
    |DBMS_PIPE
    |DBMS_PROFILER
    |DBMS_RANDOM
    |DBMS_RLS
    |DBMS_SCHEDULER
    |DBMS_SESSION
    |DBMS_SQL
    |DBMS_UTILITY
    |EMP_ADMIN
    |UTL_ENCODE
    |UTL_FILE
    |UTL_HTTP
    |UTL_MAIL
    |UTL_RAW
    |UTL_SMTP
    |UTL_TCP
    |UTL_URL
    ;

/* Lexer Rules */
/*-------------*/

A_LETTER:                     'A';
ADD:                          'ADD';
AFTER:                        'AFTER';
AGENT:                        'AGENT';
AGGREGATE:                    'AGGREGATE';
ALL:                          'ALL';
ALTER:                        'ALTER';
ANALYZE:                      'ANALYZE';
AND:                          'AND';
ANY:                          'ANY';
ARRAY:                        'ARRAY';
AS:                           'AS';
ASC:                          'ASC';
ASSOCIATE:                    'ASSOCIATE';
AT:                           'AT';
ATTRIBUTE:                    'ATTRIBUTE';
AUDIT:                        'AUDIT';
AUTHID:                       'AUTHID';
AUTO:                         'AUTO';
AUTOMATIC:                    'AUTOMATIC';
AUTONOMOUS_TRANSACTION:       'AUTONOMOUS_TRANSACTION';
BATCH:                        'BATCH';
BEFORE:                       'BEFORE';
BEGIN:                        'BEGIN';
BETWEEN:                      'BETWEEN';
BFILE:                        'BFILE';
BINARY_DOUBLE:                'BINARY_DOUBLE';
BINARY_FLOAT:                 'BINARY_FLOAT';
BINARY_INTEGER:               'BINARY_INTEGER';
BLOB:                         'BLOB';
BLOCK:                        'BLOCK';
BODY:                         'BODY';
BOOLEAN:                      'BOOLEAN';
BOTH:                         'BOTH';
BREADTH:                      'BREADTH';
BULK:                         'BULK';
BY:                           'BY';
BYTE:                         'BYTE';
C_LETTER:                     'C';
CACHE:                        'CACHE';
CALL:                         'CALL';
CANONICAL:                    'CANONICAL';
CASCADE:                      'CASCADE';
CASE:                         'CASE';
CAST:                         'CAST';
CHAR:                         'CHAR';
CHAR_CS:                      'CHAR_CS';
CHARACTER:                    'CHARACTER';
CHECK:                        'CHECK';
CHR:                          'CHR';
CLOB:                         'CLOB';
CLOSE:                        'CLOSE';
CLUSTER:                      'CLUSTER';
COALESCE:                     'COALESCE';
COLLECT:                      'COLLECT';
COLUMN:                       'COLUMN';
COLUMNS:                      'COLUMNS';
COMMENT:                      'COMMENT';
COMMIT:                       'COMMIT';
COMMITTED:                    'COMMITTED';
COMPATIBILITY:                'COMPATIBILITY';
COMPILE:                      'COMPILE';
COMPOUND:                     'COMPOUND';
CONNECT:                      'CONNECT';
CONNECT_BY_ROOT:              'CONNECT_BY_ROOT';
CONSTANT:                     'CONSTANT';
CONSTRAINT:                   'CONSTRAINT';
CONSTRAINTS:                  'CONSTRAINTS';
CONSTRUCTOR:                  'CONSTRUCTOR';
CONTENT:                      'CONTENT';
CONTEXT:                      'CONTEXT';
CONTINUE:                     'CONTINUE';
CONVERT:                      'CONVERT';
CORRUPT_XID:                  'CORRUPT_XID';
CORRUPT_XID_ALL:              'CORRUPT_XID_ALL';
COST:                         'COST';
COUNT:                        'COUNT';
CREATE:                       'CREATE';
CROSS:                        'CROSS';
CUBE:                         'CUBE';
CURRENT:                      'CURRENT';
CURRENT_USER:                 'CURRENT_USER';
CURSOR:                       'CURSOR';
CUSTOMDATUM:                  'CUSTOMDATUM';
CYCLE:                        'CYCLE';
DATA:                         'DATA';
DATABASE:                     'DATABASE';
DATE:                         'DATE';
DAY:                          'DAY';
DB_ROLE_CHANGE:               'DB_ROLE_CHANGE';
DBTIMEZONE:                   'DBTIMEZONE';
DDL:                          'DDL';
DEBUG:                        'DEBUG';
DEC:                          'DEC';
DECIMAL:                      'DECIMAL';
DECLARE:                      'DECLARE';
DECOMPOSE:                    'DECOMPOSE';
DECREMENT:                    'DECREMENT';
DEFAULT:                      'DEFAULT';
DEFAULTS:                     'DEFAULTS';
DEFERRED:                     'DEFERRED';
DEFINER:                      'DEFINER';
DELETE:                       'DELETE';
DEPTH:                        'DEPTH';
DESC:                         'DESC';
DETERMINISTIC:                'DETERMINISTIC';
DIMENSION:                    'DIMENSION';
DISABLE:                      'DISABLE';
DISASSOCIATE:                 'DISASSOCIATE';
DISTINCT:                     'DISTINCT';
DOCUMENT:                     'DOCUMENT';
DOUBLE:                       'DOUBLE';
DROP:                         'DROP';
DSINTERVAL_UNCONSTRAINED:     'DSINTERVAL_UNCONSTRAINED';
EACH:                         'EACH';
ELEMENT:                      'ELEMENT';
ELSE:                         'ELSE';
ELSIF:                        'ELSIF';
EMPTY:                        'EMPTY';
ENABLE:                       'ENABLE';
ENCODING:                     'ENCODING';
END:                          'END';
ENTITYESCAPING:               'ENTITYESCAPING';
ERR:                          'ERR';
ERRORS:                       'ERRORS';
ESCAPE:                       'ESCAPE';
EVALNAME:                     'EVALNAME';
EXCEPTION:                    'EXCEPTION';
EXCEPTION_INIT:               'EXCEPTION_INIT';
EXCEPTIONS:                   'EXCEPTIONS';
EXCLUDE:                      'EXCLUDE';
EXCLUSIVE:                    'EXCLUSIVE';
EXECUTE:                      'EXECUTE';
EXISTS:                       'EXISTS';
EXIT:                         'EXIT';
EXPLAIN:                      'EXPLAIN';
EXTERNAL:                     'EXTERNAL';
EXTRACT:                      'EXTRACT';
FAILURE:                      'FAILURE';
FALSE:                        'FALSE';
FETCH:                        'FETCH';
FINAL:                        'FINAL';
FIRST:                        'FIRST';
FIRST_VALUE:                  'FIRST_VALUE';
FLOAT:                        'FLOAT';
FOLLOWING:                    'FOLLOWING';
FOLLOWS:                      'FOLLOWS';
FOR:                          'FOR';
FORALL:                       'FORALL';
FORCE:                        'FORCE';
FROM:                         'FROM';
FULL:                         'FULL';
FUNCTION:                     'FUNCTION';
GOTO:                         'GOTO';
GRANT:                        'GRANT';
GROUP:                        'GROUP';
GROUPING:                     'GROUPING';
HASH:                         'HASH';
HAVING:                       'HAVING';
HIDE:                         'HIDE';
HOUR:                         'HOUR';
IF:                           'IF';
IGNORE:                       'IGNORE';
IMMEDIATE:                    'IMMEDIATE';
IN:                           'IN';
INCLUDE:                      'INCLUDE';
INCLUDING:                    'INCLUDING';
INCREMENT:                    'INCREMENT';
INDENT:                       'INDENT';
INDEX:                        'INDEX';
INDEXED:                      'INDEXED';
INDICATOR:                    'INDICATOR';
INDICES:                      'INDICES';
INFINITE:                     'INFINITE';
INLINE:                       'INLINE';
INNER:                        'INNER';
INOUT:                        'INOUT';
INSERT:                       'INSERT';
INSTANTIABLE:                 'INSTANTIABLE';
INSTEAD:                      'INSTEAD';
INT:                          'INT';
INTEGER:                      'INTEGER';
INTERSECT:                    'INTERSECT';
INTERVAL:                     'INTERVAL';
INTO:                         'INTO';
INVALIDATE:                   'INVALIDATE';
IS:                           'IS';
ISOLATION:                    'ISOLATION';
ITERATE:                      'ITERATE';
JAVA:                         'JAVA';
JOIN:                         'JOIN';
KEEP:                         'KEEP';
LANGUAGE:                     'LANGUAGE';
LAST:                         'LAST';
LAST_VALUE:                   'LAST_VALUE';
LEADING:                      'LEADING';
LEFT:                         'LEFT';
LEVEL:                        'LEVEL';
LIBRARY:                      'LIBRARY';
LIKE:                         'LIKE';
LIKE2:                        'LIKE2';
LIKE4:                        'LIKE4';
LIKEC:                        'LIKEC';
LIMIT:                        'LIMIT';
LOCAL:                        'LOCAL';
LOCK:                         'LOCK';
LOCKED:                       'LOCKED';
LOG:                          'LOG';
LOGOFF:                       'LOGOFF';
LOGON:                        'LOGON';
LONG:                         'LONG';
LOOP:                         'LOOP';
MAIN:                         'MAIN';
MAP:                          'MAP';
MATCHED:                      'MATCHED';
MAXVALUE:                     'MAXVALUE';
MEASURES:                     'MEASURES';
MEMBER:                       'MEMBER';
MERGE:                        'MERGE';
MINUS:                        'MINUS';
MINUTE:                       'MINUTE';
MINVALUE:                     'MINVALUE';
MLSLABEL:                     'MLSLABEL';
MODE:                         'MODE';
MODEL:                        'MODEL';
MODIFY:                       'MODIFY';
MONTH:                        'MONTH';
MULTISET:                     'MULTISET';
NAME:                         'NAME';
NAN:                          'NAN';
NATURAL:                      'NATURAL';
NATURALN:                     'NATURALN';
NAV:                          'NAV';
NCHAR:                        'NCHAR';
NCHAR_CS:                     'NCHAR_CS';
NCLOB:                        'NCLOB';
NESTED:                       'NESTED';
NEW:                          'NEW';
NO:                           'NO';
NOAUDIT:                      'NOAUDIT';
NOCACHE:                      'NOCACHE';
NOCOPY:                       'NOCOPY';
NOCYCLE:                      'NOCYCLE';
NOENTITYESCAPING:             'NOENTITYESCAPING';
NOMAXVALUE:                   'NOMAXVALUE';
NOMINVALUE:                   'NOMINVALUE';
NONE:                         'NONE';
NOORDER:                      'NOORDER';
NOSCHEMACHECK:                'NOSCHEMACHECK';
NOT:                          'NOT';
NOWAIT:                       'NOWAIT';
NULL:                         'NULL';
NULLS:                        'NULLS';
NUMBER:                       'NUMBER';
NUMERIC:                      'NUMERIC';
NVARCHAR2:                    'NVARCHAR2';
OBJECT:                       'OBJECT';
OF:                           'OF';
OFF:                          'OFF';
OID:                          'OID';
OLD:                          'OLD';
ON:                           'ON';
ONLY:                         'ONLY';
OPEN:                         'OPEN';
OPTION:                       'OPTION';
OR:                           'OR';
ORADATA:                      'ORADATA';
ORDER:                        'ORDER';
ORDINALITY:                   'ORDINALITY';
OSERROR:                      'OSERROR';
OUT:                          'OUT';
OUTER:                        'OUTER';
OVER:                         'OVER';
OVERRIDING:                   'OVERRIDING';
PACKAGE:                      'PACKAGE';
PARALLEL_ENABLE:              'PARALLEL_ENABLE';
PARAMETERS:                   'PARAMETERS';
PARENT:                       'PARENT';
PARTITION:                    'PARTITION';
PASSING:                      'PASSING';
PATH:                         'PATH';
PERCENT_ISOPEN:               '%ISOPEN';
PERCENT_FOUND:                '%FOUND';
PERCENT_NOTFOUND:             '%NOTFOUND';
PERCENT_ROWCOUNT:             '%ROWCOUNT';
PERCENT_ROWTYPE:              '%ROWTYPE';
PERCENT_TYPE:                 '%TYPE';
PIPELINED:                    'PIPELINED';
PIVOT:                        'PIVOT';
PLAN:                         'PLAN';
PUBLIC:                       'PUBLIC';
PLS_INTEGER:                  'PLS_INTEGER';
POSITIVE:                     'POSITIVE';
POSITIVEN:                    'POSITIVEN';
PRAGMA:                       'PRAGMA';
PRECEDING:                    'PRECEDING';
PRECISION:                    'PRECISION';
PRESENT:                      'PRESENT';
PRIOR:                        'PRIOR';
PROCEDURE:                    'PROCEDURE';
RAISE:                        'RAISE';
RANGE:                        'RANGE';
RAW:                          'RAW';
READ:                         'READ';
REAL:                         'REAL';
RECORD:                       'RECORD';
REF:                          'REF';
REFERENCE:                    'REFERENCE';
REFERENCING:                  'REFERENCING';
REJECT:                       'REJECT';
RENAME:                       'RENAME';
REPLACE:                      'REPLACE';
RESPECT:                      'RESPECT';
RESTRICT_REFERENCES:          'RESTRICT_REFERENCES';
RESULT:                       'RESULT';
RETURN:                       'RETURN';
RETURNING:                    'RETURNING';
REUSE:                        'REUSE';
REVERSE:                      'REVERSE';
REVOKE:                       'REVOKE';
RIGHT:                        'RIGHT';
ROLLBACK:                     'ROLLBACK';
ROLLUP:                       'ROLLUP';
ROW:                          'ROW';
ROWID:                        'ROWID';
ROWS:                         'ROWS';
RULES:                        'RULES';
SAMPLE:                       'SAMPLE';
SAVE:                         'SAVE';
SAVEPOINT:                    'SAVEPOINT';
SCHEMA:                       'SCHEMA';
SCHEMACHECK:                  'SCHEMACHECK';
SCN:                          'SCN';
SEARCH:                       'SEARCH';
SECOND:                       'SECOND';
SEED:                         'SEED';
SEGMENT:                      'SEGMENT';
SELECT:                       'SELECT';
SELF:                         'SELF';
SEQUENCE:                     'SEQUENCE';
SEQUENTIAL:                   'SEQUENTIAL';
SERIALIZABLE:                 'SERIALIZABLE';
SERIALLY_REUSABLE:            'SERIALLY_REUSABLE';
SERVERERROR:                  'SERVERERROR';
SESSIONTIMEZONE:              'SESSIONTIMEZONE';
SET:                          'SET';
SETS:                         'SETS';
SETTINGS:                     'SETTINGS';
SHARE:                        'SHARE';
SHOW:                         'SHOW';
SHUTDOWN:                     'SHUTDOWN';
SIBLINGS:                     'SIBLINGS';
SIGNTYPE:                     'SIGNTYPE';
SIMPLE_INTEGER:               'SIMPLE_INTEGER';
SINGLE:                       'SINGLE';
SIZE:                         'SIZE';
SKIP_:                        'SKIP';
SMALLINT:                     'SMALLINT';
SNAPSHOT:                     'SNAPSHOT';
SOME:                         'SOME';
SPECIFICATION:                'SPECIFICATION';
SQLDATA:                      'SQLDATA';
SQLERROR:                     'SQLERROR';
STANDALONE:                   'STANDALONE';
START:                        'START';
STARTUP:                      'STARTUP';
STATEMENT:                    'STATEMENT';
STATEMENT_ID:                 'STATEMENT_ID';
STATIC:                       'STATIC';
STATISTICS:                   'STATISTICS';
STRING:                       'STRING';
SUBMULTISET:                  'SUBMULTISET';
SUBPARTITION:                 'SUBPARTITION';
SUBSTITUTABLE:                'SUBSTITUTABLE';
SUBTYPE:                      'SUBTYPE';
SUCCESS:                      'SUCCESS';
SUSPEND:                      'SUSPEND';
SYNONYM:                      'SYNONYM';
TABLE:                        'TABLE';
THE:                          'THE';
THEN:                         'THEN';
TIME:                         'TIME';
TIMESTAMP:                    'TIMESTAMP';
TIMESTAMP_LTZ_UNCONSTRAINED:  'TIMESTAMP_LTZ_UNCONSTRAINED';
TIMESTAMP_TZ_UNCONSTRAINED:   'TIMESTAMP_TZ_UNCONSTRAINED';
TIMESTAMP_UNCONSTRAINED:      'TIMESTAMP_UNCONSTRAINED';
TIMEZONE_ABBR:                'TIMEZONE_ABBR';
TIMEZONE_HOUR:                'TIMEZONE_HOUR';
TIMEZONE_MINUTE:              'TIMEZONE_MINUTE';
TIMEZONE_REGION:              'TIMEZONE_REGION';
TO:                           'TO';
TRAILING:                     'TRAILING';
TRANSACTION:                  'TRANSACTION';
TRANSLATE:                    'TRANSLATE';
TREAT:                        'TREAT';
TRIGGER:                      'TRIGGER';
TRUE:                         'TRUE';
TRUNCATE:                     'TRUNCATE';
TYPE:                         'TYPE';
UNBOUNDED:                    'UNBOUNDED';
UNDER:                        'UNDER';
UNION:                        'UNION';
UNIQUE:                       'UNIQUE';
UNLIMITED:                    'UNLIMITED';
UNPIVOT:                      'UNPIVOT';
UNTIL:                        'UNTIL';
UPDATE:                       'UPDATE';
UPDATED:                      'UPDATED';
UPSERT:                       'UPSERT';
UROWID:                       'UROWID';
USE:                          'USE';
USING:                        'USING';
VALIDATE:                     'VALIDATE';
VALUE:                        'VALUE';
VALUES:                       'VALUES';
VARCHAR:                      'VARCHAR';
VARCHAR2:                     'VARCHAR2' | 'varchar2';
VARIABLE:                     'VARIABLE';
VARRAY:                       'VARRAY';
VARYING:                      'VARYING';
VERSION:                      'VERSION';
VERSIONS:                     'VERSIONS';
WAIT:                         'WAIT';
WARNING:                      'WARNING';
WELLFORMED:                   'WELLFORMED';
WHEN:                         'WHEN';
WHENEVER:                     'WHENEVER';
WHERE:                        'WHERE';
WHILE:                        'WHILE';
WITH:                         'WITH';
WITHIN:                       'WITHIN';
WORK:                         'WORK';
WRITE:                        'WRITE';
XML:                          'XML';
XMLAGG:                       'XMLAGG';
XMLATTRIBUTES:                'XMLATTRIBUTES';
XMLCAST:                      'XMLCAST';
XMLCOLATTVAL:                 'XMLCOLATTVAL';
XMLELEMENT:                   'XMLELEMENT';
XMLEXISTS:                    'XMLEXISTS';
XMLFOREST:                    'XMLFOREST';
XMLNAMESPACES:                'XMLNAMESPACES';
XMLPARSE:                     'XMLPARSE';
XMLPI:                        'XMLPI';
XMLQUERY:                     'XMLQUERY';
XMLROOT:                      'XMLROOT';
XMLSERIALIZE:                 'XMLSERIALIZE';
XMLTABLE:                     'XMLTABLE';
YEAR:                         'YEAR';
YES:                          'YES';
YMINTERVAL_UNCONSTRAINED:     'YMINTERVAL_UNCONSTRAINED';
ZONE:                         'ZONE';

PREDICTION:                   'PREDICTION';
PREDICTION_BOUNDS:            'PREDICTION_BOUNDS';
PREDICTION_COST:              'PREDICTION_COST';
PREDICTION_DETAILS:           'PREDICTION_DETAILS';
PREDICTION_PROBABILITY:       'PREDICTION_PROBABILITY';
PREDICTION_SET:               'PREDICTION_SET';

CUME_DIST:                    'CUME_DIST';
DENSE_RANK:                   'DENSE_RANK';
LISTAGG:                      'LISTAGG';
PERCENT_RANK:                 'PERCENT_RANK';
PERCENTILE_CONT:              'PERCENTILE_CONT';
PERCENTILE_DISC:              'PERCENTILE_DISC';
RANK:                         'RANK';

AVG:                          'AVG';
CORR:                         'CORR';
COVAR_:                       'COVAR_';
DECODE:                       'DECODE';
LAG:                          'LAG';
LEAD:                         'LEAD';
MAX:                          'MAX';
MEDIAN:                       'MEDIAN';
MIN:                          'MIN';
NTILE:                        'NTILE';
NVL:                          'NVL';
RATIO_TO_REPORT:              'RATIO_TO_REPORT';
REGR_:                        'REGR_';
ROUND:                        'ROUND';
ROW_NUMBER:                   'ROW_NUMBER';
SUBSTR:                       'SUBSTR';
TO_CHAR:                      'TO_CHAR';
TRIM:                         'TRIM';
SUM:                          'SUM';
STDDEV:                       'STDDEV';
VAR_:                         'VAR_';
VARIANCE:                     'VARIANCE';

//Lexer Package Rules for EDB supported Packages

DBMS_ALERT:     'DBMS_ALERT';
DBMS_AQADM:     'DBMS_AQADM';
DBMS_AQ:        'DBMS_AQ';
DBMS_CRYPTO:    'DBMS_CRYPTO';
DBMS_JOB:       'DBMS_JOB';
DBMS_LOB:       'DBMS_LOB';
DBMS_LOCK:      'DBMS_LOCK';
DBMS_MVIEW:     'DBMS_MVIEW';
DBMS_OUTPUT:    'DBMS_OUTPUT';
DBMS_PIPE:      'DBMS_PIPE';
DBMS_PROFILER:  'DBMS_PROFILER';
DBMS_RANDOM:    'DBMS_RANDOM';
DBMS_RLS:       'DBMS_RLS';
DBMS_SCHEDULER: 'DBMS_SCHEDULER';
DBMS_SESSION:   'DBMS_SESSION';
DBMS_SQL:       'DBMS_SQL';
DBMS_UTILITY:   'DBMS_UTILITY';
UTL_ENCODE:     'UTL_ENCODE';
UTL_FILE:       'UTL_FILE';
UTL_HTTP:       'UTL_HTTP';
UTL_MAIL:       'UTL_MAIL';
UTL_RAW:        'UTL_RAW';
UTL_SMTP:       'UTL_SMTP';
UTL_TCP:        'UTL_TCP';
UTL_URL:        'UTL_URL';

// Rule #358 <NATIONAL_CHAR_STRING_LIT> - subtoken typecast in <REGULAR_ID>, it also incorporates <character_representation>
//  Lowercase 'n' is a usual addition to the standard
NATIONAL_CHAR_STRING_LIT: 'N' '\'' (~('\'' | '\r' | '\n' ) | '\'' '\'' | NEWLINE)* '\'';

//  Rule #040 <BIT_STRING_LIT> - subtoken typecast in <REGULAR_ID>
//  Lowercase 'b' is a usual addition to the standard
BIT_STRING_LIT: 'B' ('\'' [01]* '\'')+;

//  Rule #284 <HEX_STRING_LIT> - subtoken typecast in <REGULAR_ID>
//  Lowercase 'x' is a usual addition to the standard
HEX_STRING_LIT: 'X' ('\'' [A-F0-9]* '\'')+;
DOUBLE_PERIOD: '..';
PERIOD:        '.';

//{ Rule #238 <EXACT_NUM_LIT>
//  This rule is a bit tricky - it resolves the ambiguity with <PERIOD>
//  It also incorporates <mantisa> and <exponent> for the <APPROXIMATE_NUM_LIT>
//  Rule #501 <signed_integer> was incorporated directly in the token <APPROXIMATE_NUM_LIT>
//  See also the rule #617 <unsigned_num_lit>
/*
    : (
            UNSIGNED_INTEGER
            ( '.' UNSIGNED_INTEGER
            | {$type = UNSIGNED_INTEGER;}
            ) ( E ('+' | '-')? UNSIGNED_INTEGER {$type = APPROXIMATE_NUM_LIT;} )?
    | '.' UNSIGNED_INTEGER ( E ('+' | '-')? UNSIGNED_INTEGER {$type = APPROXIMATE_NUM_LIT;} )?
    )
    (D | F)?
    ;*/

UNSIGNED_INTEGER: UNSIGNED_INTEGER_FRAGMENT;
APPROXIMATE_NUM_LIT: FLOAT_FRAGMENT ('E' ('+'|'-')? (FLOAT_FRAGMENT | UNSIGNED_INTEGER_FRAGMENT))? ('D' | 'F')?;

// Rule #--- <CHAR_STRING> is a base for Rule #065 <char_string_lit> , it incorporates <character_representation>
// and a superfluous subtoken typecasting of the "QUOTE"
CHAR_STRING: '\'' (~('\'' | '\r' | '\n') | '\'' '\'' | NEWLINE)* '\'';

// Perl-style quoted string, see Oracle SQL reference, chapter String Literals
CHAR_STRING_PERL    : 'Q' ( QS_ANGLE | QS_BRACE | QS_BRACK | QS_PAREN) -> type(CHAR_STRING);
fragment QUOTE      : '\'' ;
fragment QS_ANGLE   : QUOTE '<' .*? '>' QUOTE ;
fragment QS_BRACE   : QUOTE '{' .*? '}' QUOTE ;
fragment QS_BRACK   : QUOTE '[' .*? ']' QUOTE ;
fragment QS_PAREN   : QUOTE '(' .*? ')' QUOTE ;
fragment QS_OTHER_CH: ~('<' | '{' | '[' | '(' | ' ' | '\t' | '\n' | '\r');

// Rule #163 <DELIMITED_ID>
DELIMITED_ID: '"' (~('"' | '\r' | '\n') | '"' '"')+ '"' ;

// Rule #546 <SQL_SPECIAL_CHAR> was split into single rules
PERCENT: '%';
AMPERSAND: '&';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
DOUBLE_ASTERISK: '**';
ASTERISK: '*';
PLUS_SIGN: '+';
MINUS_SIGN: '-';
COMMA: ',';
SOLIDUS: '/';
AT_SIGN: '@';
ASSIGN_OP: ':=';

// See OCI reference for more information about this
BINDVAR
    : ':' SIMPLE_LETTER  (SIMPLE_LETTER | [0-9] | '_')*
    | ':' DELIMITED_ID  // not used in SQL but spotted in v$sqltext when using cursor_sharing
    | ':' UNSIGNED_INTEGER
    | QUESTION_MARK // not in SQL, not in Oracle, not in OCI, use this for JDBC
    ;

COLON: ':';
SEMICOLON: ';';
LESS_THAN_OR_EQUALS_OP: '<=';
LESS_THAN_OP: '<';
GREATER_THAN_OR_EQUALS_OP: '>=';
NOT_EQUAL_OP: '!='| '<>'| '^='| '~=';
CARRET_OPERATOR_PART: '^';
TILDE_OPERATOR_PART: '~';
EXCLAMATION_OPERATOR_PART: '!';
GREATER_THAN_OP: '>';

fragment
QUESTION_MARK: '?';

// protected UNDERSCORE : '_' SEPARATOR ; // subtoken typecast within <INTRODUCER>
CONCATENATION_OP: '||';
VERTICAL_BAR: '|';
EQUALS_OP: '=';

// Rule #532 <SQL_EMBDD_LANGUAGE_CHAR> was split into single rules:
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';

//{ Rule #319 <INTRODUCER>
INTRODUCER
    : '_' //(SEPARATOR {$type = UNDERSCORE;})?
    ;

//{ Rule #479 <SEPARATOR>
//  It was originally a protected rule set to be filtered out but the <COMMENT> and <'-'> clashed.
/*SEPARATOR
    : '-' -> type('-')
    | COMMENT -> channel(HIDDEN)
    | (SPACE | NEWLINE)+ -> channel(HIDDEN)
    ;*/
//}

SPACES: [ \t\r\n]+ -> skip;

//{ Rule #504 <SIMPLE_LETTER> - simple_latin _letter was generalised into SIMPLE_LETTER
//  Unicode is yet to be implemented - see NSF0
fragment
SIMPLE_LETTER
    : [A-Z]
    ;
//}

//  Rule #176 <DIGIT> was incorporated by <UNSIGNED_INTEGER>
//{ Rule #615 <UNSIGNED_INTEGER> - subtoken typecast in <EXACT_NUM_LIT>
fragment
UNSIGNED_INTEGER_FRAGMENT: [0-9]+ ;

fragment
FLOAT_FRAGMENT
    : UNSIGNED_INTEGER* '.'? UNSIGNED_INTEGER+
    ;

//{ Rule #097 <COMMENT>
SINGLE_LINE_COMMENT: '--' ~('\r' | '\n')* (NEWLINE | EOF)   -> channel(HIDDEN);
MULTI_LINE_COMMENT: '/*' .*? '*/'                           -> channel(HIDDEN);

// SQL*Plus prompt
// TODO should be grammar rule, but tricky to implement
PROMPT
    : 'prompt' SPACE ( ~('\r' | '\n') )* (NEWLINE|EOF)
    ;

START_CMD
    // TODO When using full word START there is a conflict with START WITH in sequences and CONNECT BY queries
    // 'start' SPACE ( ~( '\r' | '\n') )* (NEWLINE|EOF)
    : 'sta' SPACE ( ~('\r' | '\n') )* (NEWLINE|EOF)
    // TODO Single @ conflicts with a database link name, like employees@remote
    // | '@' ( ~('\r' | '\n') )* (NEWLINE|EOF)
    | '@@' ( ~('\r' | '\n') )* (NEWLINE|EOF)
    ;

//{ Rule #360 <NEWLINE>
fragment
NEWLINE: '\r'? '\n';

fragment
SPACE: [ \t];

//{ Rule #442 <REGULAR_ID> additionally encapsulates a few STRING_LITs.
//  Within testLiterals all reserved and non-reserved words are being resolved

REGULAR_ID: SIMPLE_LETTER (SIMPLE_LETTER | '$' | '_' | '.' | '#' | [0-9])*;
ZV: '@!' -> channel(HIDDEN);
