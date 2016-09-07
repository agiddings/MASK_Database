/*avg score*/
/*can add cities and reviews*/


/* Query 1 */
SELECT Country FROM COUNTRY WHERE Population < 1000000;

/* Query 2 */
SELECT City FROM CITY_LANGUAGE WHERE Lang LIKE 'Spanish';

/* Query 3 */
DROP VIEW FrenchCity;
CREATE VIEW FrenchCity AS SELECT * FROM CITY_LANGUAGE WHERE Lang LIKE 'French';
CREATE VIEW AverageRating AS SELECT Review_ID, AVG (Score) FROM REVIEW;
CREATE VIEW FranceRating AS SELECT * FROM FrenchCity NATURAL JOIN AverageRating;
SELECT City FROM FranceRating WHERE Score LIKE (SELECT MAX(Score) FROM FranceRating);

/*Query 4*/
CREATE VIEW SpanishLang AS SELECT * FROM CITY_LANGUAGE WHERE Lang LIKE 'Spanish' AND COUNT > 1;
CREATE VIEW SpanishCity AS SELECT * FROM CITY WHERE Country LIKE 'Spain';
SELECT City FROM SpanishLang NATURAL JOIN SpanishCity;

/* Query 5 */
CREATE VIEW BarcelonaLocation AS SELECT * FROM LOCATION WHERE CITY LIKE 'Barcelona';
/* Reuse average rating view */
CREATE VIEW BarcelonaLocationRating AS SELECT * FROM BarcelonaLocation NATURAL JOIN AverageRating;
SELECT City FROM BarcelonaLocationRating WHERE Score LIKE (SELECT MIN(Score) FROM AverageRating);


/* Query 6 */
SELECT Event_Name FROM MASKEVENT WHERE City LIKE 'Madrid' AND Category LIKE 'Museum';

/* Query 7 */
SELECT Event_Name FROM MASKEVENT WHERE City LIKE 'Barcelona' AND Category LIKE 'Concert' AND Cost > 0 AND Cost < 150;

/* Query 8 */
SELECT Location_Name FROM LOCATION WHERE CITY LIKE 'Paris' GROUP BY CATEGORY;

/* Query 9 */
CREATE VIEW BarcelonaEvent AS SELECT * FROM MASKEVENT WHERE City LIKE 'Barcelona';
/* Reuse average rating view */
CREATE VIEW BEventRating AS BarcelonaEvent NATURAL JOIN AverageRating;
SELECT City FROM BEventRating WHERE Score LIKE (SELECT MAX(Score) FROM BEventRating);

/* Query 10 */
SELECT Event_Name FROM MASKEVENT WHERE CITY LIKE 'Paris' AND COST = 0 OR STD_DISCOUNT LIKE 'Yes';


