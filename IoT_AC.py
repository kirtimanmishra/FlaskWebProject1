import pyodbc
from datetime import datetime
from flask import render_template
from node_AC import app


def process_AC():
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                    "Database=DbTest;"
                    "Trusted_Connection=yes;")
    cursor = conn.cursor()
    qstr = "select * from [DbTest].[dbo].[kali_node] where nodeid=\'node_AC\' and nstatus=\'pending\' "
    #print ('query is',qstr)
    cursor.execute(qstr)
    print ('AC in execution')
    #begin for loop
    for row in cursor:
        jobid = row[0]
        FaceCount = row[5] 
        print ('joblist: ',jobid, 'FaceCount: ',FaceCount, ' has been sent to Actuator for Processsing')
    return 'AC Done Processing' 