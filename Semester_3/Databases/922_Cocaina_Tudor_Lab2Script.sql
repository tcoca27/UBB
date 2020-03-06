INSERT INTO Player(Pl_name, Pl_nationality, Pl_rating)
VALUES ('Harry Kane','England',89),
('Alex Paun','Romania',70),
('Gini Wijnaldum','Netherlands',84),
('ABC','SRC',1),
('Ciprian Deac','Romania',73),
('Juan Culio','Argentina',71), 
('Sergio Aguero', 'Argentina', 89),
('Lucas Moura', 'Brazil', 83),
('Billel Omrani', 'Algeria', 69),
('Virgil Van Dijk','Netherlands',90),
('Neymar Jr','Brazil',92),
('Alex Sandro','Brazil',85);

INSERT INTO Player(Pl_name, Pl_nationality, Pl_rating)
VALUES ('Ciprian Deac','Moldova',61)

UPDATE Player
SET Pl_rating=72
WHERE Pl_name LIKE 'Ciprian Deac' AND Pl_rating>71

DELETE Player where Pl_name='ABC' OR Pl_nationality='SRC' OR Pl_rating<=1

INSERT INTO Weekend_League(wlid)
VALUES (2),(1);

INSERT INTO Gamer(gamertag)
VALUES ('Sparkk'),
('Inception'),
('EagerestPark'),
('tekkz');

DELETE Gamer where gamertag='Sparkk'

UPDATE Gamer
SET gamertag='InceptionXX'
WHERE gamertag='Inception'

INSERT INTO Stadium(S_name)
VALUES ('Old Trafford'),('Anfield'),('Cluj Arena');

INSERT INTO Club(Cname,established_in_the_year,wlid,gamertag,S_name)
VALUES('CFR',1907,1,'tekkz','Anfield');

INSERT INTO Coach(Co_name,Crating,nationality,Co_type)
VALUES ('Pavel','bad','Romania','defenders coach'),
('Dumitru','average','Romania','goalkeeper coach'),
('Guardiola','excelent','Spain','head coach'),
('Petrescu','good','Romania','head coach'),
('Mourinho','excelent','Portugal','head coach');

INSERT INTO Squad(Sname,rating,Cname)
VALUES ('FRANARII',78,'CFR'),('RTG',87,'CFR');

UPDATE Squad
SET rating=80
WHERE Sname='FRANARII' and NOT(rating=80) and Cname IS NOT NULL

UPDATE Squad
SET rating=90
where rating BETWEEN 86 AND 88

INSERT INTO Squad_enrollment(Sname,Pl_name,[contract])
VALUES ('RTG','Gini Wijnaldum',36),
('RTG','Alex Paun',6),
('FRANARII','Juan Culio',3),
('RTG','Virgil Van Dijk',31),
('RTG','Sergio Aguero',28),
('RTG','Lucas Moura',3),
('FRANARII','Billel Omrani',21),
('FRANARII','Neymar Jr',1),
('FRANARII','Alex Sandro',6);

INSERT INTO Tournament(tid,type,tname)
VALUES (1,'cup','Champions Cup'),(2,'league','Prem'),(3,'knockout','KO');

INSERT INTO Tournament_enrollment(Cname,tid)
VALUES ('CFR',1),('CFR',2);

INSERT INTO Squad_coaching(Co_name,Sname,[contract])
VALUES ('Dumitru','FRANARII',10),
('Petrescu','FRANARII',5),
('Mourinho','RTG',21),
('Petrescu','RTG',5);








SELECT * from Player

SELECT * from Coach

SELECT * from Squad

SELECT * from Gamer

SELECT * from Stadium

SELECT * from Weekend_League

SELECT * from Squad_enrollment

--------------------A UNION----------------------------

--Find the names of the players who have a rating better than 84 or who are from Brazil--

SELECT P.Pl_name from Player P
where P.Pl_rating>84
UNION
SELECT P2.Pl_name from Player P2
where P2.Pl_nationality='Brazil'
ORDER BY P.Pl_name

--Find the names of the coaches who are Romanian or French--

SELECT C.Co_name from Coach C
where C.nationality='Romania' or C.nationality='France'

------------------B. INTERSECT-------------------------

--Find the names of the players who are from the Netherlands and are enrolled in a squad--

SELECT P.Pl_name from Player P
where P.Pl_nationality='Netherlands' and P.Pl_name IN (SELECT SE.Pl_name FROM Squad_enrollment SE)

SELECT P.Pl_name from Player P
where P.Pl_nationality='Netherlands'
INTERSECT
SELECT SE.Pl_name from Squad_enrollment SE

---------------------C. EXCEPT------------------------------

--Find the names of the clubs that are enrolled in the first tournament but not the third---

SELECT T1.Cname from Tournament_enrollment T1
where T1.tid=1
EXCEPT
SELECT T2.Cname from Tournament_enrollment T2
where T2.tid=3

SELECT T1.Cname from Tournament_enrollment T1
where T1.tid=1 AND T1.Cname NOT IN (SELECT T2.Cname from Tournament_enrollment T2
					   where T2.tid=3)
					  
--------------------D. JOINS---------------------------------

---find all player's contracts; include the squads that they are contracted to---

SELECT * from Player P INNER JOIN Squad_enrollment S ON P.Pl_name=S.Pl_name INNER JOIN Squad Sq ON S.Sname=Sq.Sname

