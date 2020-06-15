create procedure proc_delmsg_node(@jobid INT) as
begin
	delete from [DbTest].[dbo].[kali_node] where jobid = @jobid;
end