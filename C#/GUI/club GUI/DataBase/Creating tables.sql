/*CREATE DATABASE Club_DataBase;
USE Club_DataBase; */

CREATE TABLE Admin
(
	[Username] VARCHAR(50) NOT NULL PRIMARY KEY, 
    [Password] VARCHAR(50) NOT NULL, 
    [Email] VARCHAR(50) NOT NULL DEFAULT 'Empty@mail.apu.edu.my'
);

CREATE TABLE Students
(
	[Username] VARCHAR(50) NOT NULL PRIMARY KEY, 
    [Password] VARCHAR(50) NOT NULL,
    /* Holds the name of the club the representative represents */
    [rep] VARCHAR(50) NOT NULL DEFAULT 'not',
    [Email] VARCHAR(50) NOT NULL DEFAULT 'Empty@mail.apu.edu.my'
);

CREATE TABLE Clubs
(
	[ClubName] VARCHAR(50) NOT NULL PRIMARY KEY, 
	[Cat] VARCHAR(50) NOT NULL,
    [RegDate] Date NOT NULL,
    [President] VARCHAR(50) NOT NULL,
    [Vice] VARCHAR(50) NOT NULL,
    [Description] VARCHAR(MAX) NOT NULL,
    [LastUpdated] DateTime
);