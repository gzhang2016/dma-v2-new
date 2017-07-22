###############################################################
# Copyright (c) 2016-2017 EnterpriseDB - All rights reserved.
# Author: Raghavendra Ra
#
# HTML template for assessment report which will be used in
# assessment_html_writer.py
###############################################################

# HTML CSS style structure
#-------------------------
html_css_style = """
<!DOCTYPE html>
<html>
<head>
    <style>
    /* Html and body tag setting */
    html,
    body {
        height: 100%;
        margin: 0;
        padding: 0;
        font-family: "Arial";
    }
    /* header setting */
    
    header {
        width: 100%;
        background: gold;
        position: fixed;
        top: 0;
        height: 60px !important;
        opacity: .8;
        text-align: center;
    }
    /* Footer alignment */
    
    h3 {
        color: blue;
    }
    
    .footer {
        width: 100%;
        background: gold;
        position: fixed;
        bottom: 0;
        height: 30px;
        text-align: center;
        font-style: italic;
        vertical-align: text-top;
        font-size: 14px;
    }
    /* center content setting */
    
    .content {
        position: relative;
        height: 100%;
        width: 100%;
        padding: 60px 0 20px 0;
        /* Sizing - any length */
        margin: 0 auto 0 auto;
        overflow: scroll;
        /* Header height and footer height */
        /* Center content */
        -moz-box-sizing: border-box;
        -webkit-box-sizing: border-box;
        -o-box-sizing: border-box;
        -ms-box-sizing: border-box;
        box-sizing: border-box;
    }
    
    #middlecontent {
        background: white;
        height: 100%;
        min-width: 300px;
        margin-left: 300px;
        /* margin-right: 100px; overflow: auto; */
        overflow: hidden;
        overflow-x: scroll;
        overflow-y: scroll;
        -moz-box-sizing: border-box;
        -webkit-box-sizing: border-box;
        -o-box-sizing: border-box;
        -ms-box-sizing: border-box;
        box-sizing: border-box;
        border-left-color: red;
        font-size: 14px;
    }
    /* Sidebar and its navigation settings */
    
    .sidebar {
        background: orange;
        background-color: orange;
        top: 60px;
        bottom: 20px;
        width: 300px;
        position: absolute;
        -moz-box-sizing: border-box;
        -webkit-box-sizing: border-box;
        -o-box-sizing: border-box;
        -ms-box-sizing: border-box;
        box-sizing: border-box;
    }
    
    /* Sidebar Navigation list */
    nav {
        float: left;
        margin: 0;
        padding: 1em;
    }
    
    nav ul {
        list-style-type: none;
        padding: 0;
    }
    
    nav ul li a {
        text-decoration: none;
        font-size: 14px;
        color: blue;
    }
    /* Every table title settings */
    
    caption {
        text-align: left;
        font-size: 160%;
        font-weight: bold;
        color: blue;
        white-space: nowrap;
        overflow: hidden;
        padding: 5px;
    }
    
    .alltables {
        table-layout: fixed;
        vertical-align: middle;
        border-collapse: collapse;
        font-family: "Arial";
        font-size: 10px;
        white-space: wrap;
        text-align: center;
        border: 1px solid black;
    }
  
    .alltables td {
        border: 1px solid black;
        font-family: "Arial";
        font-size: 14px;
        color: black; /* text-align: left;*/
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    /* for summary rows */

    .row-migration-stage {
        width: 10px;
        background-color: #F59B00;
        text-align: center;
    }
    .row-migration-stage-description {
        width: 100px;
        background-color: #F59B00;
        text-align: left;
    }
    .row-objects-instages {
        width: 20px;
        background-color: #F59B00;
        text-align: center;
    }

    th {
        background-color: #F59B00;
        border: 1px solid black;
        font-family: "Arial";
        font-size: 13px;
        color: black;
    }

    tr {
        line-height: 20px;
        text-align: center;
    }
    </style>
</head>
<body>
"""

#Top title of html page
#----------------------
html_header ="""
    <!-- Define Static header information -->
    <header>
        <font size="5"><b>Database Migration Assessment Report</b></font><br>
        <font size="2">A compatibility migration analysis for deploying Oracle database, on <b>EDB Postgres Advanced Server 9.6</b></font>
    </header>

    <!-- Main content after excluding header/footer -->
    <div class="content">
        <!-- Sidebar Always on top. Fixed position,width,relative to content width-->
"""

#HTML Side bar
#------------
html_sidebar="""
        <div id="sidebar">
            <nav>
                <img src="dma2/templates/html/EDB-Logo.jpeg" width="100px" height="65px">
                <p style="color:blue;font-size:10px; "><i><b>EnterpriseDB Corporation</b></i></p>
                <font size="3"><b>DMA Engine Version 2.0</b></font>
                <ul style="line-height: 135%">
                    <br>
                    <li><a href="#Executive Summary">Executive Summary</a></li>
                    <li><a href="#Schema Level Summary">Schema Level Summary</a></li>
                    <li><a href="#Schema Incompatibility Summary">Schema Incompatibility Summary</a></li>
                    <li><a href="#Schema Objects Summary">Schema Objects Summary</a></li>
                    <li><a href="#Schema Objects Status Summary">Schema Objects Status Summary</a></li>
                </ul>
            </nav>
        </div>
        <!-- Scrollable main content -->
        <div id="middlecontent">
"""

