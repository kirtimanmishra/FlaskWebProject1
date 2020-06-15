delete [DbTest].[dbo].[kali_node_temp]

delete [DbTest].[dbo].[kali_wf_temp]


SELECT * FROM [DbTest].[dbo].[kali_node_temp]

SELECT * FROM [DbTest].[dbo].[kali_wf_temp]

select * from [DbTest].[dbo].[kali_node_temp] where nodeid='node_analytics' and nstatus='pending'
select * from [DbTest].[dbo].[kali_wf_temp] where nodeid='node_analytics'

update [DbTest].[dbo].[kali_node_temp] set FaceCount=0 where nodeid='node_analytics'
insert into [DbTest].[dbo].[kali_wf_temp] values(8,'node_analytics','wf_AC','pending','D:/Projects/Implementation Workflow/IoT Workflow/FlaskWebProject1/FlaskWebProject1/nodes/node_camera/download8.jpg',0);

select count(*) from [DbTest].[dbo].[kali_node_temp]

