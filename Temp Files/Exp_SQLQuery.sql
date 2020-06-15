delete [DbTest].[dbo].[kali_node]

delete [DbTest].[dbo].[kali_wf]

SELECT * FROM [DbTest].[dbo].[kali_node]

SELECT * FROM [DbTest].[dbo].[kali_wf]

select * from [DbTest].[dbo].[kali_node] where nodeid='node_analytics' and nstatus='pending'
select * from [DbTest].[dbo].[kali_wf] where nodeid='node_analytics'

update [DbTest].[dbo].[kali_node] set FaceCount=0 where nodeid='node_analytics'
insert into [DbTest].[dbo].[kali_wf] values(8,'node_analytics','wf_AC','pending','D:/Projects/Implementation Workflow/IoT Workflow/FlaskWebProject1/FlaskWebProject1/nodes/node_camera/download8.jpg',0);