#Middle content executive summary table
#-------------------------------------

middle_content_executive_summary="""
            <!-- Executive Summary Section -->
            <div id="Executive Summary"></div><br>
            <table class="alltables">
                <caption>Executive Summary</caption>
                <tr><td style="font-size: 12px;text-align: left;">Assessment Date</td><td>%s</td></tr>
                <tr><td style="font-size: 12px;text-align: left;">Oracle Database Name</td><td>%s</td></tr>
                <tr><td style="font-size: 12px;text-align: left;">Oracle Schema Name</td><td>%s</td></tr>
                <tr><td style="font-size: 12px;text-align: left;">Total Storage Objects</td><td>%s</td></tr>
                <tr><td style="font-size: 12px;text-align: left;">Total Code Objects</td><td>%s</td></tr>
                <tr><td style="font-size: 12px;text-align: left;">Number of Lines Parsed(Code Objects)</td><td>%s</td></tr>
            </table>
            <br>
            <p>When migrating an Oracle database and application to EDB Postgres Advanced Server, the objects need to be modified either by automatic using EDB Migration Toolkit or manually changes by editing SQL Definition of object. DMA analyzes the objects and classifies the modification needed into 5 stages. There are:</p>
            <!-- Migration Stage Table -->
            <table class="alltables">
                <caption>Objects in Migration Stages</caption>
                <thead>
                    <tr>
                        <th class="row-migration-stage"> Migration Stages </th>
                        <th class="row-migration-stage-description">Description</th>
                        <th class="row-objects-instages">No. of Objects</th>
                    </tr>
                </thead>
"""

#Migration Stages Summary
#------------------------

migration_stage_summary= """
                <tbody>
                    <tr><td>0</td><td>Automatic migration. No changes are needed<br>EDB Migration Toolkit can convert these objects automatically without any impact to database or application functionality</td><td>%d</td></tr>
                    <tr><td>1</td><td>A manual intervention is needed to change the syntax. The functionality remain the same</td><td>%d</td></tr>
                    <tr><td>2</td><td>Behaviorally difference, hence application logic need to be changed</td><td>%d</td></tr>
                    <tr><td>3</td><td>Solution exist to achieve the similar functionality in EPAS</td><td>%d</td></tr>
                    <tr><td>4</td><td>Not Supported, alternative solution need to be used either rewrite or alternative method</td><td>%d</td></tr>
                </tbody>
            </table><br>
"""
#Schema level summary header
#---------------------------
schema_level_summary_table_header = """
            <!-- Schema Level Summary Table -->
            <div id="Schema Level Summary"></div>
            <table class="alltables">
                <caption>Schema Level Summary</caption>
                <thead>
                    <tr>
                    <th>Object Type</th>
                    <th>No. of Assessed Objects</th>
                    <th>No. of Incompatible Objects</th>
                    <th>Migration Succes(%)</th>
                    </tr>
                </thead>
                <tbody>
"""

#Schema level summary header row iterator
#----------------------------------------
schema_level_summary_table_rowiterator = """
                    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
"""
#Schema incompatible summary header
#----------------------------------
schema_incompatible_summary_header = """
                </tbody>
            </table><br><br>
            <!-- Schema Level Summary Table -->
            <div id="Schema Incompatibility Summary"></div>
            <table class="alltables">
                <caption>Schema Incompatibility Summary</caption>
                <thead>
                    <tr>
                    <th>Object Type</th>
                    <th>Incompatibility Reason</th>
                    <th>Average Occurence in an Object</th>
                    </tr>
                </thead>
                <tbody>
"""
#Schema incompatible summary header row iterator
#-----------------------------------------------

schema_incompatible_summary_rowiterator = """
                    <tr><td>%s</td><td>%s</td><td>%s</td></tr>
"""
#Schema Object level summary header
#----------------------------------

schema_object_level_summary_header = """
                </tbody>
            </table><br><br>

            <!-- Schema Objects Summary Table -->
            <div id="Schema Objects Summary"></div>
            <table class="alltables">
                <caption>Schema Objects Summary</caption>
                <thead>
                    <tr>
                    <th>Object Type</th>
                    <th>Object Name</th>
                    <th>Incompatible Context</th>
                    <th>Incompatible Context Details</th>
                    <th>At line</th>
                    </tr>
                </thead>
                <tbody>
"""
#Schema Object level summary header rowiterator
#----------------------------------------------
schema_object_level_summary_rowiterator = """
                    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
"""

#Schema Object status summary header
#----------------------------------
schema_object_status_summary_header = """
                </tbody>
            </table><br><br>
            <!-- Schema Objects Status Summary Table -->
            <div id="Schema Objects Status Summary"></div>
            <table class="alltables">
                <caption>Schema Objects Status Summary</caption>
                <thead>
                    <tr>
                    <th>Object Type</th>
                    <th>Total Objects</th>
                    <th>Valid Objects</th>
                    <th>Invalid Objects</th>
                    </tr>
                </thead>
                <tbody>
"""
#Schema Object status summary header rowiterator
#----------------------------------------------
schema_object_status_summary_rowiterator = """
                    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
"""

html_tags_closure = """ 
</tbody>
            </table><br><br>
        </div>
    </div>
"""

html_bottom = """
    <!-- Always at the end of the page -->
    <div class="footer">
        Copyrights &copy;2017 EnterpriseDB Corporation
    </div>
</body>
</html>
"""

