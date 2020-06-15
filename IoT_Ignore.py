import pyodbc

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                "Database=DbTest;"
                "Trusted_Connection=yes;")
cursor = conn.cursor()
qstr = "select * from [DbTest].[dbo].[kali_node] where nodeid=\'node_ignore\' and nstatus=\'pending\' "
#print ('query is',qstr)
cursor.execute(qstr)
print ('Node Ignore in execution')
#begin for loop
for row in cursor:
    jobid = row[0]
    FaceCount = row[5] 
    print ('joblist: ',jobid, 'FaceCount: ',FaceCount, ' has been sent to Actuator for Processsing')
