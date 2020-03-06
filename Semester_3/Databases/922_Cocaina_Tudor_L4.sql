INSERT INTO Tables(Name)
VALUES('Player'),
('Squad_enrollment'),
('Squad')

DBCC CHECKIDENT ('Tables', RESEED, 0);
GO

--view on one table
CREATE VIEW SelectOne
AS
SELECT * FROM Player
GO

--view on two tables
ALTER VIEW SelectTwo
AS
SELECT * FROM Player p, Squad S
WHERE p.Pl_rating>70 and S.Sname like 'Squad%'
GO

--view on two tables with group by
ALTER VIEW SelectThree
AS
SELECT COUNT(P.Pl_name) AS NumberPlayers, P.Pl_rating FROM Player P
GROUP BY P.Pl_rating
HAVING COUNT(P.Pl_name) > (SELECT COUNT(S.Sname) FROM Squad S
							WHERE S.rating=P.Pl_rating)
GO

SELECT * FROM SelectThree

INSERT INTO Views(Name)
VALUES ('SelectOne'),
('SelectTwo'),
('SelectThree')

--insert in tests--
INSERT INTO Tests(Name)
VALUES ('TestAll')

--insert data in TestTables
INSERT INTO TestTables(TestID,TableID,NoOfRows,Position)
VALUES (1,1,500,2),
(1,2,500,1),
(1,3,500,3)

INSERT INTO Views(Name)
VALUES('SelectOne'),
('SelectTwo'),
('SelectThree')

SELECT * FROM Tables
SELECT * FROM Views
SELECT * FROM Tests
SELECT * FROM TestTables


