import os
import pyodbc 
import time

start_time = time.time()
cam_dir = 'D:/Projects/Implementation Workflow/IoT Workflow/FlaskWebProject1/FlaskWebProject1/nodes/node_camera/'
i=0
listing = os.listdir(cam_dir)
for j in range (1):
    for file in listing:
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                      "Database=DbTest;"
                      "Trusted_Connection=yes;")
        cursor = conn.cursor() 
        SQLCommand = ('INSERT INTO [DbTest].[dbo].[kali_node] (jobid,nodeid,wfid,nstatus,img_path,FaceCount) values (?,?,?,?,?,?);')
        values = [i,'node_camera','wf_AC','pending',cam_dir+file,0]
        cursor.execute(SQLCommand,values)
        conn.commit()
        conn.close()
        i=i+1
        #print('database inserted')
        #break
        j=j+1
print("--- %s seconds ---" % (time.time() - start_time))