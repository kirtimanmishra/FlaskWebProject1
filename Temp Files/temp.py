import pyodbc 
try :
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                  "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                  "Database=DbTest;"
                  "Trusted_Connection=yes;")
    cursor = conn.cursor() 
    SQLCommand = ('INSERT INTO [DbTest].[dbo].[kali_node] (jobid,nodeid,wfid,nstatus,img_path,FaceCount) values (?,?,?,?,?,?);')
    values = [4,'node_camera','wf_AC','pending','hii',0]
    cursor.execute(SQLCommand,values)
    conn.commit()
    conn.close()
except :
    pass