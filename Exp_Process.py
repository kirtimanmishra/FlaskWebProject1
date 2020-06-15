import pyodbc
import time

def process_message(nodeid,FaceCount) :
    #print ('conditional routing happens here... mydata')
    if(nodeid=='node_camera'):
        return 'node_analytics'
    if(nodeid=='node_analytics' and FaceCount<10):
        return 'node_ignore'
    if(nodeid=='node_analytics' and FaceCount>=10):
        return 'node_AC'

start_time = time.time()

conn1 = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                  "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                  "Database=DbTest;"
                  "Trusted_Connection=yes;")
cursor1 = conn1.cursor() 
cursor1.execute('select count(*) from [DbTest].[dbo].[kali_wf]')
for row in cursor1:    
    t=row[0]
 
for i in range(t): 
    conn1 = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                  "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                  "Database=DbTest;"
                  "Trusted_Connection=yes;")
    cursor1 = conn1.cursor() 

   # print ('Processing workflow')
    cursor1.execute('select top 1 * from [DbTest].[dbo].[kali_wf] where nstatus=\'pending\'')
    #just process one pending job at a time
    for row in cursor1:    
        #print('WF processing...',row)
        jobid=row[0]
        nodeid=row[1]
        wfid=row[2]
        nstatus = row[3] 
        img_path=row[4]
        FaceCount = row[5] 

        target_nid = process_message(nodeid,FaceCount)

        q1 = 'DELETE FROM kali_wf WHERE jobid=?'
        cursor1.execute(q1,(jobid,))

        q2 = ('INSERT INTO [DbTest].[dbo].[kali_node] (jobid,nodeid,wfid,nstatus,img_path,FaceCount) values (?,?,?,?,?,?);')
        values = [jobid,target_nid,wfid,nstatus,img_path,FaceCount]
        cursor1.execute(q2,values)
        break
    # end for loop
    cursor1.commit()
    #cursor2.commit()
    conn1.close()
    #conn2.close()
   
print("--- %s seconds ---" % (time.time() - start_time))