ALTER PROCEDURE TestRun
( @test VARCHAR(50))
AS
BEGIN
	IF EXISTS(SELECT 1 FROM Tests WHERE Name=@test)
	BEGIN
	--INSERT THE TEST INTO THE TEST RUNS TABLE WITH THE CURRENT TIME--
	DECLARE @CURRENT DATETIME=GETDATE();
	INSERT INTO TestRuns
	VALUES ('ALL TESTS',@CURRENT,@CURRENT)

	DECLARE @TestRunId INT;
	DECLARE @TableName VARCHAR(30);
	--DYNAMIC VARIABLE THAT WILL BE EXECUTED
	DECLARE @T VARCHAR(100);

	--GET THE ID OF THE TEST--
	SET @TestRunId = (SELECT TestRunId FROM TestRuns WHERE StartAt=@CURRENT)

	--DELETE ON TABLES--
	--FIRST WE DELETE DATA FROM THE TABLE THAT HOLDS THE RELATION BETWEEN THE OTHER 2--
	SET @TableName=(SELECT T.Name FROM Tables T INNER JOIN TestTables TT ON T.TableID=TT.TableID WHERE TT.Position=1)
	SET @T= 'DELETE FROM '+@TableName
	EXEC(@T)

	--DELETE THE OTHER TWO TABLES
	SET @TableName=(SELECT T.Name FROM Tables T INNER JOIN TestTables TT ON T.TableID=TT.TableID WHERE TT.Position=2)
	SET @T= 'DELETE FROM '+@TableName
	EXEC(@T)

	SET @TableName=(SELECT T.Name FROM Tables T INNER JOIN TestTables TT ON T.TableID=TT.TableID WHERE TT.Position=3)
	SET @T= 'DELETE FROM '+@TableName
	EXEC(@T)

	--INSERT INTO TABLES--
	DECLARE @ID VARCHAR(50);
	DECLARE @Rows INT;
	DECLARE @Time DATETIME;

	---INSERT DATA ABOUT THE INSERT OPERATION ON THE TABLE SQUAD IN TEST RUN TABLES--
	--INSERTING INTO TABLE SQUAD--
	DECLARE @TableId VARCHAR(30);
	SET @TableId = (SELECT T.TableID FROM Tables T INNER JOIN TestTables TT ON T.TableID=TT.TableID WHERE TT.Position=3)
	SET @Time=GETDATE()
	INSERT INTO TestRunTables
	VALUES(@TestRunId,@TableId,@Time,@Time)

	SET @Rows=(SELECT TT.NoOfRows FROM Tables T INNER JOIN TestTables TT ON T.TableID=TT.TableID WHERE TT.Position=3)
	SET @ID=1
	SET @TableName=(SELECT T.Name FROM Tables T INNER JOIN TestTables TT ON T.TableID=TT.TableID WHERE TT.Position=3)
	WHILE @Rows>0
	BEGIN
		DECLARE @RATING VARCHAR(10);
		DECLARE @StId VARCHAR(10);
		SET @RATING=(SELECT FLOOR(RAND()*(99-1+1))+1);
		SET @StId=(SELECT FLOOR(RAND()*(8-5+1))+5);
		SET @T= 'INSERT INTO '+@TableName+'(Sq_id,Sname,rating,Sq_stadium)'+' VALUES('+@ID+','+'''Squad'+@ID+''','+@RATING+','+@StId+')'
		PRINT @T
		EXEC (@T)
		SET @ID=@ID+1
		SET @Rows=@Rows-1
	END

	--INSERTION ENDED, WE INSERT THE TIME AT WHICH IT ENDED--
	UPDATE TestRunTables
	SET EndAt =GETDATE() WHERE
	StartAt=@Time

	--FOR THE TABLE PLAYER--
	SET @TableId=(SELECT T.TableID FROM Tables t INNER JOIN TestTables TT ON TT.TableID=T.TableID WHERE TT.Position=2)
	SET @Time=GETDATE()
	INSERT INTO TestRunTables
	VALUES(@TestRunId,@TableId,@Time,@Time)

	SET @Rows=(SELECT TT.NoOfRows FROM TestTables TT INNER JOIN Tables T ON TT.TableID=T.TableID WHERE TT.Position=2)
	SET @ID=1
	SET @TableName=(SELECT T.Name FROM Tables T INNER JOIN TestTables TT ON TT.TableID=T.TableID WHERE TT.Position=2)
	WHILE @Rows>0
	BEGIN
		SET @RATING=(SELECT FLOOR(RAND()*(99-1+1))+1);
		SET @T='INSERT INTO '+@TableName+'(Pl_id,Pl_name,Pl_rating,Pl_nationality) VALUES('+@ID+','+'''Player'+@ID+''','+@RATING+','+'''Nation'+@ID+''')'
		PRINT @T
		EXEC(@T)
		SET @ID=@ID+1
		SET @Rows=@Rows-1
	END

	UPDATE TestRunTables
	SET EndAt=GETDATE() WHERE
	StartAT=@Time

	--FOR THE TABLE SQUAD_ENROLMENT--
	SET @TableId=(SELECT T.TableID FROM Tables T INNER JOIN TestTables TT ON TT.TableID=T.TableID WHERE TT.Position=1)
	SET @Time=GETDATE()
	INSERT INTO TestRunTables
	VALUES(@TestRunId,@TableId,@Time,@Time)

	SET @Rows=(SELECT TT.NoOfRows FROM TestTables TT INNER JOIN Tables T ON T.TableID=TT.TableID WHERE TT.Position=1)
	SET @TableName=(SELECT T.Name FROM Tables T INNER JOIN TestTables TT ON TT.TableID=T.TableID WHERE TT.Position=1)
	SET @ID=1
	WHILE @Rows>0
	BEGIN
		DECLARE @CONTRACT VARCHAR(10)
		SET @CONTRACT=(SELECT FLOOR(RAND()*(99-0+1))+0);
		SET @T='INSERT INTO '+@TableName+'(Sq_id,Pl_id,contract) VALUES('+@ID+','+@ID+','+@CONTRACT+')'
		PRINT @T
		EXEC(@T)
		SET @ID=@ID+1
		SET @Rows=@Rows-1
	END

	UPDATE TestRunTables
	SET EndAt=GETDATE() WHERE
	StartAt =@Time

	UPDATE TestRunTables
	SET EndAt= GETDATE() WHERE
	StartAt=@CURRENT
	-- DELETE AND INSERT ARE FINISHED --

	--TEST THE VIEWS--
	--FIRST ONE--
	DECLARE @VIEWTIME DATETIME=GETDATE()
	INSERT INTO TestRunViews
	VALUES(@TestRunId,1,@VIEWTIME,@VIEWTIME)
	
	SELECT * FROM SelectOne

	UPDATE TestRunViews
	SET EndAt=GETDATE() WHERE
	StartAt=@VIEWTIME

	--SECOND--
	SET @VIEWTIME=GETDATE()
	INSERT INTO TestRunViews
	VALUES(@TestRunId,2,@VIEWTIME,@VIEWTIME)
	
	SELECT * FROM SelectTwo

	UPDATE TestRunViews
	SET EndAt=GETDATE() WHERE
	StartAt=@VIEWTIME

	--THIRD--
	SET @VIEWTIME=GETDATE()
	INSERT INTO TestRunViews
	VALUES(@TestRunId,3,@VIEWTIME,@VIEWTIME)
	
	SELECT * FROM SelectThree

	UPDATE TestRunViews
	SET EndAt=GETDATE() WHERE
	StartAt=@VIEWTIME
	--VIEWS DONE--

	UPDATE TestRuns SET EndAt=GETDATE() WHERE StartAt=@CURRENT
	END
END
GO

EXEC TestRun TestAll

DELETE FROM TestRunViews
DELETE FROM TestRunTables
DELETE FROM TestRuns

SELECT * FROM TestRunViews
SELECT * FROM TestRunTables
SELECT * FROM TestRuns
