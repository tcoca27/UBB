DROP TABLE Squad_coaching
DROP TABLE Squad_enrollment
DROP TABLE Squad
DROP TABLE Player

CREATE TABLE Squad
(
	Sq_id INT NOT NULL PRIMARY KEY,
	Sname CHAR(15) NOT NULL,
	rating INT NOT NULL UNIQUE
	);

	
CREATE TABLE Player
(
	Pl_id INT NOT NULL PRIMARY KEY,
	Pl_name CHAR(30),
	Pl_rating INT,
	Pl_nationality CHAR(15),
	)

CREATE TABLE Squad_enrollment
(
	se_id INT NOT NULL PRIMARY KEY,
	Sq_id INT NOT NULL FOREIGN KEY REFERENCES Squad(Sq_id),
	Pl_id INT NOT NULL FOREIGN KEY REFERENCES Player(Pl_id),
	[contract] INT
	)

INSERT INTO Player(Pl_id,Pl_name,Pl_nationality,Pl_rating)
VALUES (1,'pl1','rou',55),
(2,'ret','asd',87),
(3,'dsa','ghj',79),
(4,'gg','tye',91),
(5,'qw','rty',23)

INSERT INTO Squad(Sq_id,Sname,rating)
VALUES (7,'ors',23),
(1,'opt',88),
(2,'sda',46),
(3,'hgf',84),
(4,'iuo',72),
(5,'jkl',65),
(6,'lkl',90)

INSERT INTO Squad_enrollment(se_id,Sq_id,Pl_id,contract)
VALUES (6,7,1,9),
(1,1,2,6),
(2,5,4,8),
(3,6,2,9),
(4,1,3,7),
(5,3,2,2)

--Ta is Squad, Tb is Player, Tc is Squad_enrollment--

--clustered index scan; 
		SELECT * FROM Squad

--clustered index seek;
		SELECT * FROM Squad
		WHERE Sq_id >= 3

--nonclustered index scan;
		SELECT rating FROM Squad

--nonclustered index seek
		SELECT rating FROM Squad WHERE rating >= 70

--key look-up
		SELECT * FROM Squad
		where rating=88

---b.Write a query on table Tb with a WHERE clause of the form WHERE b2 = value and analyze its execution plan. 
--Create a nonclustered index that can speed up the query. 
--Recheck the query’s execution plan (operators, SELECT’s estimated subtree cost). 

--0.0032875
DROP INDEX ind2 ON Player
SELECT P.Pl_rating FROM Player P
WHERE P.Pl_rating=88

--nonclustered index
--0.0032831
CREATE NONCLUSTERED INDEX ind2 ON Player(Pl_rating)
SELECT P.Pl_rating
FROM Player P
WHERE P.Pl_rating = 88

--c. Create a view that joins at least 2 tables. 
-- Check whether existing indexes are helpful; if not, reassess existing indexes / examine the cardinality of the tables.

	ALTER VIEW JoinT
	AS
	SELECT P.Pl_id,P.Pl_name, P.Pl_rating, SE.contract FROM Player P
	INNER JOIN Squad_enrollment SE on P.Pl_id=Se.Sq_id where P.Pl_rating > 70
	GO

	--0.0073902
	DROP INDEX ind2 ON Player
	SELECT * FROM JoinT

	DROP VIEW JoinT

