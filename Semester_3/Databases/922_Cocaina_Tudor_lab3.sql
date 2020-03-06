DROP Proc spdo1
DROP proc spdo2
DROP proc spdo3
DROP proc spdo4
DROP proc spdo5
DROP proc spdo6
DROP proc spdo7

DROP proc spundo2
DROP proc spundo1
DROP proc spundo3
DROP proc spundo4
DROP proc spundo5
DROP proc spundo6
DROP proc spundo7

DROP proc ModifyVersion


--a.Modify the type of a column--
CREATE PROCEDURE spdo1
AS
	ALTER TABLE Kit
	ALTER COLUMN [type] Int
GO

--revert--

CREATE PROCEDURE spundo1
AS
	ALTER TABLE Kit
	ALTER COLUMN [type] CHAR(15)
GO

--b.add/remove a column--
CREATE PROCEDURE spdo2
AS
	ALTER TABLE Gamer
	ADD JoinedOn INT
GO

--revert--

CREATE PROCEDURE spundo2
AS
	ALTER TABLE Gamer
	DROP COLUMN JoinedOn
GO


---add a default constraint---

CREATE PROCEDURE spdo3
AS
	ALTER TABLE Weekend_League
	ADD CONSTRAINT def_constr DEFAULT 'no boosted players' for CONSTRAINTS
GO

--revert--
CREATE PROCEDURE spundo3
AS
	ALTER TABLE Weekend_League
	DROP CONSTRAINT def_constr
GO

---add a primary key---
CREATE PROCEDURE spdo5
AS
	ALTER TABLE Console
	ADD CONSTRAINT pk_Console PRIMARY KEY (ConsoleID)
GO

--revert--
CREATE PROCEDURE spundo5
AS
	ALTER TABLE Console
	DROP CONSTRAINT pk_Console
GO

---create table---
CREATE PROCEDURE spdo4
AS
	CREATE TABLE Console(
		ConsoleID int NOT NULL,
		[type] CHAR(20),
		gamertag CHAR(20) NOT NULL
		)
GO

--revert--
CREATE PROCEDURE spundo4
AS
	DROP TABLE Console
GO;

---add candidate key---
CREATE PROCEDURE spdo6
AS
	ALTER TABLE Tournament
	ADD CONSTRAINT ck_Tournament UNIQUE (tname)
GO;

--revert--
CREATE PROCEDURE spundo6
AS
	ALTER TABLE Tournament
	DROP CONSTRAINT ck_Tournament
GO;

---add foreign key---
CREATE PROCEDURE spdo7
AS
	ALTER TABLE Console
	ADD CONSTRAINT Fgk_Console FOREIGN KEY(gamertag) REFERENCES Gamer(gamertag)
GO

--revert--
CREATE PROCEDURE spundo7
AS
	ALTER TABLE Console
	DROP CONSTRAINT Fgk_Console
GO

exec spundo4

-----------------------------------------

CREATE TABLE VERSIONS(
	[Version] int
	)

INSERT INTO VERSIONS([Version])
VALUES(0)

CREATE PROCEDURE ModifyVersion(@version int)
AS
BEGIN
	DECLARE @current int
	SET @current =(SELECT MAX([Version]) FROM VERSIONS)

	if @version <0 or @version >7
	BEGIN
	PRINT N'Invalid version!';
	END

	else
	begin

	while @version > @current
	begin
		set @current=@current+1
		exec('EXEC spdo'+@current)
	end

	while @version < @current
	begin
		exec('EXEC spundo'+@current)
		set @current=@current-1
	end

	update VERSIONS
	set [Version] = @current
	END
END
GO

EXEC ModifyVersion 0