---find all player's contracts including players not being in a team---

SELECT * from Player P LEFT JOIN Squad_enrollment S ON P.Pl_name=S.Pl_name

---find all the squads and their coaches; including coaches that don't coach a team---

SELECT * from Squad_coaching S RIGHT JOIN Coach C ON S.Co_name=C.Co_name

---find all the players with their coaches and teams, include coaches who don't coach squads and players with no choach---

SELECT P.Pl_name,P.Pl_rating,P.Pl_nationality,S.Sname,S.rating, SE.[contract],C.Co_name,C.Crating,C.nationality 
FROM PLAYER P FULL JOIN Squad_enrollment SE ON P.Pl_name=SE.Pl_name
FULL JOIN Squad S ON SE.Sname=S.Sname
FULL JOIN Squad_coaching SC ON S.Sname=SC.Sname
FULL JOIN Coach C ON C.Co_name=SC.Co_name

-----------------E.IN------------------

---find all squads that have at least 4 players---

SELECT S.Sname from Squad S
WHERE S.Sname in (SELECT SE.Sname from Squad_enrollment SE GROUP BY SE.Sname HAVING COUNT(*)>=4)

---find the names of the squads that contain argentinian players---

SELECT Sname from Squad
WHERE Sname in (SELECT Sname from Squad_enrollment where Pl_name in (SELECT Pl_name from Player where Pl_nationality='Argentina'))


---H. GROUP BY---

---find the highest rating of a player, who is at least 80 rated, from each nationality that has at least 3 players---

SELECT P.Pl_nationality, MAX(P.Pl_rating) AS MaxRtg FROM Player P 
WHERE P.Pl_rating>=80 GROUP BY P.Pl_nationality HAVING COUNT(*) >= 3

---find the nationalities who have more players than than coaches---

SELECT COUNT(P.Pl_name) AS NumberPlayers, P.Pl_nationality FROM Player P
GROUP BY P.Pl_nationality
HAVING COUNT(P.Pl_name) > (SELECT COUNT(C.Co_name) FROM Coach C
							WHERE C.nationality=P.Pl_nationality)

---find the nationalities who have player ratings average >= 75---

SELECT P.Pl_nationality, AVG(P.Pl_rating) AS AVGR From Player P
GROUP BY P.Pl_nationality HAVING AVG(P.Pl_rating)>=75

---find the types of coaches in which all the coaches are of 'excelent' or 'good' rating---

SELECT COUNT(C.Co_name) as NumberCoaches,C.Co_type from Coach C
Group by C.Co_type
having COUNT(C.Co_name) = (SELECT COUNT(C2.Co_name) from Coach C2 where C2.Co_type=C.Co_type and (C2.Crating='excelent' or C2.Crating='good'))

-----------------------F. EXISTS------------------

---find the tournaments in which at least one club is registered---

SELECT T.tid from Tournament T
where EXISTS(SELECT TE.tid from Tournament_enrollment TE where TE.tid=T.tid)

---find the nationalities of the players who are free agents (not registered in any squad)---

SELECT DISTINCT P.Pl_nationality from Player P
where NOT EXISTS(SELECT SE.Pl_name from Squad_enrollment SE where SE.Pl_name=P.Pl_name)

-------------------G. FROM----------------------

---find the average rating of the players at the club---

SELECT AverageRating
from(SELECT AVG(Pl_rating) as AverageRating from Player) as PlayerRtg

---find the nationalities of the players in the club sorted descendetly---

SELECT Pl_nationality
from(SELECT Pl_nationality from Player group by Pl_nationality) as PlayerNat order by Pl_nationality desc

-------------------I. ANY & ALL--------------------------------

---find the player with the highest rating----

SELECT Pl_name, Pl_rating from Player
where Pl_rating >= ALL(SELECT P.Pl_rating from Player P)

SELECT Pl_name, Pl_rating from Player
where Pl_rating >= (SELECT MAX(P.Pl_rating) from Player P)

---find the best two brazilian players with a rating bigger the rating of a romanian player---

SELECT TOP 2 Pl_name, Pl_rating from Player
where Pl_nationality='Brazil' AND Pl_rating > ANY (SELECT P.Pl_rating from Player P where P.Pl_nationality='Romania')

SELECT TOP 2 Pl_name, Pl_rating from Player
where Pl_nationality='Brazil' AND Pl_rating > (SELECT MIN(P.Pl_rating) from Player P where P.Pl_nationality='Romania')

---find the nationalities of all coaches that aren't head coaches---

SELECT DISTINCT nationality from Coach
where Co_name <> ALL (SELECT C.Co_name from Coach C where C.Co_type='head coach')

---all the names---
SELECT * from Coach
where Co_name NOT IN (SELECT C.Co_name from Coach C where C.Co_type='head coach') ORDER BY Co_name DESC

---find all players with contracts of at least 1 remianig game and at most 10---

SELECT * from Squad_enrollment
where Pl_name = ANY (SELECT SE.Pl_name from Squad_enrollment SE where SE.[contract]>=1 AND SE.[contract]<=10)

---find all players with contracts of at most 10 remianig games or at least 30 who don't play for FRANARII squad---

SELECT * from Squad_enrollment
where Pl_name IN (SELECT SE.Pl_name from Squad_enrollment SE where (SE.[contract]<=10 OR SE.[contract]>=30) AND NOT(SE.Sname='FRANARII'))
