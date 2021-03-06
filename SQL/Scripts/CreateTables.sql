USE [AIChatBot]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[nrch_livst_a51]') AND type in (N'U'))
DROP TABLE [dbo].[nrch_livst_a51]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[nrch_livst_a51](
	[rid] [char](16) NOT NULL, --Train RTTI Train Identifier
	[tpl] [char](7) NOT NULL, --Location TIPLOC
	[pta] [char](5) NULL, --Planned Time of Arrival
	[ptd] [char](5) NULL, --Planned Time of Departure
	[wta] [char](8) NULL, --Working (staff) Time of Arrival
	[wtp] [char](8) NULL, --Working Time of Passing
	[wtd] [char](8) NULL, --Working Time of Departure
	[arr_et] [char](5) NULL, --Estimated Arrival Time
	[arr_wet] [char](5) NULL, --Working Estimated Time
	[arr_atremoved] [bit] NOT NULL, --true if actual replaced by estimated
	[pass_et] [char](5) NULL, --Estimated Passing Time
	[pass_wet] [char](5) NULL, --Working Estimated Time
	[pass_atremoved] [bit] NOT NULL, --true if actual replaced by estimated
	[dep_et] [char](5) NULL, --Estimated Departure
	[dep_wet] [char](5) NULL, --Working Estimated Time
	[dep_atremoved] [bit] NOT NULL, --true if actual replaced by estimated
	[arr_at] [char](5) NULL, --Recorded Actual Time of Arrival
	[pass_at] [char](5) NULL, --Actual Passing Time
	[dep_at] [char](5) NULL, --Actual Departure Time
	[cr_code] [smallint] NOT NULL, --Cancellation Reason Code
	[lr_code] [smallint] NOT NULL --Late Running Reason
) ON [PRIMARY]
GO

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Stations]') AND type in (N'U'))
DROP TABLE [dbo].[Stations]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Stations](
	[name] [nvarchar](50) NOT NULL,
	[longname_name_alias] [nvarchar](50) NULL,
	[alpha3] [nvarchar](50) NULL,
	[tiploc] [nvarchar](50) NOT NULL,
	[db_name] [nvarchar](50) NULL
) ON [PRIMARY]
GO

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Conversation_Record]') AND type in (N'U'))
DROP TABLE [dbo].[Conversation_Record]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Conversation_Record](
	[userID] [nvarchar](50) NOT NULL,
	[message] [nvarchar](1000) NULL,
	[fromUser] [bit] NOT NULL,
	[dateTimeID] [datetime] NOT NULL
) ON [PRIMARY]
GO

