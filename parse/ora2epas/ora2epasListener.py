# Generated from ora2epas.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ora2epasParser import ora2epasParser
else:
    from ora2epasParser import ora2epasParser

# This class defines a complete listener for a parse tree produced by ora2epasParser.
class ora2epasListener(ParseTreeListener):

    # Enter a parse tree produced by ora2epasParser#swallow_to_semi.
    def enterSwallow_to_semi(self, ctx:ora2epasParser.Swallow_to_semiContext):
        pass

    # Exit a parse tree produced by ora2epasParser#swallow_to_semi.
    def exitSwallow_to_semi(self, ctx:ora2epasParser.Swallow_to_semiContext):
        pass


    # Enter a parse tree produced by ora2epasParser#compilation_unit.
    def enterCompilation_unit(self, ctx:ora2epasParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by ora2epasParser#compilation_unit.
    def exitCompilation_unit(self, ctx:ora2epasParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sql_script.
    def enterSql_script(self, ctx:ora2epasParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sql_script.
    def exitSql_script(self, ctx:ora2epasParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by ora2epasParser#unit_statement.
    def enterUnit_statement(self, ctx:ora2epasParser.Unit_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#unit_statement.
    def exitUnit_statement(self, ctx:ora2epasParser.Unit_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_cluster_table.
    def enterCreate_cluster_table(self, ctx:ora2epasParser.Create_cluster_tableContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_cluster_table.
    def exitCreate_cluster_table(self, ctx:ora2epasParser.Create_cluster_tableContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_database_links.
    def enterCreate_database_links(self, ctx:ora2epasParser.Create_database_linksContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_database_links.
    def exitCreate_database_links(self, ctx:ora2epasParser.Create_database_linksContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_function_body.
    def enterCreate_function_body(self, ctx:ora2epasParser.Create_function_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_function_body.
    def exitCreate_function_body(self, ctx:ora2epasParser.Create_function_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#parallel_enable_clause.
    def enterParallel_enable_clause(self, ctx:ora2epasParser.Parallel_enable_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#parallel_enable_clause.
    def exitParallel_enable_clause(self, ctx:ora2epasParser.Parallel_enable_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#partition_by_clause.
    def enterPartition_by_clause(self, ctx:ora2epasParser.Partition_by_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#partition_by_clause.
    def exitPartition_by_clause(self, ctx:ora2epasParser.Partition_by_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#streaming_clause.
    def enterStreaming_clause(self, ctx:ora2epasParser.Streaming_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#streaming_clause.
    def exitStreaming_clause(self, ctx:ora2epasParser.Streaming_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_index.
    def enterCreate_index(self, ctx:ora2epasParser.Create_indexContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_index.
    def exitCreate_index(self, ctx:ora2epasParser.Create_indexContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_package.
    def enterCreate_package(self, ctx:ora2epasParser.Create_packageContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_package.
    def exitCreate_package(self, ctx:ora2epasParser.Create_packageContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_package_body.
    def enterCreate_package_body(self, ctx:ora2epasParser.Create_package_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_package_body.
    def exitCreate_package_body(self, ctx:ora2epasParser.Create_package_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#package_obj_spec.
    def enterPackage_obj_spec(self, ctx:ora2epasParser.Package_obj_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#package_obj_spec.
    def exitPackage_obj_spec(self, ctx:ora2epasParser.Package_obj_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#procedure_spec.
    def enterProcedure_spec(self, ctx:ora2epasParser.Procedure_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#procedure_spec.
    def exitProcedure_spec(self, ctx:ora2epasParser.Procedure_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#function_spec.
    def enterFunction_spec(self, ctx:ora2epasParser.Function_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#function_spec.
    def exitFunction_spec(self, ctx:ora2epasParser.Function_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#package_obj_body.
    def enterPackage_obj_body(self, ctx:ora2epasParser.Package_obj_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#package_obj_body.
    def exitPackage_obj_body(self, ctx:ora2epasParser.Package_obj_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#function_body.
    def enterFunction_body(self, ctx:ora2epasParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#function_body.
    def exitFunction_body(self, ctx:ora2epasParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#procedure_body.
    def enterProcedure_body(self, ctx:ora2epasParser.Procedure_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#procedure_body.
    def exitProcedure_body(self, ctx:ora2epasParser.Procedure_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_procedure_body.
    def enterCreate_procedure_body(self, ctx:ora2epasParser.Create_procedure_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_procedure_body.
    def exitCreate_procedure_body(self, ctx:ora2epasParser.Create_procedure_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_trigger.
    def enterCreate_trigger(self, ctx:ora2epasParser.Create_triggerContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_trigger.
    def exitCreate_trigger(self, ctx:ora2epasParser.Create_triggerContext):
        pass


    # Enter a parse tree produced by ora2epasParser#trigger_follows_clause.
    def enterTrigger_follows_clause(self, ctx:ora2epasParser.Trigger_follows_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#trigger_follows_clause.
    def exitTrigger_follows_clause(self, ctx:ora2epasParser.Trigger_follows_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#trigger_when_clause.
    def enterTrigger_when_clause(self, ctx:ora2epasParser.Trigger_when_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#trigger_when_clause.
    def exitTrigger_when_clause(self, ctx:ora2epasParser.Trigger_when_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#simple_dml_trigger.
    def enterSimple_dml_trigger(self, ctx:ora2epasParser.Simple_dml_triggerContext):
        pass

    # Exit a parse tree produced by ora2epasParser#simple_dml_trigger.
    def exitSimple_dml_trigger(self, ctx:ora2epasParser.Simple_dml_triggerContext):
        pass


    # Enter a parse tree produced by ora2epasParser#for_each_row.
    def enterFor_each_row(self, ctx:ora2epasParser.For_each_rowContext):
        pass

    # Exit a parse tree produced by ora2epasParser#for_each_row.
    def exitFor_each_row(self, ctx:ora2epasParser.For_each_rowContext):
        pass


    # Enter a parse tree produced by ora2epasParser#compound_dml_trigger.
    def enterCompound_dml_trigger(self, ctx:ora2epasParser.Compound_dml_triggerContext):
        pass

    # Exit a parse tree produced by ora2epasParser#compound_dml_trigger.
    def exitCompound_dml_trigger(self, ctx:ora2epasParser.Compound_dml_triggerContext):
        pass


    # Enter a parse tree produced by ora2epasParser#non_dml_trigger.
    def enterNon_dml_trigger(self, ctx:ora2epasParser.Non_dml_triggerContext):
        pass

    # Exit a parse tree produced by ora2epasParser#non_dml_trigger.
    def exitNon_dml_trigger(self, ctx:ora2epasParser.Non_dml_triggerContext):
        pass


    # Enter a parse tree produced by ora2epasParser#trigger_body.
    def enterTrigger_body(self, ctx:ora2epasParser.Trigger_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#trigger_body.
    def exitTrigger_body(self, ctx:ora2epasParser.Trigger_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#routine_clause.
    def enterRoutine_clause(self, ctx:ora2epasParser.Routine_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#routine_clause.
    def exitRoutine_clause(self, ctx:ora2epasParser.Routine_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#compound_trigger_block.
    def enterCompound_trigger_block(self, ctx:ora2epasParser.Compound_trigger_blockContext):
        pass

    # Exit a parse tree produced by ora2epasParser#compound_trigger_block.
    def exitCompound_trigger_block(self, ctx:ora2epasParser.Compound_trigger_blockContext):
        pass


    # Enter a parse tree produced by ora2epasParser#timing_point_section.
    def enterTiming_point_section(self, ctx:ora2epasParser.Timing_point_sectionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#timing_point_section.
    def exitTiming_point_section(self, ctx:ora2epasParser.Timing_point_sectionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#non_dml_event.
    def enterNon_dml_event(self, ctx:ora2epasParser.Non_dml_eventContext):
        pass

    # Exit a parse tree produced by ora2epasParser#non_dml_event.
    def exitNon_dml_event(self, ctx:ora2epasParser.Non_dml_eventContext):
        pass


    # Enter a parse tree produced by ora2epasParser#dml_event_clause.
    def enterDml_event_clause(self, ctx:ora2epasParser.Dml_event_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#dml_event_clause.
    def exitDml_event_clause(self, ctx:ora2epasParser.Dml_event_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#dml_event_element.
    def enterDml_event_element(self, ctx:ora2epasParser.Dml_event_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#dml_event_element.
    def exitDml_event_element(self, ctx:ora2epasParser.Dml_event_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#dml_event_nested_clause.
    def enterDml_event_nested_clause(self, ctx:ora2epasParser.Dml_event_nested_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#dml_event_nested_clause.
    def exitDml_event_nested_clause(self, ctx:ora2epasParser.Dml_event_nested_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#referencing_clause.
    def enterReferencing_clause(self, ctx:ora2epasParser.Referencing_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#referencing_clause.
    def exitReferencing_clause(self, ctx:ora2epasParser.Referencing_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#referencing_element.
    def enterReferencing_element(self, ctx:ora2epasParser.Referencing_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#referencing_element.
    def exitReferencing_element(self, ctx:ora2epasParser.Referencing_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_type.
    def enterCreate_type(self, ctx:ora2epasParser.Create_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_type.
    def exitCreate_type(self, ctx:ora2epasParser.Create_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_definition.
    def enterType_definition(self, ctx:ora2epasParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_definition.
    def exitType_definition(self, ctx:ora2epasParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#object_type_def.
    def enterObject_type_def(self, ctx:ora2epasParser.Object_type_defContext):
        pass

    # Exit a parse tree produced by ora2epasParser#object_type_def.
    def exitObject_type_def(self, ctx:ora2epasParser.Object_type_defContext):
        pass


    # Enter a parse tree produced by ora2epasParser#object_as_part.
    def enterObject_as_part(self, ctx:ora2epasParser.Object_as_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#object_as_part.
    def exitObject_as_part(self, ctx:ora2epasParser.Object_as_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#object_under_part.
    def enterObject_under_part(self, ctx:ora2epasParser.Object_under_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#object_under_part.
    def exitObject_under_part(self, ctx:ora2epasParser.Object_under_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#nested_table_type_def.
    def enterNested_table_type_def(self, ctx:ora2epasParser.Nested_table_type_defContext):
        pass

    # Exit a parse tree produced by ora2epasParser#nested_table_type_def.
    def exitNested_table_type_def(self, ctx:ora2epasParser.Nested_table_type_defContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sqlj_object_type.
    def enterSqlj_object_type(self, ctx:ora2epasParser.Sqlj_object_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sqlj_object_type.
    def exitSqlj_object_type(self, ctx:ora2epasParser.Sqlj_object_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_body.
    def enterType_body(self, ctx:ora2epasParser.Type_bodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_body.
    def exitType_body(self, ctx:ora2epasParser.Type_bodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_body_elements.
    def enterType_body_elements(self, ctx:ora2epasParser.Type_body_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_body_elements.
    def exitType_body_elements(self, ctx:ora2epasParser.Type_body_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#map_order_func_declaration.
    def enterMap_order_func_declaration(self, ctx:ora2epasParser.Map_order_func_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#map_order_func_declaration.
    def exitMap_order_func_declaration(self, ctx:ora2epasParser.Map_order_func_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subprog_decl_in_type.
    def enterSubprog_decl_in_type(self, ctx:ora2epasParser.Subprog_decl_in_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subprog_decl_in_type.
    def exitSubprog_decl_in_type(self, ctx:ora2epasParser.Subprog_decl_in_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#proc_decl_in_type.
    def enterProc_decl_in_type(self, ctx:ora2epasParser.Proc_decl_in_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#proc_decl_in_type.
    def exitProc_decl_in_type(self, ctx:ora2epasParser.Proc_decl_in_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#func_decl_in_type.
    def enterFunc_decl_in_type(self, ctx:ora2epasParser.Func_decl_in_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#func_decl_in_type.
    def exitFunc_decl_in_type(self, ctx:ora2epasParser.Func_decl_in_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#constructor_declaration.
    def enterConstructor_declaration(self, ctx:ora2epasParser.Constructor_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#constructor_declaration.
    def exitConstructor_declaration(self, ctx:ora2epasParser.Constructor_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_view.
    def enterCreate_view(self, ctx:ora2epasParser.Create_viewContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_view.
    def exitCreate_view(self, ctx:ora2epasParser.Create_viewContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_materialized_view.
    def enterCreate_materialized_view(self, ctx:ora2epasParser.Create_materialized_viewContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_materialized_view.
    def exitCreate_materialized_view(self, ctx:ora2epasParser.Create_materialized_viewContext):
        pass


    # Enter a parse tree produced by ora2epasParser#modifier_clause.
    def enterModifier_clause(self, ctx:ora2epasParser.Modifier_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#modifier_clause.
    def exitModifier_clause(self, ctx:ora2epasParser.Modifier_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#object_member_spec.
    def enterObject_member_spec(self, ctx:ora2epasParser.Object_member_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#object_member_spec.
    def exitObject_member_spec(self, ctx:ora2epasParser.Object_member_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sqlj_object_type_attr.
    def enterSqlj_object_type_attr(self, ctx:ora2epasParser.Sqlj_object_type_attrContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sqlj_object_type_attr.
    def exitSqlj_object_type_attr(self, ctx:ora2epasParser.Sqlj_object_type_attrContext):
        pass


    # Enter a parse tree produced by ora2epasParser#element_spec.
    def enterElement_spec(self, ctx:ora2epasParser.Element_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#element_spec.
    def exitElement_spec(self, ctx:ora2epasParser.Element_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#element_spec_options.
    def enterElement_spec_options(self, ctx:ora2epasParser.Element_spec_optionsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#element_spec_options.
    def exitElement_spec_options(self, ctx:ora2epasParser.Element_spec_optionsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subprogram_spec.
    def enterSubprogram_spec(self, ctx:ora2epasParser.Subprogram_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subprogram_spec.
    def exitSubprogram_spec(self, ctx:ora2epasParser.Subprogram_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_procedure_spec.
    def enterType_procedure_spec(self, ctx:ora2epasParser.Type_procedure_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_procedure_spec.
    def exitType_procedure_spec(self, ctx:ora2epasParser.Type_procedure_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_function_spec.
    def enterType_function_spec(self, ctx:ora2epasParser.Type_function_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_function_spec.
    def exitType_function_spec(self, ctx:ora2epasParser.Type_function_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#constructor_spec.
    def enterConstructor_spec(self, ctx:ora2epasParser.Constructor_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#constructor_spec.
    def exitConstructor_spec(self, ctx:ora2epasParser.Constructor_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#map_order_function_spec.
    def enterMap_order_function_spec(self, ctx:ora2epasParser.Map_order_function_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#map_order_function_spec.
    def exitMap_order_function_spec(self, ctx:ora2epasParser.Map_order_function_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pragma_clause.
    def enterPragma_clause(self, ctx:ora2epasParser.Pragma_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pragma_clause.
    def exitPragma_clause(self, ctx:ora2epasParser.Pragma_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pragma_elements.
    def enterPragma_elements(self, ctx:ora2epasParser.Pragma_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pragma_elements.
    def exitPragma_elements(self, ctx:ora2epasParser.Pragma_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_elements_parameter.
    def enterType_elements_parameter(self, ctx:ora2epasParser.Type_elements_parameterContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_elements_parameter.
    def exitType_elements_parameter(self, ctx:ora2epasParser.Type_elements_parameterContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_sequence.
    def enterCreate_sequence(self, ctx:ora2epasParser.Create_sequenceContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_sequence.
    def exitCreate_sequence(self, ctx:ora2epasParser.Create_sequenceContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sequence_spec.
    def enterSequence_spec(self, ctx:ora2epasParser.Sequence_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sequence_spec.
    def exitSequence_spec(self, ctx:ora2epasParser.Sequence_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sequence_start_clause.
    def enterSequence_start_clause(self, ctx:ora2epasParser.Sequence_start_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sequence_start_clause.
    def exitSequence_start_clause(self, ctx:ora2epasParser.Sequence_start_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_table.
    def enterCreate_table(self, ctx:ora2epasParser.Create_tableContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_table.
    def exitCreate_table(self, ctx:ora2epasParser.Create_tableContext):
        pass


    # Enter a parse tree produced by ora2epasParser#comment_on_column.
    def enterComment_on_column(self, ctx:ora2epasParser.Comment_on_columnContext):
        pass

    # Exit a parse tree produced by ora2epasParser#comment_on_column.
    def exitComment_on_column(self, ctx:ora2epasParser.Comment_on_columnContext):
        pass


    # Enter a parse tree produced by ora2epasParser#create_synonym.
    def enterCreate_synonym(self, ctx:ora2epasParser.Create_synonymContext):
        pass

    # Exit a parse tree produced by ora2epasParser#create_synonym.
    def exitCreate_synonym(self, ctx:ora2epasParser.Create_synonymContext):
        pass


    # Enter a parse tree produced by ora2epasParser#comment_on_table.
    def enterComment_on_table(self, ctx:ora2epasParser.Comment_on_tableContext):
        pass

    # Exit a parse tree produced by ora2epasParser#comment_on_table.
    def exitComment_on_table(self, ctx:ora2epasParser.Comment_on_tableContext):
        pass


    # Enter a parse tree produced by ora2epasParser#anonymous_block.
    def enterAnonymous_block(self, ctx:ora2epasParser.Anonymous_blockContext):
        pass

    # Exit a parse tree produced by ora2epasParser#anonymous_block.
    def exitAnonymous_block(self, ctx:ora2epasParser.Anonymous_blockContext):
        pass


    # Enter a parse tree produced by ora2epasParser#invoker_rights_clause.
    def enterInvoker_rights_clause(self, ctx:ora2epasParser.Invoker_rights_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#invoker_rights_clause.
    def exitInvoker_rights_clause(self, ctx:ora2epasParser.Invoker_rights_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#compiler_parameters_clause.
    def enterCompiler_parameters_clause(self, ctx:ora2epasParser.Compiler_parameters_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#compiler_parameters_clause.
    def exitCompiler_parameters_clause(self, ctx:ora2epasParser.Compiler_parameters_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#call_spec.
    def enterCall_spec(self, ctx:ora2epasParser.Call_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#call_spec.
    def exitCall_spec(self, ctx:ora2epasParser.Call_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#java_spec.
    def enterJava_spec(self, ctx:ora2epasParser.Java_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#java_spec.
    def exitJava_spec(self, ctx:ora2epasParser.Java_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#c_spec.
    def enterC_spec(self, ctx:ora2epasParser.C_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#c_spec.
    def exitC_spec(self, ctx:ora2epasParser.C_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#c_agent_in_clause.
    def enterC_agent_in_clause(self, ctx:ora2epasParser.C_agent_in_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#c_agent_in_clause.
    def exitC_agent_in_clause(self, ctx:ora2epasParser.C_agent_in_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#c_parameters_clause.
    def enterC_parameters_clause(self, ctx:ora2epasParser.C_parameters_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#c_parameters_clause.
    def exitC_parameters_clause(self, ctx:ora2epasParser.C_parameters_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#parameter.
    def enterParameter(self, ctx:ora2epasParser.ParameterContext):
        pass

    # Exit a parse tree produced by ora2epasParser#parameter.
    def exitParameter(self, ctx:ora2epasParser.ParameterContext):
        pass


    # Enter a parse tree produced by ora2epasParser#default_value_part.
    def enterDefault_value_part(self, ctx:ora2epasParser.Default_value_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#default_value_part.
    def exitDefault_value_part(self, ctx:ora2epasParser.Default_value_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#declare_spec.
    def enterDeclare_spec(self, ctx:ora2epasParser.Declare_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#declare_spec.
    def exitDeclare_spec(self, ctx:ora2epasParser.Declare_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#variable_declaration.
    def enterVariable_declaration(self, ctx:ora2epasParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#variable_declaration.
    def exitVariable_declaration(self, ctx:ora2epasParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subtype_declaration.
    def enterSubtype_declaration(self, ctx:ora2epasParser.Subtype_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subtype_declaration.
    def exitSubtype_declaration(self, ctx:ora2epasParser.Subtype_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cursor_declaration.
    def enterCursor_declaration(self, ctx:ora2epasParser.Cursor_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cursor_declaration.
    def exitCursor_declaration(self, ctx:ora2epasParser.Cursor_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#parameter_spec.
    def enterParameter_spec(self, ctx:ora2epasParser.Parameter_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#parameter_spec.
    def exitParameter_spec(self, ctx:ora2epasParser.Parameter_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#exception_declaration.
    def enterException_declaration(self, ctx:ora2epasParser.Exception_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#exception_declaration.
    def exitException_declaration(self, ctx:ora2epasParser.Exception_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pragma_declaration.
    def enterPragma_declaration(self, ctx:ora2epasParser.Pragma_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pragma_declaration.
    def exitPragma_declaration(self, ctx:ora2epasParser.Pragma_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#record_type_def.
    def enterRecord_type_def(self, ctx:ora2epasParser.Record_type_defContext):
        pass

    # Exit a parse tree produced by ora2epasParser#record_type_def.
    def exitRecord_type_def(self, ctx:ora2epasParser.Record_type_defContext):
        pass


    # Enter a parse tree produced by ora2epasParser#field_spec.
    def enterField_spec(self, ctx:ora2epasParser.Field_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#field_spec.
    def exitField_spec(self, ctx:ora2epasParser.Field_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#ref_cursor_type_def.
    def enterRef_cursor_type_def(self, ctx:ora2epasParser.Ref_cursor_type_defContext):
        pass

    # Exit a parse tree produced by ora2epasParser#ref_cursor_type_def.
    def exitRef_cursor_type_def(self, ctx:ora2epasParser.Ref_cursor_type_defContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_declaration.
    def enterType_declaration(self, ctx:ora2epasParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_declaration.
    def exitType_declaration(self, ctx:ora2epasParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_type_def.
    def enterTable_type_def(self, ctx:ora2epasParser.Table_type_defContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_type_def.
    def exitTable_type_def(self, ctx:ora2epasParser.Table_type_defContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_indexed_by_part.
    def enterTable_indexed_by_part(self, ctx:ora2epasParser.Table_indexed_by_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_indexed_by_part.
    def exitTable_indexed_by_part(self, ctx:ora2epasParser.Table_indexed_by_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#varray_type_def.
    def enterVarray_type_def(self, ctx:ora2epasParser.Varray_type_defContext):
        pass

    # Exit a parse tree produced by ora2epasParser#varray_type_def.
    def exitVarray_type_def(self, ctx:ora2epasParser.Varray_type_defContext):
        pass


    # Enter a parse tree produced by ora2epasParser#seq_of_statements.
    def enterSeq_of_statements(self, ctx:ora2epasParser.Seq_of_statementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#seq_of_statements.
    def exitSeq_of_statements(self, ctx:ora2epasParser.Seq_of_statementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#label_declaration.
    def enterLabel_declaration(self, ctx:ora2epasParser.Label_declarationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#label_declaration.
    def exitLabel_declaration(self, ctx:ora2epasParser.Label_declarationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#statement.
    def enterStatement(self, ctx:ora2epasParser.StatementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#statement.
    def exitStatement(self, ctx:ora2epasParser.StatementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#assignment_statement.
    def enterAssignment_statement(self, ctx:ora2epasParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#assignment_statement.
    def exitAssignment_statement(self, ctx:ora2epasParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#continue_statement.
    def enterContinue_statement(self, ctx:ora2epasParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#continue_statement.
    def exitContinue_statement(self, ctx:ora2epasParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#exit_statement.
    def enterExit_statement(self, ctx:ora2epasParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#exit_statement.
    def exitExit_statement(self, ctx:ora2epasParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#goto_statement.
    def enterGoto_statement(self, ctx:ora2epasParser.Goto_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#goto_statement.
    def exitGoto_statement(self, ctx:ora2epasParser.Goto_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#if_statement.
    def enterIf_statement(self, ctx:ora2epasParser.If_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#if_statement.
    def exitIf_statement(self, ctx:ora2epasParser.If_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#elsif_part.
    def enterElsif_part(self, ctx:ora2epasParser.Elsif_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#elsif_part.
    def exitElsif_part(self, ctx:ora2epasParser.Elsif_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#else_part.
    def enterElse_part(self, ctx:ora2epasParser.Else_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#else_part.
    def exitElse_part(self, ctx:ora2epasParser.Else_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#loop_statement.
    def enterLoop_statement(self, ctx:ora2epasParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#loop_statement.
    def exitLoop_statement(self, ctx:ora2epasParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cursor_loop_param.
    def enterCursor_loop_param(self, ctx:ora2epasParser.Cursor_loop_paramContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cursor_loop_param.
    def exitCursor_loop_param(self, ctx:ora2epasParser.Cursor_loop_paramContext):
        pass


    # Enter a parse tree produced by ora2epasParser#forall_statement.
    def enterForall_statement(self, ctx:ora2epasParser.Forall_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#forall_statement.
    def exitForall_statement(self, ctx:ora2epasParser.Forall_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#bounds_clause.
    def enterBounds_clause(self, ctx:ora2epasParser.Bounds_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#bounds_clause.
    def exitBounds_clause(self, ctx:ora2epasParser.Bounds_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#between_bound.
    def enterBetween_bound(self, ctx:ora2epasParser.Between_boundContext):
        pass

    # Exit a parse tree produced by ora2epasParser#between_bound.
    def exitBetween_bound(self, ctx:ora2epasParser.Between_boundContext):
        pass


    # Enter a parse tree produced by ora2epasParser#lower_bound.
    def enterLower_bound(self, ctx:ora2epasParser.Lower_boundContext):
        pass

    # Exit a parse tree produced by ora2epasParser#lower_bound.
    def exitLower_bound(self, ctx:ora2epasParser.Lower_boundContext):
        pass


    # Enter a parse tree produced by ora2epasParser#upper_bound.
    def enterUpper_bound(self, ctx:ora2epasParser.Upper_boundContext):
        pass

    # Exit a parse tree produced by ora2epasParser#upper_bound.
    def exitUpper_bound(self, ctx:ora2epasParser.Upper_boundContext):
        pass


    # Enter a parse tree produced by ora2epasParser#null_statement.
    def enterNull_statement(self, ctx:ora2epasParser.Null_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#null_statement.
    def exitNull_statement(self, ctx:ora2epasParser.Null_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#raise_statement.
    def enterRaise_statement(self, ctx:ora2epasParser.Raise_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#raise_statement.
    def exitRaise_statement(self, ctx:ora2epasParser.Raise_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#return_statement.
    def enterReturn_statement(self, ctx:ora2epasParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#return_statement.
    def exitReturn_statement(self, ctx:ora2epasParser.Return_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#function_call.
    def enterFunction_call(self, ctx:ora2epasParser.Function_callContext):
        pass

    # Exit a parse tree produced by ora2epasParser#function_call.
    def exitFunction_call(self, ctx:ora2epasParser.Function_callContext):
        pass


    # Enter a parse tree produced by ora2epasParser#body.
    def enterBody(self, ctx:ora2epasParser.BodyContext):
        pass

    # Exit a parse tree produced by ora2epasParser#body.
    def exitBody(self, ctx:ora2epasParser.BodyContext):
        pass


    # Enter a parse tree produced by ora2epasParser#exception_handler.
    def enterException_handler(self, ctx:ora2epasParser.Exception_handlerContext):
        pass

    # Exit a parse tree produced by ora2epasParser#exception_handler.
    def exitException_handler(self, ctx:ora2epasParser.Exception_handlerContext):
        pass


    # Enter a parse tree produced by ora2epasParser#trigger_block.
    def enterTrigger_block(self, ctx:ora2epasParser.Trigger_blockContext):
        pass

    # Exit a parse tree produced by ora2epasParser#trigger_block.
    def exitTrigger_block(self, ctx:ora2epasParser.Trigger_blockContext):
        pass


    # Enter a parse tree produced by ora2epasParser#block.
    def enterBlock(self, ctx:ora2epasParser.BlockContext):
        pass

    # Exit a parse tree produced by ora2epasParser#block.
    def exitBlock(self, ctx:ora2epasParser.BlockContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sql_statement.
    def enterSql_statement(self, ctx:ora2epasParser.Sql_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sql_statement.
    def exitSql_statement(self, ctx:ora2epasParser.Sql_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#execute_immediate.
    def enterExecute_immediate(self, ctx:ora2epasParser.Execute_immediateContext):
        pass

    # Exit a parse tree produced by ora2epasParser#execute_immediate.
    def exitExecute_immediate(self, ctx:ora2epasParser.Execute_immediateContext):
        pass


    # Enter a parse tree produced by ora2epasParser#dynamic_returning_clause.
    def enterDynamic_returning_clause(self, ctx:ora2epasParser.Dynamic_returning_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#dynamic_returning_clause.
    def exitDynamic_returning_clause(self, ctx:ora2epasParser.Dynamic_returning_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sql_statements.
    def enterSql_statements(self, ctx:ora2epasParser.Sql_statementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sql_statements.
    def exitSql_statements(self, ctx:ora2epasParser.Sql_statementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cursor_manipulation_statements.
    def enterCursor_manipulation_statements(self, ctx:ora2epasParser.Cursor_manipulation_statementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cursor_manipulation_statements.
    def exitCursor_manipulation_statements(self, ctx:ora2epasParser.Cursor_manipulation_statementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#close_statement.
    def enterClose_statement(self, ctx:ora2epasParser.Close_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#close_statement.
    def exitClose_statement(self, ctx:ora2epasParser.Close_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#open_statement.
    def enterOpen_statement(self, ctx:ora2epasParser.Open_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#open_statement.
    def exitOpen_statement(self, ctx:ora2epasParser.Open_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#fetch_statement.
    def enterFetch_statement(self, ctx:ora2epasParser.Fetch_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#fetch_statement.
    def exitFetch_statement(self, ctx:ora2epasParser.Fetch_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#open_for_statement.
    def enterOpen_for_statement(self, ctx:ora2epasParser.Open_for_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#open_for_statement.
    def exitOpen_for_statement(self, ctx:ora2epasParser.Open_for_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#transaction_control_statements.
    def enterTransaction_control_statements(self, ctx:ora2epasParser.Transaction_control_statementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#transaction_control_statements.
    def exitTransaction_control_statements(self, ctx:ora2epasParser.Transaction_control_statementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#set_transaction_command.
    def enterSet_transaction_command(self, ctx:ora2epasParser.Set_transaction_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#set_transaction_command.
    def exitSet_transaction_command(self, ctx:ora2epasParser.Set_transaction_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#set_constraint_command.
    def enterSet_constraint_command(self, ctx:ora2epasParser.Set_constraint_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#set_constraint_command.
    def exitSet_constraint_command(self, ctx:ora2epasParser.Set_constraint_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#commit_statement.
    def enterCommit_statement(self, ctx:ora2epasParser.Commit_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#commit_statement.
    def exitCommit_statement(self, ctx:ora2epasParser.Commit_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#write_clause.
    def enterWrite_clause(self, ctx:ora2epasParser.Write_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#write_clause.
    def exitWrite_clause(self, ctx:ora2epasParser.Write_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#rollback_statement.
    def enterRollback_statement(self, ctx:ora2epasParser.Rollback_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#rollback_statement.
    def exitRollback_statement(self, ctx:ora2epasParser.Rollback_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#savepoint_statement.
    def enterSavepoint_statement(self, ctx:ora2epasParser.Savepoint_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#savepoint_statement.
    def exitSavepoint_statement(self, ctx:ora2epasParser.Savepoint_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#explain_statement.
    def enterExplain_statement(self, ctx:ora2epasParser.Explain_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#explain_statement.
    def exitExplain_statement(self, ctx:ora2epasParser.Explain_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#select_statement.
    def enterSelect_statement(self, ctx:ora2epasParser.Select_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#select_statement.
    def exitSelect_statement(self, ctx:ora2epasParser.Select_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subquery_factoring_clause.
    def enterSubquery_factoring_clause(self, ctx:ora2epasParser.Subquery_factoring_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subquery_factoring_clause.
    def exitSubquery_factoring_clause(self, ctx:ora2epasParser.Subquery_factoring_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#factoring_element.
    def enterFactoring_element(self, ctx:ora2epasParser.Factoring_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#factoring_element.
    def exitFactoring_element(self, ctx:ora2epasParser.Factoring_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#search_clause.
    def enterSearch_clause(self, ctx:ora2epasParser.Search_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#search_clause.
    def exitSearch_clause(self, ctx:ora2epasParser.Search_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cycle_clause.
    def enterCycle_clause(self, ctx:ora2epasParser.Cycle_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cycle_clause.
    def exitCycle_clause(self, ctx:ora2epasParser.Cycle_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subquery.
    def enterSubquery(self, ctx:ora2epasParser.SubqueryContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subquery.
    def exitSubquery(self, ctx:ora2epasParser.SubqueryContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subquery_operation_part.
    def enterSubquery_operation_part(self, ctx:ora2epasParser.Subquery_operation_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subquery_operation_part.
    def exitSubquery_operation_part(self, ctx:ora2epasParser.Subquery_operation_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subquery_basic_elements.
    def enterSubquery_basic_elements(self, ctx:ora2epasParser.Subquery_basic_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subquery_basic_elements.
    def exitSubquery_basic_elements(self, ctx:ora2epasParser.Subquery_basic_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#query_block.
    def enterQuery_block(self, ctx:ora2epasParser.Query_blockContext):
        pass

    # Exit a parse tree produced by ora2epasParser#query_block.
    def exitQuery_block(self, ctx:ora2epasParser.Query_blockContext):
        pass


    # Enter a parse tree produced by ora2epasParser#selected_element.
    def enterSelected_element(self, ctx:ora2epasParser.Selected_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#selected_element.
    def exitSelected_element(self, ctx:ora2epasParser.Selected_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#from_clause.
    def enterFrom_clause(self, ctx:ora2epasParser.From_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#from_clause.
    def exitFrom_clause(self, ctx:ora2epasParser.From_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#select_list_elements.
    def enterSelect_list_elements(self, ctx:ora2epasParser.Select_list_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#select_list_elements.
    def exitSelect_list_elements(self, ctx:ora2epasParser.Select_list_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_ref_list.
    def enterTable_ref_list(self, ctx:ora2epasParser.Table_ref_listContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_ref_list.
    def exitTable_ref_list(self, ctx:ora2epasParser.Table_ref_listContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_ref.
    def enterTable_ref(self, ctx:ora2epasParser.Table_refContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_ref.
    def exitTable_ref(self, ctx:ora2epasParser.Table_refContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_ref_aux.
    def enterTable_ref_aux(self, ctx:ora2epasParser.Table_ref_auxContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_ref_aux.
    def exitTable_ref_aux(self, ctx:ora2epasParser.Table_ref_auxContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_ref_aux_internal_one.
    def enterTable_ref_aux_internal_one(self, ctx:ora2epasParser.Table_ref_aux_internal_oneContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_ref_aux_internal_one.
    def exitTable_ref_aux_internal_one(self, ctx:ora2epasParser.Table_ref_aux_internal_oneContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_ref_aux_internal_two.
    def enterTable_ref_aux_internal_two(self, ctx:ora2epasParser.Table_ref_aux_internal_twoContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_ref_aux_internal_two.
    def exitTable_ref_aux_internal_two(self, ctx:ora2epasParser.Table_ref_aux_internal_twoContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_ref_aux_internal_three.
    def enterTable_ref_aux_internal_three(self, ctx:ora2epasParser.Table_ref_aux_internal_threeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_ref_aux_internal_three.
    def exitTable_ref_aux_internal_three(self, ctx:ora2epasParser.Table_ref_aux_internal_threeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#join_clause.
    def enterJoin_clause(self, ctx:ora2epasParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#join_clause.
    def exitJoin_clause(self, ctx:ora2epasParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#join_on_part.
    def enterJoin_on_part(self, ctx:ora2epasParser.Join_on_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#join_on_part.
    def exitJoin_on_part(self, ctx:ora2epasParser.Join_on_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#join_using_part.
    def enterJoin_using_part(self, ctx:ora2epasParser.Join_using_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#join_using_part.
    def exitJoin_using_part(self, ctx:ora2epasParser.Join_using_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#outer_join_type.
    def enterOuter_join_type(self, ctx:ora2epasParser.Outer_join_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#outer_join_type.
    def exitOuter_join_type(self, ctx:ora2epasParser.Outer_join_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#query_partition_clause.
    def enterQuery_partition_clause(self, ctx:ora2epasParser.Query_partition_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#query_partition_clause.
    def exitQuery_partition_clause(self, ctx:ora2epasParser.Query_partition_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#flashback_query_clause.
    def enterFlashback_query_clause(self, ctx:ora2epasParser.Flashback_query_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#flashback_query_clause.
    def exitFlashback_query_clause(self, ctx:ora2epasParser.Flashback_query_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pivot_clause.
    def enterPivot_clause(self, ctx:ora2epasParser.Pivot_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pivot_clause.
    def exitPivot_clause(self, ctx:ora2epasParser.Pivot_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pivot_element.
    def enterPivot_element(self, ctx:ora2epasParser.Pivot_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pivot_element.
    def exitPivot_element(self, ctx:ora2epasParser.Pivot_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pivot_for_clause.
    def enterPivot_for_clause(self, ctx:ora2epasParser.Pivot_for_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pivot_for_clause.
    def exitPivot_for_clause(self, ctx:ora2epasParser.Pivot_for_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pivot_in_clause.
    def enterPivot_in_clause(self, ctx:ora2epasParser.Pivot_in_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pivot_in_clause.
    def exitPivot_in_clause(self, ctx:ora2epasParser.Pivot_in_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pivot_in_clause_element.
    def enterPivot_in_clause_element(self, ctx:ora2epasParser.Pivot_in_clause_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pivot_in_clause_element.
    def exitPivot_in_clause_element(self, ctx:ora2epasParser.Pivot_in_clause_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#pivot_in_clause_elements.
    def enterPivot_in_clause_elements(self, ctx:ora2epasParser.Pivot_in_clause_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#pivot_in_clause_elements.
    def exitPivot_in_clause_elements(self, ctx:ora2epasParser.Pivot_in_clause_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#unpivot_clause.
    def enterUnpivot_clause(self, ctx:ora2epasParser.Unpivot_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#unpivot_clause.
    def exitUnpivot_clause(self, ctx:ora2epasParser.Unpivot_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#unpivot_in_clause.
    def enterUnpivot_in_clause(self, ctx:ora2epasParser.Unpivot_in_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#unpivot_in_clause.
    def exitUnpivot_in_clause(self, ctx:ora2epasParser.Unpivot_in_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#unpivot_in_elements.
    def enterUnpivot_in_elements(self, ctx:ora2epasParser.Unpivot_in_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#unpivot_in_elements.
    def exitUnpivot_in_elements(self, ctx:ora2epasParser.Unpivot_in_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#hierarchical_query_clause.
    def enterHierarchical_query_clause(self, ctx:ora2epasParser.Hierarchical_query_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#hierarchical_query_clause.
    def exitHierarchical_query_clause(self, ctx:ora2epasParser.Hierarchical_query_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#start_part.
    def enterStart_part(self, ctx:ora2epasParser.Start_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#start_part.
    def exitStart_part(self, ctx:ora2epasParser.Start_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:ora2epasParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:ora2epasParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#group_by_elements.
    def enterGroup_by_elements(self, ctx:ora2epasParser.Group_by_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#group_by_elements.
    def exitGroup_by_elements(self, ctx:ora2epasParser.Group_by_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#rollup_cube_clause.
    def enterRollup_cube_clause(self, ctx:ora2epasParser.Rollup_cube_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#rollup_cube_clause.
    def exitRollup_cube_clause(self, ctx:ora2epasParser.Rollup_cube_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#grouping_sets_clause.
    def enterGrouping_sets_clause(self, ctx:ora2epasParser.Grouping_sets_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#grouping_sets_clause.
    def exitGrouping_sets_clause(self, ctx:ora2epasParser.Grouping_sets_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#grouping_sets_elements.
    def enterGrouping_sets_elements(self, ctx:ora2epasParser.Grouping_sets_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#grouping_sets_elements.
    def exitGrouping_sets_elements(self, ctx:ora2epasParser.Grouping_sets_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#having_clause.
    def enterHaving_clause(self, ctx:ora2epasParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#having_clause.
    def exitHaving_clause(self, ctx:ora2epasParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_clause.
    def enterModel_clause(self, ctx:ora2epasParser.Model_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_clause.
    def exitModel_clause(self, ctx:ora2epasParser.Model_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cell_reference_options.
    def enterCell_reference_options(self, ctx:ora2epasParser.Cell_reference_optionsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cell_reference_options.
    def exitCell_reference_options(self, ctx:ora2epasParser.Cell_reference_optionsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#return_rows_clause.
    def enterReturn_rows_clause(self, ctx:ora2epasParser.Return_rows_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#return_rows_clause.
    def exitReturn_rows_clause(self, ctx:ora2epasParser.Return_rows_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#reference_model.
    def enterReference_model(self, ctx:ora2epasParser.Reference_modelContext):
        pass

    # Exit a parse tree produced by ora2epasParser#reference_model.
    def exitReference_model(self, ctx:ora2epasParser.Reference_modelContext):
        pass


    # Enter a parse tree produced by ora2epasParser#main_model.
    def enterMain_model(self, ctx:ora2epasParser.Main_modelContext):
        pass

    # Exit a parse tree produced by ora2epasParser#main_model.
    def exitMain_model(self, ctx:ora2epasParser.Main_modelContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_column_clauses.
    def enterModel_column_clauses(self, ctx:ora2epasParser.Model_column_clausesContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_column_clauses.
    def exitModel_column_clauses(self, ctx:ora2epasParser.Model_column_clausesContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_column_partition_part.
    def enterModel_column_partition_part(self, ctx:ora2epasParser.Model_column_partition_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_column_partition_part.
    def exitModel_column_partition_part(self, ctx:ora2epasParser.Model_column_partition_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_column_list.
    def enterModel_column_list(self, ctx:ora2epasParser.Model_column_listContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_column_list.
    def exitModel_column_list(self, ctx:ora2epasParser.Model_column_listContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_column.
    def enterModel_column(self, ctx:ora2epasParser.Model_columnContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_column.
    def exitModel_column(self, ctx:ora2epasParser.Model_columnContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_rules_clause.
    def enterModel_rules_clause(self, ctx:ora2epasParser.Model_rules_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_rules_clause.
    def exitModel_rules_clause(self, ctx:ora2epasParser.Model_rules_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_rules_part.
    def enterModel_rules_part(self, ctx:ora2epasParser.Model_rules_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_rules_part.
    def exitModel_rules_part(self, ctx:ora2epasParser.Model_rules_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_rules_element.
    def enterModel_rules_element(self, ctx:ora2epasParser.Model_rules_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_rules_element.
    def exitModel_rules_element(self, ctx:ora2epasParser.Model_rules_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cell_assignment.
    def enterCell_assignment(self, ctx:ora2epasParser.Cell_assignmentContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cell_assignment.
    def exitCell_assignment(self, ctx:ora2epasParser.Cell_assignmentContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_iterate_clause.
    def enterModel_iterate_clause(self, ctx:ora2epasParser.Model_iterate_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_iterate_clause.
    def exitModel_iterate_clause(self, ctx:ora2epasParser.Model_iterate_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#until_part.
    def enterUntil_part(self, ctx:ora2epasParser.Until_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#until_part.
    def exitUntil_part(self, ctx:ora2epasParser.Until_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:ora2epasParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:ora2epasParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#order_by_elements.
    def enterOrder_by_elements(self, ctx:ora2epasParser.Order_by_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#order_by_elements.
    def exitOrder_by_elements(self, ctx:ora2epasParser.Order_by_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#for_update_clause.
    def enterFor_update_clause(self, ctx:ora2epasParser.For_update_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#for_update_clause.
    def exitFor_update_clause(self, ctx:ora2epasParser.For_update_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#for_update_of_part.
    def enterFor_update_of_part(self, ctx:ora2epasParser.For_update_of_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#for_update_of_part.
    def exitFor_update_of_part(self, ctx:ora2epasParser.For_update_of_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#for_update_options.
    def enterFor_update_options(self, ctx:ora2epasParser.For_update_optionsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#for_update_options.
    def exitFor_update_options(self, ctx:ora2epasParser.For_update_optionsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#update_statement.
    def enterUpdate_statement(self, ctx:ora2epasParser.Update_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#update_statement.
    def exitUpdate_statement(self, ctx:ora2epasParser.Update_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#update_set_clause.
    def enterUpdate_set_clause(self, ctx:ora2epasParser.Update_set_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#update_set_clause.
    def exitUpdate_set_clause(self, ctx:ora2epasParser.Update_set_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#column_based_update_set_clause.
    def enterColumn_based_update_set_clause(self, ctx:ora2epasParser.Column_based_update_set_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#column_based_update_set_clause.
    def exitColumn_based_update_set_clause(self, ctx:ora2epasParser.Column_based_update_set_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#delete_statement.
    def enterDelete_statement(self, ctx:ora2epasParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#delete_statement.
    def exitDelete_statement(self, ctx:ora2epasParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#insert_statement.
    def enterInsert_statement(self, ctx:ora2epasParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#insert_statement.
    def exitInsert_statement(self, ctx:ora2epasParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#single_table_insert.
    def enterSingle_table_insert(self, ctx:ora2epasParser.Single_table_insertContext):
        pass

    # Exit a parse tree produced by ora2epasParser#single_table_insert.
    def exitSingle_table_insert(self, ctx:ora2epasParser.Single_table_insertContext):
        pass


    # Enter a parse tree produced by ora2epasParser#multi_table_insert.
    def enterMulti_table_insert(self, ctx:ora2epasParser.Multi_table_insertContext):
        pass

    # Exit a parse tree produced by ora2epasParser#multi_table_insert.
    def exitMulti_table_insert(self, ctx:ora2epasParser.Multi_table_insertContext):
        pass


    # Enter a parse tree produced by ora2epasParser#multi_table_element.
    def enterMulti_table_element(self, ctx:ora2epasParser.Multi_table_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#multi_table_element.
    def exitMulti_table_element(self, ctx:ora2epasParser.Multi_table_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#conditional_insert_clause.
    def enterConditional_insert_clause(self, ctx:ora2epasParser.Conditional_insert_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#conditional_insert_clause.
    def exitConditional_insert_clause(self, ctx:ora2epasParser.Conditional_insert_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#conditional_insert_when_part.
    def enterConditional_insert_when_part(self, ctx:ora2epasParser.Conditional_insert_when_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#conditional_insert_when_part.
    def exitConditional_insert_when_part(self, ctx:ora2epasParser.Conditional_insert_when_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#conditional_insert_else_part.
    def enterConditional_insert_else_part(self, ctx:ora2epasParser.Conditional_insert_else_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#conditional_insert_else_part.
    def exitConditional_insert_else_part(self, ctx:ora2epasParser.Conditional_insert_else_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#insert_into_clause.
    def enterInsert_into_clause(self, ctx:ora2epasParser.Insert_into_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#insert_into_clause.
    def exitInsert_into_clause(self, ctx:ora2epasParser.Insert_into_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#values_clause.
    def enterValues_clause(self, ctx:ora2epasParser.Values_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#values_clause.
    def exitValues_clause(self, ctx:ora2epasParser.Values_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#merge_statement.
    def enterMerge_statement(self, ctx:ora2epasParser.Merge_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#merge_statement.
    def exitMerge_statement(self, ctx:ora2epasParser.Merge_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#merge_update_clause.
    def enterMerge_update_clause(self, ctx:ora2epasParser.Merge_update_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#merge_update_clause.
    def exitMerge_update_clause(self, ctx:ora2epasParser.Merge_update_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#merge_element.
    def enterMerge_element(self, ctx:ora2epasParser.Merge_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#merge_element.
    def exitMerge_element(self, ctx:ora2epasParser.Merge_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#merge_update_delete_part.
    def enterMerge_update_delete_part(self, ctx:ora2epasParser.Merge_update_delete_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#merge_update_delete_part.
    def exitMerge_update_delete_part(self, ctx:ora2epasParser.Merge_update_delete_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#merge_insert_clause.
    def enterMerge_insert_clause(self, ctx:ora2epasParser.Merge_insert_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#merge_insert_clause.
    def exitMerge_insert_clause(self, ctx:ora2epasParser.Merge_insert_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#selected_tableview.
    def enterSelected_tableview(self, ctx:ora2epasParser.Selected_tableviewContext):
        pass

    # Exit a parse tree produced by ora2epasParser#selected_tableview.
    def exitSelected_tableview(self, ctx:ora2epasParser.Selected_tableviewContext):
        pass


    # Enter a parse tree produced by ora2epasParser#lock_table_statement.
    def enterLock_table_statement(self, ctx:ora2epasParser.Lock_table_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#lock_table_statement.
    def exitLock_table_statement(self, ctx:ora2epasParser.Lock_table_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#wait_nowait_part.
    def enterWait_nowait_part(self, ctx:ora2epasParser.Wait_nowait_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#wait_nowait_part.
    def exitWait_nowait_part(self, ctx:ora2epasParser.Wait_nowait_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#lock_table_element.
    def enterLock_table_element(self, ctx:ora2epasParser.Lock_table_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#lock_table_element.
    def exitLock_table_element(self, ctx:ora2epasParser.Lock_table_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#lock_mode.
    def enterLock_mode(self, ctx:ora2epasParser.Lock_modeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#lock_mode.
    def exitLock_mode(self, ctx:ora2epasParser.Lock_modeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#general_table_ref.
    def enterGeneral_table_ref(self, ctx:ora2epasParser.General_table_refContext):
        pass

    # Exit a parse tree produced by ora2epasParser#general_table_ref.
    def exitGeneral_table_ref(self, ctx:ora2epasParser.General_table_refContext):
        pass


    # Enter a parse tree produced by ora2epasParser#static_returning_clause.
    def enterStatic_returning_clause(self, ctx:ora2epasParser.Static_returning_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#static_returning_clause.
    def exitStatic_returning_clause(self, ctx:ora2epasParser.Static_returning_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#error_logging_clause.
    def enterError_logging_clause(self, ctx:ora2epasParser.Error_logging_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#error_logging_clause.
    def exitError_logging_clause(self, ctx:ora2epasParser.Error_logging_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#error_logging_into_part.
    def enterError_logging_into_part(self, ctx:ora2epasParser.Error_logging_into_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#error_logging_into_part.
    def exitError_logging_into_part(self, ctx:ora2epasParser.Error_logging_into_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#error_logging_reject_part.
    def enterError_logging_reject_part(self, ctx:ora2epasParser.Error_logging_reject_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#error_logging_reject_part.
    def exitError_logging_reject_part(self, ctx:ora2epasParser.Error_logging_reject_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#dml_table_expression_clause.
    def enterDml_table_expression_clause(self, ctx:ora2epasParser.Dml_table_expression_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#dml_table_expression_clause.
    def exitDml_table_expression_clause(self, ctx:ora2epasParser.Dml_table_expression_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_collection_expression.
    def enterTable_collection_expression(self, ctx:ora2epasParser.Table_collection_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_collection_expression.
    def exitTable_collection_expression(self, ctx:ora2epasParser.Table_collection_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#subquery_restriction_clause.
    def enterSubquery_restriction_clause(self, ctx:ora2epasParser.Subquery_restriction_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#subquery_restriction_clause.
    def exitSubquery_restriction_clause(self, ctx:ora2epasParser.Subquery_restriction_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sample_clause.
    def enterSample_clause(self, ctx:ora2epasParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sample_clause.
    def exitSample_clause(self, ctx:ora2epasParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#seed_part.
    def enterSeed_part(self, ctx:ora2epasParser.Seed_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#seed_part.
    def exitSeed_part(self, ctx:ora2epasParser.Seed_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cursor_expression.
    def enterCursor_expression(self, ctx:ora2epasParser.Cursor_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cursor_expression.
    def exitCursor_expression(self, ctx:ora2epasParser.Cursor_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#expression_list.
    def enterExpression_list(self, ctx:ora2epasParser.Expression_listContext):
        pass

    # Exit a parse tree produced by ora2epasParser#expression_list.
    def exitExpression_list(self, ctx:ora2epasParser.Expression_listContext):
        pass


    # Enter a parse tree produced by ora2epasParser#condition.
    def enterCondition(self, ctx:ora2epasParser.ConditionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#condition.
    def exitCondition(self, ctx:ora2epasParser.ConditionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#expression.
    def enterExpression(self, ctx:ora2epasParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#expression.
    def exitExpression(self, ctx:ora2epasParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#logical_or_expression.
    def enterLogical_or_expression(self, ctx:ora2epasParser.Logical_or_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#logical_or_expression.
    def exitLogical_or_expression(self, ctx:ora2epasParser.Logical_or_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#logical_and_expression.
    def enterLogical_and_expression(self, ctx:ora2epasParser.Logical_and_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#logical_and_expression.
    def exitLogical_and_expression(self, ctx:ora2epasParser.Logical_and_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#negated_expression.
    def enterNegated_expression(self, ctx:ora2epasParser.Negated_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#negated_expression.
    def exitNegated_expression(self, ctx:ora2epasParser.Negated_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#equality_expression.
    def enterEquality_expression(self, ctx:ora2epasParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#equality_expression.
    def exitEquality_expression(self, ctx:ora2epasParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#multiset_expression.
    def enterMultiset_expression(self, ctx:ora2epasParser.Multiset_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#multiset_expression.
    def exitMultiset_expression(self, ctx:ora2epasParser.Multiset_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#multiset_type.
    def enterMultiset_type(self, ctx:ora2epasParser.Multiset_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#multiset_type.
    def exitMultiset_type(self, ctx:ora2epasParser.Multiset_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#relational_expression.
    def enterRelational_expression(self, ctx:ora2epasParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#relational_expression.
    def exitRelational_expression(self, ctx:ora2epasParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#compound_expression.
    def enterCompound_expression(self, ctx:ora2epasParser.Compound_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#compound_expression.
    def exitCompound_expression(self, ctx:ora2epasParser.Compound_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#relational_operator.
    def enterRelational_operator(self, ctx:ora2epasParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by ora2epasParser#relational_operator.
    def exitRelational_operator(self, ctx:ora2epasParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by ora2epasParser#like_type.
    def enterLike_type(self, ctx:ora2epasParser.Like_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#like_type.
    def exitLike_type(self, ctx:ora2epasParser.Like_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#like_escape_part.
    def enterLike_escape_part(self, ctx:ora2epasParser.Like_escape_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#like_escape_part.
    def exitLike_escape_part(self, ctx:ora2epasParser.Like_escape_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#in_elements.
    def enterIn_elements(self, ctx:ora2epasParser.In_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#in_elements.
    def exitIn_elements(self, ctx:ora2epasParser.In_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#between_elements.
    def enterBetween_elements(self, ctx:ora2epasParser.Between_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#between_elements.
    def exitBetween_elements(self, ctx:ora2epasParser.Between_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#concatenation.
    def enterConcatenation(self, ctx:ora2epasParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by ora2epasParser#concatenation.
    def exitConcatenation(self, ctx:ora2epasParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by ora2epasParser#additive_expression.
    def enterAdditive_expression(self, ctx:ora2epasParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#additive_expression.
    def exitAdditive_expression(self, ctx:ora2epasParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#multiply_expression.
    def enterMultiply_expression(self, ctx:ora2epasParser.Multiply_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#multiply_expression.
    def exitMultiply_expression(self, ctx:ora2epasParser.Multiply_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#datetime_expression.
    def enterDatetime_expression(self, ctx:ora2epasParser.Datetime_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#datetime_expression.
    def exitDatetime_expression(self, ctx:ora2epasParser.Datetime_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#interval_expression.
    def enterInterval_expression(self, ctx:ora2epasParser.Interval_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#interval_expression.
    def exitInterval_expression(self, ctx:ora2epasParser.Interval_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_expression.
    def enterModel_expression(self, ctx:ora2epasParser.Model_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_expression.
    def exitModel_expression(self, ctx:ora2epasParser.Model_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#model_expression_element.
    def enterModel_expression_element(self, ctx:ora2epasParser.Model_expression_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#model_expression_element.
    def exitModel_expression_element(self, ctx:ora2epasParser.Model_expression_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#single_column_for_loop.
    def enterSingle_column_for_loop(self, ctx:ora2epasParser.Single_column_for_loopContext):
        pass

    # Exit a parse tree produced by ora2epasParser#single_column_for_loop.
    def exitSingle_column_for_loop(self, ctx:ora2epasParser.Single_column_for_loopContext):
        pass


    # Enter a parse tree produced by ora2epasParser#for_like_part.
    def enterFor_like_part(self, ctx:ora2epasParser.For_like_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#for_like_part.
    def exitFor_like_part(self, ctx:ora2epasParser.For_like_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#for_increment_decrement_type.
    def enterFor_increment_decrement_type(self, ctx:ora2epasParser.For_increment_decrement_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#for_increment_decrement_type.
    def exitFor_increment_decrement_type(self, ctx:ora2epasParser.For_increment_decrement_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#multi_column_for_loop.
    def enterMulti_column_for_loop(self, ctx:ora2epasParser.Multi_column_for_loopContext):
        pass

    # Exit a parse tree produced by ora2epasParser#multi_column_for_loop.
    def exitMulti_column_for_loop(self, ctx:ora2epasParser.Multi_column_for_loopContext):
        pass


    # Enter a parse tree produced by ora2epasParser#unary_expression.
    def enterUnary_expression(self, ctx:ora2epasParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#unary_expression.
    def exitUnary_expression(self, ctx:ora2epasParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#case_statement.
    def enterCase_statement(self, ctx:ora2epasParser.Case_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#case_statement.
    def exitCase_statement(self, ctx:ora2epasParser.Case_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#simple_case_statement.
    def enterSimple_case_statement(self, ctx:ora2epasParser.Simple_case_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#simple_case_statement.
    def exitSimple_case_statement(self, ctx:ora2epasParser.Simple_case_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#simple_case_when_part.
    def enterSimple_case_when_part(self, ctx:ora2epasParser.Simple_case_when_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#simple_case_when_part.
    def exitSimple_case_when_part(self, ctx:ora2epasParser.Simple_case_when_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#searched_case_statement.
    def enterSearched_case_statement(self, ctx:ora2epasParser.Searched_case_statementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#searched_case_statement.
    def exitSearched_case_statement(self, ctx:ora2epasParser.Searched_case_statementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#searched_case_when_part.
    def enterSearched_case_when_part(self, ctx:ora2epasParser.Searched_case_when_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#searched_case_when_part.
    def exitSearched_case_when_part(self, ctx:ora2epasParser.Searched_case_when_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#case_else_part.
    def enterCase_else_part(self, ctx:ora2epasParser.Case_else_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#case_else_part.
    def exitCase_else_part(self, ctx:ora2epasParser.Case_else_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#atom.
    def enterAtom(self, ctx:ora2epasParser.AtomContext):
        pass

    # Exit a parse tree produced by ora2epasParser#atom.
    def exitAtom(self, ctx:ora2epasParser.AtomContext):
        pass


    # Enter a parse tree produced by ora2epasParser#expression_or_vector.
    def enterExpression_or_vector(self, ctx:ora2epasParser.Expression_or_vectorContext):
        pass

    # Exit a parse tree produced by ora2epasParser#expression_or_vector.
    def exitExpression_or_vector(self, ctx:ora2epasParser.Expression_or_vectorContext):
        pass


    # Enter a parse tree produced by ora2epasParser#vector_expr.
    def enterVector_expr(self, ctx:ora2epasParser.Vector_exprContext):
        pass

    # Exit a parse tree produced by ora2epasParser#vector_expr.
    def exitVector_expr(self, ctx:ora2epasParser.Vector_exprContext):
        pass


    # Enter a parse tree produced by ora2epasParser#quantified_expression.
    def enterQuantified_expression(self, ctx:ora2epasParser.Quantified_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#quantified_expression.
    def exitQuantified_expression(self, ctx:ora2epasParser.Quantified_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#string_function.
    def enterString_function(self, ctx:ora2epasParser.String_functionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#string_function.
    def exitString_function(self, ctx:ora2epasParser.String_functionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#standard_function.
    def enterStandard_function(self, ctx:ora2epasParser.Standard_functionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#standard_function.
    def exitStandard_function(self, ctx:ora2epasParser.Standard_functionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#numeric_function_wrapper.
    def enterNumeric_function_wrapper(self, ctx:ora2epasParser.Numeric_function_wrapperContext):
        pass

    # Exit a parse tree produced by ora2epasParser#numeric_function_wrapper.
    def exitNumeric_function_wrapper(self, ctx:ora2epasParser.Numeric_function_wrapperContext):
        pass


    # Enter a parse tree produced by ora2epasParser#numeric_function.
    def enterNumeric_function(self, ctx:ora2epasParser.Numeric_functionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#numeric_function.
    def exitNumeric_function(self, ctx:ora2epasParser.Numeric_functionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#other_function.
    def enterOther_function(self, ctx:ora2epasParser.Other_functionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#other_function.
    def exitOther_function(self, ctx:ora2epasParser.Other_functionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#over_clause_keyword.
    def enterOver_clause_keyword(self, ctx:ora2epasParser.Over_clause_keywordContext):
        pass

    # Exit a parse tree produced by ora2epasParser#over_clause_keyword.
    def exitOver_clause_keyword(self, ctx:ora2epasParser.Over_clause_keywordContext):
        pass


    # Enter a parse tree produced by ora2epasParser#within_or_over_clause_keyword.
    def enterWithin_or_over_clause_keyword(self, ctx:ora2epasParser.Within_or_over_clause_keywordContext):
        pass

    # Exit a parse tree produced by ora2epasParser#within_or_over_clause_keyword.
    def exitWithin_or_over_clause_keyword(self, ctx:ora2epasParser.Within_or_over_clause_keywordContext):
        pass


    # Enter a parse tree produced by ora2epasParser#standard_prediction_function_keyword.
    def enterStandard_prediction_function_keyword(self, ctx:ora2epasParser.Standard_prediction_function_keywordContext):
        pass

    # Exit a parse tree produced by ora2epasParser#standard_prediction_function_keyword.
    def exitStandard_prediction_function_keyword(self, ctx:ora2epasParser.Standard_prediction_function_keywordContext):
        pass


    # Enter a parse tree produced by ora2epasParser#over_clause.
    def enterOver_clause(self, ctx:ora2epasParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#over_clause.
    def exitOver_clause(self, ctx:ora2epasParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#windowing_clause.
    def enterWindowing_clause(self, ctx:ora2epasParser.Windowing_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#windowing_clause.
    def exitWindowing_clause(self, ctx:ora2epasParser.Windowing_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#windowing_type.
    def enterWindowing_type(self, ctx:ora2epasParser.Windowing_typeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#windowing_type.
    def exitWindowing_type(self, ctx:ora2epasParser.Windowing_typeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#windowing_elements.
    def enterWindowing_elements(self, ctx:ora2epasParser.Windowing_elementsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#windowing_elements.
    def exitWindowing_elements(self, ctx:ora2epasParser.Windowing_elementsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#using_clause.
    def enterUsing_clause(self, ctx:ora2epasParser.Using_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#using_clause.
    def exitUsing_clause(self, ctx:ora2epasParser.Using_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#using_element.
    def enterUsing_element(self, ctx:ora2epasParser.Using_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#using_element.
    def exitUsing_element(self, ctx:ora2epasParser.Using_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#collect_order_by_part.
    def enterCollect_order_by_part(self, ctx:ora2epasParser.Collect_order_by_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#collect_order_by_part.
    def exitCollect_order_by_part(self, ctx:ora2epasParser.Collect_order_by_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#within_or_over_part.
    def enterWithin_or_over_part(self, ctx:ora2epasParser.Within_or_over_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#within_or_over_part.
    def exitWithin_or_over_part(self, ctx:ora2epasParser.Within_or_over_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cost_matrix_clause.
    def enterCost_matrix_clause(self, ctx:ora2epasParser.Cost_matrix_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cost_matrix_clause.
    def exitCost_matrix_clause(self, ctx:ora2epasParser.Cost_matrix_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xml_passing_clause.
    def enterXml_passing_clause(self, ctx:ora2epasParser.Xml_passing_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xml_passing_clause.
    def exitXml_passing_clause(self, ctx:ora2epasParser.Xml_passing_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xml_attributes_clause.
    def enterXml_attributes_clause(self, ctx:ora2epasParser.Xml_attributes_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xml_attributes_clause.
    def exitXml_attributes_clause(self, ctx:ora2epasParser.Xml_attributes_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xml_namespaces_clause.
    def enterXml_namespaces_clause(self, ctx:ora2epasParser.Xml_namespaces_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xml_namespaces_clause.
    def exitXml_namespaces_clause(self, ctx:ora2epasParser.Xml_namespaces_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xml_table_column.
    def enterXml_table_column(self, ctx:ora2epasParser.Xml_table_columnContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xml_table_column.
    def exitXml_table_column(self, ctx:ora2epasParser.Xml_table_columnContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xml_general_default_part.
    def enterXml_general_default_part(self, ctx:ora2epasParser.Xml_general_default_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xml_general_default_part.
    def exitXml_general_default_part(self, ctx:ora2epasParser.Xml_general_default_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xml_multiuse_expression_element.
    def enterXml_multiuse_expression_element(self, ctx:ora2epasParser.Xml_multiuse_expression_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xml_multiuse_expression_element.
    def exitXml_multiuse_expression_element(self, ctx:ora2epasParser.Xml_multiuse_expression_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xmlroot_param_version_part.
    def enterXmlroot_param_version_part(self, ctx:ora2epasParser.Xmlroot_param_version_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xmlroot_param_version_part.
    def exitXmlroot_param_version_part(self, ctx:ora2epasParser.Xmlroot_param_version_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xmlroot_param_standalone_part.
    def enterXmlroot_param_standalone_part(self, ctx:ora2epasParser.Xmlroot_param_standalone_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xmlroot_param_standalone_part.
    def exitXmlroot_param_standalone_part(self, ctx:ora2epasParser.Xmlroot_param_standalone_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xmlserialize_param_enconding_part.
    def enterXmlserialize_param_enconding_part(self, ctx:ora2epasParser.Xmlserialize_param_enconding_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xmlserialize_param_enconding_part.
    def exitXmlserialize_param_enconding_part(self, ctx:ora2epasParser.Xmlserialize_param_enconding_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xmlserialize_param_version_part.
    def enterXmlserialize_param_version_part(self, ctx:ora2epasParser.Xmlserialize_param_version_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xmlserialize_param_version_part.
    def exitXmlserialize_param_version_part(self, ctx:ora2epasParser.Xmlserialize_param_version_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xmlserialize_param_ident_part.
    def enterXmlserialize_param_ident_part(self, ctx:ora2epasParser.Xmlserialize_param_ident_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xmlserialize_param_ident_part.
    def exitXmlserialize_param_ident_part(self, ctx:ora2epasParser.Xmlserialize_param_ident_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sql_plus_command.
    def enterSql_plus_command(self, ctx:ora2epasParser.Sql_plus_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sql_plus_command.
    def exitSql_plus_command(self, ctx:ora2epasParser.Sql_plus_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#whenever_command.
    def enterWhenever_command(self, ctx:ora2epasParser.Whenever_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#whenever_command.
    def exitWhenever_command(self, ctx:ora2epasParser.Whenever_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#set_command.
    def enterSet_command(self, ctx:ora2epasParser.Set_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#set_command.
    def exitSet_command(self, ctx:ora2epasParser.Set_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#exit_command.
    def enterExit_command(self, ctx:ora2epasParser.Exit_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#exit_command.
    def exitExit_command(self, ctx:ora2epasParser.Exit_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#prompt_command.
    def enterPrompt_command(self, ctx:ora2epasParser.Prompt_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#prompt_command.
    def exitPrompt_command(self, ctx:ora2epasParser.Prompt_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#show_errors_command.
    def enterShow_errors_command(self, ctx:ora2epasParser.Show_errors_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#show_errors_command.
    def exitShow_errors_command(self, ctx:ora2epasParser.Show_errors_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#start_command.
    def enterStart_command(self, ctx:ora2epasParser.Start_commandContext):
        pass

    # Exit a parse tree produced by ora2epasParser#start_command.
    def exitStart_command(self, ctx:ora2epasParser.Start_commandContext):
        pass


    # Enter a parse tree produced by ora2epasParser#partition_extension_clause.
    def enterPartition_extension_clause(self, ctx:ora2epasParser.Partition_extension_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#partition_extension_clause.
    def exitPartition_extension_clause(self, ctx:ora2epasParser.Partition_extension_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#column_alias.
    def enterColumn_alias(self, ctx:ora2epasParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by ora2epasParser#column_alias.
    def exitColumn_alias(self, ctx:ora2epasParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_alias.
    def enterTable_alias(self, ctx:ora2epasParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_alias.
    def exitTable_alias(self, ctx:ora2epasParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by ora2epasParser#alias_quoted_string.
    def enterAlias_quoted_string(self, ctx:ora2epasParser.Alias_quoted_stringContext):
        pass

    # Exit a parse tree produced by ora2epasParser#alias_quoted_string.
    def exitAlias_quoted_string(self, ctx:ora2epasParser.Alias_quoted_stringContext):
        pass


    # Enter a parse tree produced by ora2epasParser#where_clause.
    def enterWhere_clause(self, ctx:ora2epasParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#where_clause.
    def exitWhere_clause(self, ctx:ora2epasParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#current_of_clause.
    def enterCurrent_of_clause(self, ctx:ora2epasParser.Current_of_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#current_of_clause.
    def exitCurrent_of_clause(self, ctx:ora2epasParser.Current_of_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#into_clause.
    def enterInto_clause(self, ctx:ora2epasParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#into_clause.
    def exitInto_clause(self, ctx:ora2epasParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#xml_column_name.
    def enterXml_column_name(self, ctx:ora2epasParser.Xml_column_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#xml_column_name.
    def exitXml_column_name(self, ctx:ora2epasParser.Xml_column_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cost_class_name.
    def enterCost_class_name(self, ctx:ora2epasParser.Cost_class_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cost_class_name.
    def exitCost_class_name(self, ctx:ora2epasParser.Cost_class_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#attribute_name.
    def enterAttribute_name(self, ctx:ora2epasParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#attribute_name.
    def exitAttribute_name(self, ctx:ora2epasParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#savepoint_name.
    def enterSavepoint_name(self, ctx:ora2epasParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#savepoint_name.
    def exitSavepoint_name(self, ctx:ora2epasParser.Savepoint_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#rollback_segment_name.
    def enterRollback_segment_name(self, ctx:ora2epasParser.Rollback_segment_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#rollback_segment_name.
    def exitRollback_segment_name(self, ctx:ora2epasParser.Rollback_segment_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_var_name.
    def enterTable_var_name(self, ctx:ora2epasParser.Table_var_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_var_name.
    def exitTable_var_name(self, ctx:ora2epasParser.Table_var_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#schema_name.
    def enterSchema_name(self, ctx:ora2epasParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#schema_name.
    def exitSchema_name(self, ctx:ora2epasParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#routine_name.
    def enterRoutine_name(self, ctx:ora2epasParser.Routine_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#routine_name.
    def exitRoutine_name(self, ctx:ora2epasParser.Routine_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#package_name.
    def enterPackage_name(self, ctx:ora2epasParser.Package_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#package_name.
    def exitPackage_name(self, ctx:ora2epasParser.Package_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#implementation_type_name.
    def enterImplementation_type_name(self, ctx:ora2epasParser.Implementation_type_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#implementation_type_name.
    def exitImplementation_type_name(self, ctx:ora2epasParser.Implementation_type_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#parameter_name.
    def enterParameter_name(self, ctx:ora2epasParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#parameter_name.
    def exitParameter_name(self, ctx:ora2epasParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#reference_model_name.
    def enterReference_model_name(self, ctx:ora2epasParser.Reference_model_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#reference_model_name.
    def exitReference_model_name(self, ctx:ora2epasParser.Reference_model_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#main_model_name.
    def enterMain_model_name(self, ctx:ora2epasParser.Main_model_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#main_model_name.
    def exitMain_model_name(self, ctx:ora2epasParser.Main_model_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#aggregate_function_name.
    def enterAggregate_function_name(self, ctx:ora2epasParser.Aggregate_function_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#aggregate_function_name.
    def exitAggregate_function_name(self, ctx:ora2epasParser.Aggregate_function_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#query_name.
    def enterQuery_name(self, ctx:ora2epasParser.Query_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#query_name.
    def exitQuery_name(self, ctx:ora2epasParser.Query_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#constraint_name.
    def enterConstraint_name(self, ctx:ora2epasParser.Constraint_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#constraint_name.
    def exitConstraint_name(self, ctx:ora2epasParser.Constraint_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#label_name.
    def enterLabel_name(self, ctx:ora2epasParser.Label_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#label_name.
    def exitLabel_name(self, ctx:ora2epasParser.Label_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_name.
    def enterType_name(self, ctx:ora2epasParser.Type_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_name.
    def exitType_name(self, ctx:ora2epasParser.Type_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#sequence_name.
    def enterSequence_name(self, ctx:ora2epasParser.Sequence_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#sequence_name.
    def exitSequence_name(self, ctx:ora2epasParser.Sequence_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#exception_name.
    def enterException_name(self, ctx:ora2epasParser.Exception_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#exception_name.
    def exitException_name(self, ctx:ora2epasParser.Exception_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#view_name.
    def enterView_name(self, ctx:ora2epasParser.View_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#view_name.
    def exitView_name(self, ctx:ora2epasParser.View_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#mview_name.
    def enterMview_name(self, ctx:ora2epasParser.Mview_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#mview_name.
    def exitMview_name(self, ctx:ora2epasParser.Mview_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#dblink_name.
    def enterDblink_name(self, ctx:ora2epasParser.Dblink_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#dblink_name.
    def exitDblink_name(self, ctx:ora2epasParser.Dblink_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#function_name.
    def enterFunction_name(self, ctx:ora2epasParser.Function_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#function_name.
    def exitFunction_name(self, ctx:ora2epasParser.Function_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#procedure_name.
    def enterProcedure_name(self, ctx:ora2epasParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#procedure_name.
    def exitProcedure_name(self, ctx:ora2epasParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#trigger_name.
    def enterTrigger_name(self, ctx:ora2epasParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#trigger_name.
    def exitTrigger_name(self, ctx:ora2epasParser.Trigger_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#variable_name.
    def enterVariable_name(self, ctx:ora2epasParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#variable_name.
    def exitVariable_name(self, ctx:ora2epasParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#index_name.
    def enterIndex_name(self, ctx:ora2epasParser.Index_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#index_name.
    def exitIndex_name(self, ctx:ora2epasParser.Index_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#cursor_name.
    def enterCursor_name(self, ctx:ora2epasParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#cursor_name.
    def exitCursor_name(self, ctx:ora2epasParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#record_name.
    def enterRecord_name(self, ctx:ora2epasParser.Record_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#record_name.
    def exitRecord_name(self, ctx:ora2epasParser.Record_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#collection_name.
    def enterCollection_name(self, ctx:ora2epasParser.Collection_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#collection_name.
    def exitCollection_name(self, ctx:ora2epasParser.Collection_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#link_name.
    def enterLink_name(self, ctx:ora2epasParser.Link_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#link_name.
    def exitLink_name(self, ctx:ora2epasParser.Link_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#column_name.
    def enterColumn_name(self, ctx:ora2epasParser.Column_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#column_name.
    def exitColumn_name(self, ctx:ora2epasParser.Column_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#tableview_name.
    def enterTableview_name(self, ctx:ora2epasParser.Tableview_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#tableview_name.
    def exitTableview_name(self, ctx:ora2epasParser.Tableview_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#char_set_name.
    def enterChar_set_name(self, ctx:ora2epasParser.Char_set_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#char_set_name.
    def exitChar_set_name(self, ctx:ora2epasParser.Char_set_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#synonym_name.
    def enterSynonym_name(self, ctx:ora2epasParser.Synonym_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#synonym_name.
    def exitSynonym_name(self, ctx:ora2epasParser.Synonym_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#schema_object_name.
    def enterSchema_object_name(self, ctx:ora2epasParser.Schema_object_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#schema_object_name.
    def exitSchema_object_name(self, ctx:ora2epasParser.Schema_object_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#keep_clause.
    def enterKeep_clause(self, ctx:ora2epasParser.Keep_clauseContext):
        pass

    # Exit a parse tree produced by ora2epasParser#keep_clause.
    def exitKeep_clause(self, ctx:ora2epasParser.Keep_clauseContext):
        pass


    # Enter a parse tree produced by ora2epasParser#function_argument.
    def enterFunction_argument(self, ctx:ora2epasParser.Function_argumentContext):
        pass

    # Exit a parse tree produced by ora2epasParser#function_argument.
    def exitFunction_argument(self, ctx:ora2epasParser.Function_argumentContext):
        pass


    # Enter a parse tree produced by ora2epasParser#function_argument_analytic.
    def enterFunction_argument_analytic(self, ctx:ora2epasParser.Function_argument_analyticContext):
        pass

    # Exit a parse tree produced by ora2epasParser#function_argument_analytic.
    def exitFunction_argument_analytic(self, ctx:ora2epasParser.Function_argument_analyticContext):
        pass


    # Enter a parse tree produced by ora2epasParser#function_argument_modeling.
    def enterFunction_argument_modeling(self, ctx:ora2epasParser.Function_argument_modelingContext):
        pass

    # Exit a parse tree produced by ora2epasParser#function_argument_modeling.
    def exitFunction_argument_modeling(self, ctx:ora2epasParser.Function_argument_modelingContext):
        pass


    # Enter a parse tree produced by ora2epasParser#respect_or_ignore_nulls.
    def enterRespect_or_ignore_nulls(self, ctx:ora2epasParser.Respect_or_ignore_nullsContext):
        pass

    # Exit a parse tree produced by ora2epasParser#respect_or_ignore_nulls.
    def exitRespect_or_ignore_nulls(self, ctx:ora2epasParser.Respect_or_ignore_nullsContext):
        pass


    # Enter a parse tree produced by ora2epasParser#argument.
    def enterArgument(self, ctx:ora2epasParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ora2epasParser#argument.
    def exitArgument(self, ctx:ora2epasParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ora2epasParser#type_spec.
    def enterType_spec(self, ctx:ora2epasParser.Type_specContext):
        pass

    # Exit a parse tree produced by ora2epasParser#type_spec.
    def exitType_spec(self, ctx:ora2epasParser.Type_specContext):
        pass


    # Enter a parse tree produced by ora2epasParser#datatype.
    def enterDatatype(self, ctx:ora2epasParser.DatatypeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#datatype.
    def exitDatatype(self, ctx:ora2epasParser.DatatypeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#precision_part.
    def enterPrecision_part(self, ctx:ora2epasParser.Precision_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#precision_part.
    def exitPrecision_part(self, ctx:ora2epasParser.Precision_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#native_datatype_element.
    def enterNative_datatype_element(self, ctx:ora2epasParser.Native_datatype_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#native_datatype_element.
    def exitNative_datatype_element(self, ctx:ora2epasParser.Native_datatype_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#bind_variable.
    def enterBind_variable(self, ctx:ora2epasParser.Bind_variableContext):
        pass

    # Exit a parse tree produced by ora2epasParser#bind_variable.
    def exitBind_variable(self, ctx:ora2epasParser.Bind_variableContext):
        pass


    # Enter a parse tree produced by ora2epasParser#general_element.
    def enterGeneral_element(self, ctx:ora2epasParser.General_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#general_element.
    def exitGeneral_element(self, ctx:ora2epasParser.General_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#general_element_part.
    def enterGeneral_element_part(self, ctx:ora2epasParser.General_element_partContext):
        pass

    # Exit a parse tree produced by ora2epasParser#general_element_part.
    def exitGeneral_element_part(self, ctx:ora2epasParser.General_element_partContext):
        pass


    # Enter a parse tree produced by ora2epasParser#table_element.
    def enterTable_element(self, ctx:ora2epasParser.Table_elementContext):
        pass

    # Exit a parse tree produced by ora2epasParser#table_element.
    def exitTable_element(self, ctx:ora2epasParser.Table_elementContext):
        pass


    # Enter a parse tree produced by ora2epasParser#constant.
    def enterConstant(self, ctx:ora2epasParser.ConstantContext):
        pass

    # Exit a parse tree produced by ora2epasParser#constant.
    def exitConstant(self, ctx:ora2epasParser.ConstantContext):
        pass


    # Enter a parse tree produced by ora2epasParser#numeric.
    def enterNumeric(self, ctx:ora2epasParser.NumericContext):
        pass

    # Exit a parse tree produced by ora2epasParser#numeric.
    def exitNumeric(self, ctx:ora2epasParser.NumericContext):
        pass


    # Enter a parse tree produced by ora2epasParser#numeric_negative.
    def enterNumeric_negative(self, ctx:ora2epasParser.Numeric_negativeContext):
        pass

    # Exit a parse tree produced by ora2epasParser#numeric_negative.
    def exitNumeric_negative(self, ctx:ora2epasParser.Numeric_negativeContext):
        pass


    # Enter a parse tree produced by ora2epasParser#quoted_string.
    def enterQuoted_string(self, ctx:ora2epasParser.Quoted_stringContext):
        pass

    # Exit a parse tree produced by ora2epasParser#quoted_string.
    def exitQuoted_string(self, ctx:ora2epasParser.Quoted_stringContext):
        pass


    # Enter a parse tree produced by ora2epasParser#identifier.
    def enterIdentifier(self, ctx:ora2epasParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ora2epasParser#identifier.
    def exitIdentifier(self, ctx:ora2epasParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ora2epasParser#id_expression.
    def enterId_expression(self, ctx:ora2epasParser.Id_expressionContext):
        pass

    # Exit a parse tree produced by ora2epasParser#id_expression.
    def exitId_expression(self, ctx:ora2epasParser.Id_expressionContext):
        pass


    # Enter a parse tree produced by ora2epasParser#not_equal_op.
    def enterNot_equal_op(self, ctx:ora2epasParser.Not_equal_opContext):
        pass

    # Exit a parse tree produced by ora2epasParser#not_equal_op.
    def exitNot_equal_op(self, ctx:ora2epasParser.Not_equal_opContext):
        pass


    # Enter a parse tree produced by ora2epasParser#greater_than_or_equals_op.
    def enterGreater_than_or_equals_op(self, ctx:ora2epasParser.Greater_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by ora2epasParser#greater_than_or_equals_op.
    def exitGreater_than_or_equals_op(self, ctx:ora2epasParser.Greater_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by ora2epasParser#less_than_or_equals_op.
    def enterLess_than_or_equals_op(self, ctx:ora2epasParser.Less_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by ora2epasParser#less_than_or_equals_op.
    def exitLess_than_or_equals_op(self, ctx:ora2epasParser.Less_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by ora2epasParser#concatenation_op.
    def enterConcatenation_op(self, ctx:ora2epasParser.Concatenation_opContext):
        pass

    # Exit a parse tree produced by ora2epasParser#concatenation_op.
    def exitConcatenation_op(self, ctx:ora2epasParser.Concatenation_opContext):
        pass


    # Enter a parse tree produced by ora2epasParser#outer_join_sign.
    def enterOuter_join_sign(self, ctx:ora2epasParser.Outer_join_signContext):
        pass

    # Exit a parse tree produced by ora2epasParser#outer_join_sign.
    def exitOuter_join_sign(self, ctx:ora2epasParser.Outer_join_signContext):
        pass


    # Enter a parse tree produced by ora2epasParser#regular_id.
    def enterRegular_id(self, ctx:ora2epasParser.Regular_idContext):
        pass

    # Exit a parse tree produced by ora2epasParser#regular_id.
    def exitRegular_id(self, ctx:ora2epasParser.Regular_idContext):
        pass


    # Enter a parse tree produced by ora2epasParser#string_function_name.
    def enterString_function_name(self, ctx:ora2epasParser.String_function_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#string_function_name.
    def exitString_function_name(self, ctx:ora2epasParser.String_function_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#numeric_function_name.
    def enterNumeric_function_name(self, ctx:ora2epasParser.Numeric_function_nameContext):
        pass

    # Exit a parse tree produced by ora2epasParser#numeric_function_name.
    def exitNumeric_function_name(self, ctx:ora2epasParser.Numeric_function_nameContext):
        pass


    # Enter a parse tree produced by ora2epasParser#supported_packages.
    def enterSupported_packages(self, ctx:ora2epasParser.Supported_packagesContext):
        pass

    # Exit a parse tree produced by ora2epasParser#supported_packages.
    def exitSupported_packages(self, ctx:ora2epasParser.Supported_packagesContext):
        pass


