USE [TelegramBotDB]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[TelegramUsers](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[TelegramId] [bigint] NOT NULL,
	[FirstName] [nvarchar](100) NULL,
	[LastName] [nvarchar](100) NULL,
	[UserName] [nvarchar](50) NULL,
	[link] [nvarchar](400) NULL,
	[InsertDateTime] [datetime] NOT NULL,
 CONSTRAINT [PK__Telegram__3214EC0701C0E560] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[TelegramUsers] ADD  CONSTRAINT [DF_TelegramUsers_InsertDateTime]  DEFAULT (getdate()) FOR [InsertDateTime]
GO


CREATE TABLE [dbo].[TelegramUserMessage](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[TelegramId] [int] NOT NULL,
	[Command] [nvarchar](100) NOT NULL,
	[InsertDateTime] [datetime] NOT NULL,
 CONSTRAINT [PK_TelegramUserMessage] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[TelegramUserMessage] ADD  CONSTRAINT [DF_TelegramUserMessage_InsertDateTime]  DEFAULT (getdate()) FOR [InsertDateTime]
GO

