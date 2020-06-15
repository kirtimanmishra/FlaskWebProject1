import cv2
import pyodbc
face_cascade = cv2.CascadeClassifier('D:/Projects/IoT Project/FlaskWebProject1/FlaskWebProject1/haarcascade_frontalface_default.xml')

while True:
    conn1 = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                "Database=DbTest;"
                "Trusted_Connection=yes;")
    cursor1 = conn1.cursor() 
    
    conn2 = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                    "Database=DbTest;"
                    "Trusted_Connection=yes;")
    cursor2 = conn2.cursor() 
    
    print ('Processing workflow')
    cursor1.execute('select  * from [DbTest].[dbo].[kali_node] where nodeid=\'node_analytics\' and FaceCount=0 and nstatus=\'pending\'')
    print('WF processing...')
    
    for row in cursor1:    
        jobid=row[0]
        nodeid=row[1]
        wfid=row[2]
        nstatus = row[3] 
        img_path=row[4]
        FaceCount = row[5] 
        print(jobid,nodeid)
        image = cv2.imread(img_path)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayImage)
        if len(faces) == 0:
                FaceCount = 0
                print('Faces are')
                print(FaceCount)
        else:
            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
            cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
     
            FaceCount = faces.shape[0] 
            print('Faces are')
            print(FaceCount)
        
        q1 = 'DELETE FROM kali_node WHERE jobid=?'
        cursor1.execute(q1,(jobid,))
        
        q2 = ('INSERT INTO [DbTest].[dbo].[kali_node] (jobid,nodeid,wfid,nstatus,img_path,FaceCount) values (?,?,?,?,?,?);')
        values = [jobid,nodeid,wfid,nstatus,img_path,FaceCount]
        cursor2.execute(q2,values)
        break
        # end for loop
    cursor1.commit()
    cursor2.commit()
    conn1.close()
    conn2.close()