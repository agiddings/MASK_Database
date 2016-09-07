
INSERT INTO SUPPORTED_LANGUAGES VALUES ('ENGLISH');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('SPANISH');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('CATALAN');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('GERMAN');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('ITALIAN');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('FRENCH');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('FLEMISH');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('DUTCH');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('GREEK');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('VALENCIAN');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('GALICIAN');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('BASQUE(EUSKARA)');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('GAELIC');
INSERT INTO SUPPORTED_LANGUAGES VALUES ('PORTUGUESE');

INSERT INTO SUPPORTED_LOCATIONS VALUES ('MUSEUM');
INSERT INTO SUPPORTED_LOCATIONS VALUES ('STADIUM');
INSERT INTO SUPPORTED_LOCATIONS VALUES ('RESTAURANT');
INSERT INTO SUPPORTED_LOCATIONS VALUES ('PLAZA');
INSERT INTO SUPPORTED_LOCATIONS VALUES ('PARK');
INSERT INTO SUPPORTED_LOCATIONS VALUES ('MEMORIAL');
INSERT INTO SUPPORTED_LOCATIONS VALUES ('CHURCH');
INSERT INTO SUPPORTED_LOCATIONS VALUES ('OTHER');


INSERT INTO SUPPORTED_EVENTS VALUES ('CONCERT');
INSERT INTO SUPPORTED_EVENTS VALUES ('SPORTS MATCH');
INSERT INTO SUPPORTED_EVENTS VALUES ('RACE');
INSERT INTO SUPPORTED_EVENTS VALUES ('FESTIVAL');
INSERT INTO SUPPORTED_EVENTS VALUES ('PRESENTATION');

INSERT INTO COUNTRY(Country, Population) VALUES ('Spain', '48146134');
INSERT INTO COUNTRY(Country, Population) VALUES ('France', '66553766');
INSERT INTO COUNTRY(Country, Population) VALUES ('Belgium', '11323973');
INSERT INTO COUNTRY(Country, Population) VALUES ('Monaco', '37731');
INSERT INTO COUNTRY(Country, Population) VALUES ('Ireland', '4892305');

INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('Spain', 'Spanish');
INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('France', 'French');
INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('Belgium', 'French');
INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('Belgium', 'Dutch');
INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('Belgium', 'German');
INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('Monaco', 'French');
INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('Ireland', 'English');
INSERT INTO COUNTRY_LANGUAGE(Country, Lang) VALUES ('Ireland', 'Gaelic');

INSERT INTO REVIEWABLE(Review_Id) VALUES ('0');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('1');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('2');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('3');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('4');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('5');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('6');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('7');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('8');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('9');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('10');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('11');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('12');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('13');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('14');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('15');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('16');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('17');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('18');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('19');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('20');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('21');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('22');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('23');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('24');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('25');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('26');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('27');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('28');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('29');
INSERT INTO REVIEWABLE(Review_Id) VALUES ('30');

INSERT INTO CITY(Country, City, Longitude, Latitude, Review_ID, Population) VALUES ('Spain', 'Madrid', '3 41 W', '40 24 N', '0', '6489162');
INSERT INTO CITY(Country, City, Longitude, Latitude, Review_ID, Population) VALUES ('Spain', 'Barcelona', '2 11 E', '41 23 N', '1', '5375774');
INSERT INTO CITY(Country, City, Longitude, Latitude, Review_ID, Population) VALUES ('Spain', 'Valencia', '0 23 W', '39 28 N', '2', '2516818');
INSERT INTO CITY(Country, City, Longitude, Latitude, Review_ID, Population) VALUES ('Ireland', 'Dublin', '6 15 W', '53 20 N', '3', '1801040');
INSERT INTO CITY(Country, City, Longitude, Latitude, Review_ID, Population) VALUES ('France', 'Paris', '2 20 E', '48 52 N', '4', '1801040');
INSERT INTO CITY(Country, City, Longitude, Latitude, Review_ID, Population) VALUES ('Monaco', 'Monaco', '7 25 E', '43 43 N', '5', '37731');
INSERT INTO CITY(Country, City, Longitude, Latitude, Review_ID, Population) VALUES ('Belgium', 'Brussels', '4 21 E', '50 51 N', '6', '1830000');

INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Spain', 'Madrid', 'Spanish');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Spain', 'Barcelona', 'Spanish');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Spain', 'Barcelona', 'Catalan');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Spain', 'Valencia', 'Spanish');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Spain', 'Valencia', 'Valencian');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Ireland', 'Dublin', 'English');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Ireland', 'Dublin', 'Gaelic');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('France', 'Paris', 'French');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Monaco', 'Monaco', 'French');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Belgium', 'Brussels', 'French');
INSERT INTO CITY_LANGUAGE(Country, City, Lang) VALUES ('Belgium', 'Brussels', 'Dutch');

INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES ('Spain', 'Madrid', '101 Disney World', 'Retiro Park', '0', 'Park', '0', '11');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES   ('Spain', 'Madrid', '102 Disney World', 'The Prado', '15', 'Museum', '1', '12');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES ('Spain', 'Madrid', '103 Disney World', 'Royal Palace', '13', 'Museum', '1', '13');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES  ('Spain', 'Madrid', '104 Disney World', 'Opera House', '0', 'Other', '0', '14');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES  ('Spain', 'Madrid', '105 Disney World', 'Reina Sofia', '17', 'Museum', '1', '15');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES   ('Spain', 'Barcelona', '106 Disney World', 'Arc d\'Triomf', '0', 'Other', '0', '16');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES  ('Spain', 'Barcelona', '107 Disney World', 'Camp Nou', '0', 'Stadium', '0', '17');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES   ('Spain', 'Barcelona', '108 Disney World', 'Sagrada Familia', '15', 'Church', '1', '18');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES  ('Spain', 'Barcelona', '109 Disney World', 'Parc Guell', '8', 'Park', '0', '19');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES  ('Spain', 'Barcelona', '110 Disney World', 'Teatre Apolo', '0', 'Other', '0', '20');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES ('France', 'Paris', '111 Disney World', 'Eiffel Tower', '14', 'Other', '1', '21');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES ('France', 'Paris', '112 Disney World', 'Louvre', '25', 'Museum', '1', '22');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES  ('France', 'Paris', '113 Disney World', 'Notre Dame', '0', 'Church', '0', '23');
INSERT INTO LOCATION(Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, Review_ID) VALUES  ('France', 'Paris', '114 Disney World', 'Moulin Rouge', '0', 'Restaurant', '0', '24');

INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('Spain', 'Barcelona', '106 Disney Way', 'Beauty and the Beast Sing Along', '2016-04-25', '18:00', '20:30', '1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Concert', '15', '7');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('Spain', 'Barcelona', '109 Disney Way', 'Animating Finding Dory', '2016-8-1', '19:30', NULL, '0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Presentation', '0', '8');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('Spain', 'Barcelona', '110 Disney Way', 'Brother Bear Live', '2016-5-6', '15:00', '17:00', '0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Concert', '20', '9');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('Spain', 'Barcelona', '109 Disney Way', 'Why Jane Is A Boss', '2016-6-9', '17:30', NULL, '1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Presentation', '5', '10');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('Spain', 'Barcelona', '106 Disney Way', 'Beauty and the Beast Sing along', '2016-7-16', '20:00', '22:30', '0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Concert', '15', '25');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('Spain', 'Barcelona', '107 Disney Way', 'Olaf vs Sven', '2016-7-3', '20:00', '23:00', '0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Sports Match', '30', '26');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('France', 'Paris', '111 Disney Way', 'Race to Defeat the Huns', '2016-5-9', '12:00', NULL, '0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Race', '40', '27');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('France', 'Paris', '112 Disney Way', 'Disney Convention', '2016-1-25', '19:00', '23:00', '0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Festival', '35', '28');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('France', 'Paris', '111 Disney Way', 'Race to See the Floating Lanterns', '2016-3-22', '6:00', '12:00', '0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Race', '50', '29');
INSERT INTO MASKEVENT(Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, Category, Cost, Review_ID) VALUES	('France', 'Paris', '114 Disney Way', 'Brother Bear Live', '2016-6-1', '15:00', '17:00', '1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Concert', '20', '30');

