/* Creating and using the DataBase */
CREATE DATABASE BingBing;
USE BingBing;

/* Creating the tables of the DataBase */

-- Player account table: 
-- Holds the user's information and progress
CREATE TABLE Player(
    Player_ID INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
    Player_Name VARCHAR(255) NOT NULL UNIQUE,
    Username VARCHAR(255) NOT NULL UNIQUE,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Global_lvl INT NOT NULL DEFAULT 1,
    Diamonds INT NOT NULL DEFAULT 250,
    Battle_Points INT NOT NULL DEFAULT 3000,
    -- 0 for Flase and any other value for True
    Online_Status BIT
);

-- Hero table: 
-- Holds all of the heroes information
CREATE TABLE Hero(
    Hero_ID INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
    Hero_Name VARCHAR(255) NOT NULL UNIQUE,
    Hero_Role VARCHAR(255) NOT NULL,
    Hero_Speciality VARCHAR(255) NOT NULL,
    Hero_Price INT NOT NULL
);

-- Skin table: 
-- Holds all of the heroes information
CREATE TABLE Skin(
    Skin_ID INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
    Skin_Name VARCHAR(255) NOT NULL UNIQUE,
    Skin_Price INT NOT NULL,
    Hero_ID INT NOT NULL REFERENCES Hero(Hero_ID)
);

-- Personal Statistics table: 
-- Holds additional information about the player
CREATE TABLE Personal_Statistic(
    Player_ID INT NOT NULL REFERENCES Player(Player_ID),
    MostUsed_Hero INT REFERENCES Hero(Hero_ID),
    Details VARCHAR(255),
    -- 0 for Flase and any other value for True
    PrevGame_Result BIT
);

-- Player Hero table: 
-- Holds the level of the referenced hero owned by the specified player, and is referenced in the Hero Skin table
CREATE TABLE Player_Hero(
    Ph_ID INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
    Player_ID INT NOT NULL REFERENCES Player(Player_ID),
    Hero_ID INT NOT NULL REFERENCES Hero(Hero_ID),
    lvl INT NOT NULL DEFAULT 1
);

-- Hero Skin table: 
-- Holds all the skins of the referenced hero owned by the specified player
CREATE TABLE Hero_Skin(
    Ph_ID INT NOT NULL REFERENCES Player_Hero(Ph_ID),
    Skin_ID INT NOT NULL REFERENCES Skin(Skin_ID)
);

-- Game Mode table: 
-- Holds information about every game mode available
CREATE TABLE Game_Mode(
    Mode_ID INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
    -- Brawl mode, Human vs AI mode, or Classic Mode
    Mode_Type VARCHAR(255) NOT NULL,
    Mode_Name VARCHAR(255) NOT NULL UNIQUE,
    Arena VARCHAR(255) NOT NULL UNIQUE,
);

-- Team table
-- Holds the names of the team members joining the game, their heroes and the heros' levels
CREATE TABLE Team(
    Team_ID INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
    Ph_ID1 INT NOT NULL REFERENCES Player_Hero(Ph_ID) UNIQUE,
    Ph_ID2 INT NOT NULL REFERENCES Player_Hero(Ph_ID) UNIQUE,
    Ph_ID3 INT NOT NULL REFERENCES Player_Hero(Ph_ID) UNIQUE,
    Ph_ID4 INT NOT NULL REFERENCES Player_Hero(Ph_ID) UNIQUE,
    Ph_ID5 INT NOT NULL REFERENCES Player_Hero(Ph_ID) UNIQUE,
);

-- Game Table
-- Holds the information of all the games played
CREATE TABLE Game(
    Game_ID INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
    Mode_ID INT NOT NULL REFERENCES Game_Mode(Mode_ID),
    Game_Duration INT NOT NULL,
    Battle_DateTime DATETIME NOT NULL,
    Game_Loser INT NOT NULL REFERENCES Team(Team_ID),
    Game_Winner INT NOT NULL REFERENCES Team(Team_ID)
);



