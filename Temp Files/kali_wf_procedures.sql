use kalidb;

drop table if exists kali_node;

create table kali_node (
	jobid varchar(255),
	nodeid varchar(255),
	wfid varchar(255),
	nstatus varchar(255), --pending or processed
	ndata varchar(255) -- json contents
);

/* --------------------------------------------------------------- */

drop table if exists kali_wf;

create table kali_wf (
	jobid varchar(255),
	nodeid varchar(255),
	wfid varchar(255),
	wfstatus varchar(255), --pending or processed
	wfdata varchar(255) -- json contents
);

/* --------------------------------------------------------------- */

drop procedure if exists proc_putmsg_node;

create procedure proc_putmsg_node(@node varchar(200), @wfid varchar(200), @data varchar(200)) as

begin
	Declare @nrows int;
	Declare @jobid varchar(50);

	set @nrows = (select count(*) from [kalidb].[dbo].[kali_node]);
	/* print @nrows; */
	set @jobid = Convert(varchar,@nrows)
	/*print @jobid;*/

	insert into [kalidb].[dbo].[kali_node] values (@jobid,@node,@wfid,'pending',@data);
end

exec proc_putmsg_node 'nx','wfx','mydata'

/* --------------------------------------------------------------- */

drop procedure if exists proc_putmsg_wf;

create procedure proc_putmsg_wf(@node varchar(200), @wfid varchar(200), @data varchar(200)) as

begin
	Declare @nrows int;
	Declare @jobid varchar(50);

	set @nrows = (select count(*) from [kalidb].[dbo].[kali_wf]);
	/* print @nrows; */
	set @jobid = Convert(varchar,@nrows)
	/*print @jobid;*/

	insert into [kalidb].[dbo].[kali_wf] values (@jobid,@node,@wfid,'pending',@data);
end

exec proc_putmsg_wf 'nx','wfx','mydata'

/* --------------------------------------------------------------- */

drop procedure if exists proc_delmsg_node;

create procedure proc_delmsg_node(@jobid varchar(50)) as
begin
	delete from [kalidb].[dbo].[kali_node] where jobid = @jobid;
end

exec proc_delmsg_node '0'

/* --------------------------------------------------------------- */

drop procedure if exists proc_delmsg_wf;

create procedure proc_delmsg_wf(@jobid varchar(50)) as
begin
	delete from [kalidb].[dbo].[kali_wf] where jobid = @jobid;
end

exec proc_delmsg_wf '1'

/* --------------------------------------------------------------- */

drop procedure if exists proc_wf2node;

alter procedure proc_wf2node as
begin
	Declare @pending_count int;
	Declare @wfjobid varchar(50);

	set @pending_count = (select count(*) from [kalidb].[dbo].[kali_wf] where wfstatus='pending');

	print @pending_count;

	if (@pending_count > 0)
	begin
		set @wfjobid = (select top 1 jobid from [kalidb].[dbo].[kali_wf] where wfstatus='pending');
		print @wfjobid;

		/* Move this job from wf table to node table */
	end;

end;

exec proc_wf2node

/*-----------------------------------------------------------------*/

select * from [kalidb].[dbo].[kali_wf];

select * from [kalidb].[dbo].[kali_node];

delete from [kalidb].[dbo].[kali_wf];
delete from [kalidb].[dbo].[kali_node];

insert into [kalidb].[dbo].[kali_node] values ('j8','n1','wf1','pending','ndata8');

select top 1 * from [kalidb].[dbo].[kali_wf];

select * from [kalidb].[dbo].[kali_node] where nodeid='nx' and nstatus='pending'

select * from [kalidb].[dbo].[kali_node] where nodeid='nx' and nstatus='pending'

/*-----------------------------------------------------------------*/






