CREATE TABLE Institutions
(
	iID INT NOT NULL PRIMARY KEY,
	iName VARCHAR(30),
	iWeb VARCHAR(50),
	iBudget INT,
	nrEmp INT
	)

CREATE TABLE Participants
(
	pID INT NOT NULL PRIMARY KEY,
	pName VARCHAR(30),
	pDate date,
	iID INT FOREIGN KEY REFERENCES Institutions(iID)
	)

CREATE TABLE ConferenceTypes
(
	ctID INT NOT NULL PRIMARY KEY,
	ctName VARCHAR(30),
	ctDesc VARCHAR(100)
	)

CREATE TABLE Conference
(
	cID INT NOT NULL PRIMARY KEY,
	cName VARCHAR(30),
	cLocation VARCHAR(30),
	cFee INT,
	ctID INT FOREIGN KEY REFERENCES ConferenceTypes(ctID)
	)

CREATE TABLE CP
(
	cpID INT NOT NULL IDENTITY,
	cID INT FOREIGN KEY REFERENCES Conference(cID),
	pID INT FOREIGN KEY REFERENCES Participants(pID),
	cpDate date,
	cpTime time
	)

INSERT INTO ConferenceTypes VALUES
(1,'t','asd'),
(2,'g','sdf')

SELECT * FROM Conference

INSERT INTO Conference VALUES
(4,'opt','sss',2,1),
(1,'opt','ghj',15,1),
(2,'fds','ghf',10,1),
(3,'ty','kl',12,2)

SELECT sum(C.cFee) FROM Conference C GROUP BY C.cName

INSERT INTO Institutions VALUES
(1,'ol','web',1500,12),
(2,'sd','www',200,3),
(3,'er','wet',100,2)

INSERT INTO Participants VALUES
(2,'p','1998-01-02',2),
(3,'t','1976-05-06',3),
(1,'o','1990-09-09',1)

GO
CREATE PROCEDURE sp_addCP @cID INT, @pID INT, @cpDate date, @cpTime time 
AS
	DECLARE @no INT
	SET @no=0
	SELECT @no=COUNT(*) FROM CP WHERE cid=@cID and pID=@pID

	IF (@no!=0)
	BEGIN
		UPDATE CP
		SET cpDate=@cpDate, cpTime=@cpTime
		WHERE cID=@cID and pID=@pID
	END
	ELSE
	BEGIN
		INSERT INTO CP VALUES (@cID,@pID,@cpDate,@cpTime)
	END
END

EXECUTE sp_addCP 1,1,'2020-07-07','10:00:00'
EXECUTE sp_addCP 2,1,'2020-07-07','10:00:00'
EXECUTE sp_addCP 3,1,'2020-07-07','10:00:00'
EXECUTE sp_addCP 3,1,'2020-07-08','10:00:00'

SELECT * FROM CP


CREATE VIEW v_getP
AS
	SELECT P.pName FROM Participants P
	INNER JOIN CP ON CP.pID=P.pID
	GROUP BY P.pName
	HAVING COUNT(*)= (SELECT COUNT(*) FROM Conference)
GO

SELECT * FROM v_getP

ALTER FUNCTION f_getP (@c INT, @t VARCHAR(30))
RETURNS TABLE
AS
RETURN
	SELECT P.pName, count(P.pName) as noOfConfernces FROM Participants P
	INNER JOIN CP ON CP.pID=P.pID
	INNER JOIN Conference C ON CP.cID=C.cID
	INNER JOIN ConferenceTypes CT ON C.ctID=CT.ctID WHERE CT.ctName=@t
	GROUP BY P.pName
	HAVING COUNT(*)>= @c
GO

SELECT * FROM f_getP(3,'t')