INSERT INTO NORMAL_USER(Username, Email, UserPassword) VALUES ('Allie', 'sass@gatech.edu', 'mask');
INSERT INTO NORMAL_USER(Username, Email, UserPassword) VALUES ('Kalya', 'sassss@gatech.edu', 'mask');
INSERT INTO NORMAL_USER(Username, Email, UserPassword) VALUES ('Sam', 'sasss@gatech.edu', 'mask');

INSERT INTO REVIEW(Username, Subject, ReviewDate, Score, Description, Review_ID) VALUES ('Kalya', 'Test', '2012-01-01', '5', 'testy test', '1');
INSERT INTO REVIEW(Username, Subject, ReviewDate, Score, Description, Review_ID) VALUES ('Allie', 'Test', '2012-01-01', '1', 'testy test', '21');
INSERT INTO CAPITALS(COUNTRY, CITY) VALUES ('SPAIN', 'MADRID');
INSERT INTO CAPITALS(COUNTRY, CITY) VALUES ('FRANCE', 'PARIS');
INSERT INTO CAPITALS(COUNTRY, CITY) VALUES ('BELGIUM', 'BRUSSELS');
INSERT INTO CAPITALS(COUNTRY, CITY) VALUES ('MONACO', 'MONACO');      


INSERT INTO REVIEW(Username, Subject, ReviewDate, Score, Description, Review_ID) VALUES ('Sam', 'Test', '2012-01-01', '9', 'testy test', '1');
INSERT INTO REVIEW(Username, Subject, ReviewDate, Score, Description, Review_ID) VALUES ('Allie', 'Test', '2012-01-01', '5', 'testy test', '3');
INSERT INTO REVIEW(Username, Subject, ReviewDate, Score, Description, Review_ID) VALUES ('Kalya', 'Test', '2012-01-01', '10', 'testy test', '5');


CREATE VIEW AverageRating(Review_ID, Score) AS SELECT Review_ID, AVG (Score) AS Score FROM REVIEW GROUP BY Review_ID;
CREATE VIEW SpainLang AS SELECT * FROM CITY_LANGUAGE GROUP BY City HAVING COUNT(City) > 1;
CREATE VIEW SpainCity AS SELECT * FROM CITY WHERE Country LIKE 'Spain';

CREATE VIEW FranceLang AS SELECT City FROM CITY_LANGUAGE GROUP BY City HAVING COUNT(City) > 1;
CREATE VIEW FranceCity AS SELECT * FROM CITY WHERE Country LIKE 'France';

CREATE VIEW IrelandLang(COUNTRY, CITY, LANG1) AS SELECT * FROM CITY_LANGUAGE GROUP BY City HAVING COUNT(City) > 2;
CREATE VIEW IrelandCity AS SELECT * FROM CITY WHERE Country LIKE 'Ireland';

CREATE VIEW MonacoLang AS SELECT * FROM CITY_LANGUAGE GROUP BY City HAVING COUNT(City) > 1;
CREATE VIEW MonacoCity AS SELECT * FROM CITY WHERE Country LIKE 'Monaco';

CREATE VIEW BelgiumLang(COUNTRY, CITY, LANG1) AS SELECT * FROM CITY_LANGUAGE GROUP BY City HAVING COUNT(City) > 3;
CREATE VIEW BelgiumCity AS SELECT * FROM CITY WHERE Country LIKE 'Belgium';
        