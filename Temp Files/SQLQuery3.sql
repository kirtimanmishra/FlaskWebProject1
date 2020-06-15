delete [DbTest].[dbo].[kali_node]
delete [DbTest].[dbo].[kali_wf]

SELECT TOP (1000) [jobid]
		,[nodeid]
		,[wfid]
		,[nstatus]
		,[img_path]
		,[FaceCount]
	FROM [DbTest].[dbo].[kali_node]

SELECT TOP (1000) [jobid]
      ,[nodeid]
      ,[wfid]
      ,[nstatus]
      ,[img_path]
      ,[FaceCount]
  FROM [DbTest].[dbo].[kali_wf]

select * from [DbTest].[dbo].[kali_node] where nodeid='node_analytics' and nstatus='pending'

select * from [DbTest].[dbo].[kali_wf] where nodeid='node_analytics'

update [DbTest].[dbo].[kali_node] set FaceCount=0 where nodeid='node_analytics'
