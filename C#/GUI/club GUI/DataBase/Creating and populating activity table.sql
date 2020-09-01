CREATE TABLE [dbo].[Activities] ( 

    [ClubName]       NCHAR (255)   NOT NULL, 

    [cat]       NCHAR (255)   NOT NULL,

    [Club Actiivity] VARCHAR (MAX) NOT NULL, 

    [Date]           DATETIME      NULL, 

); 

INSERT INTO [dbo].[Activities] ([ClubName], [cat],[Club Actiivity], [Date]) 
VALUES (N'Maths club', N'Academic', N'Orientation', N'2020-01-04 08:00:00') 

INSERT INTO [dbo].[Activities] ([ClubName], [cat],[Club Actiivity], [Date])
VALUES (N'Science club', N'Academic', N'Leading new students to familiar ', N'2020-01-04 08:00:00') 

INSERT INTO [dbo].[Activities] ([ClubName], [cat],[Club Actiivity], [Date])
VALUES (N'Culturework club', N'ArtOrganization', N'Art', N'2020-05-01 08:00:00') 

INSERT INTO [dbo].[Activities] ([ClubName], [cat],[Club Actiivity], [Date])
VALUES (N'Culturework club', N'ArtOrganization',N'Old-style singing', N'2020-05-01 09:00:00') 

INSERT INTO [dbo].[Activities] ([ClubName], [cat],[Club Actiivity], [Date])
VALUES (N'BasketBall club', N'Sport', N'Training', N'2020-01-04 08:00:00') 

INSERT INTO [dbo].[Activities] ([ClubName], [cat],[Club Actiivity], [Date])
VALUES (N'Futsal club', N'Sport', N'Training', N'2020-01-04 08:00:00') 

 