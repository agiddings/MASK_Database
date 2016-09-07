from flask import Flask, render_template, request, json
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)
# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mask'
app.config['MYSQL_DB'] = 'MASK'
app.config['MYSQL_HOST'] = 'localhost'

currentUser = ''

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/main")
def showMain():
    return render_template('index.html')

def tupletolistextra(data):
    list = []
    for element in data:
        list.append(element[0])
    return list


@app.route("/extraLanguageSearch")
def extraLanguageSearch():
    countrylist = query("SELECT Country FROM COUNTRY")
    return render_template('extralanguagesearch.html', countrylist=tupletolistextra(countrylist))


@app.route('/loadExtraLanguageResult', methods=['POST', 'GET'])
def loadExtraLanguage():
    if request.method == 'POST':
        print('ok')
        country = request.form['countryDropDown']
        queryResult = query('SELECT City FROM ' + country + 'Lang NATURAL JOIN ' + country + 'City;')
        print(queryResult)
        if len(queryResult) < 1:
            print(currentUser + 'lll')
            return render_template("noresult.html")
        else:
            return render_template("extralanguageresult.html", result1=tupletolist(queryResult))


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Username FROM NORMAL_USER WHERE Username='" + _name + "' AND Email='" + _email + "' AND UserPassword='" + _password + "';")
    data = cursor.fetchall()
    if len(data) < 1:
        cursor.execute(
            "INSERT INTO NORMAL_USER(Username, Email, UserPassword) VALUES ('" + _name + "', '" + _email + "', '" + _password + "');")
        conn.commit()
        global currentUser
        currentUser = _email
        return render_template('search.html')
    return render_template('signupresult.html')


@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')

#Used for drop down menus
def tupletolist(data):
    list = []
    list.append("")
    for element in data:
        list.append(element[0])
    return list

def tupletolistMakeReview(data):
    list = []
    for element in data:
        list.append(element[0])
    return list

#Navigates to the city page. The lists populate the drop down menus
@app.route('/city')
def city():
    citylist = query("SELECT City FROM CITY")
    countrylist = query("SELECT Country FROM COUNTRY")
    languagelist = query("SELECT DISTINCT Lang FROM CITY_LANGUAGE")
    return render_template("city.html", citylist=tupletolist(citylist), countrylist=tupletolist(countrylist), languagelist=tupletolist(languagelist))

#Navigates to the search page, but only if they are a user of a manager
@app.route('/search')
def search():
    isuser = query("SELECT * FROM NORMAL_USER WHERE Username='" + currentUser + "';")
    ismanager = query("SELECT * FROM MANAGER WHERE Mgr_Username='" + currentUser + "';")
    if (isuser or ismanager):
        return render_template('search.html')
    else:
        return render_template('signin.html')

#Navigates to a page that shows all of the reviews made by users, but only if they are a user
@app.route('/showreview')
def showreview():
    global currentUser
    isuser = len(query("SELECT * FROM NORMAL_USER WHERE Email='" + currentUser + "';")) > 0
    print(isuser)
    if (isuser and currentUser):
        reviewlist = query("SELECT Subject, ReviewDate, Score, Description FROM REVIEW WHERE Username='" + currentUser + "';")
        return render_template('showreview.html', reviewlist=tupletolistreview(reviewlist))
    else:
        return render_template('search.html')

#Navigates to a page for free or discount location options
@app.route('/freeordiscount')
def freeordiscount():
    citylist = query("SELECT City FROM City;")
    return render_template('freeordiscount.html', citylist=tupletolist(citylist))

#Navigates to a page that allows managers to add a city, only goes if they are a manager
@app.route('/addcity')
def addcity():
    if (len(query("SELECT * FROM MANAGER WHERE Mgr_Email='" + currentUser + "';")) > 0 and currentUser):
        countrylist = query("SELECT Country FROM COUNTRY")
        languagelist = query("SELECT DISTINCT LANG FROM CITY_LANGUAGE")
        return render_template('addcity.html', countrylist=tupletolist(countrylist), languagelist=tupletolist(languagelist))
    else:
        return render_template('search.html')

#Goes to a page where they can see the highest/lowest rating
@app.route('/ratings')
def ratings():
    ratinglist = []
    ratinglist.append('Highest rated city')
    ratinglist.append('Lowest rated city')
    ratinglist.append('Highest rated location')
    ratinglist.append('Lowest rated location')
    ratinglist.append('Highest rated event')
    ratinglist.append('Lowest rated event')
    citylist = query("SELECT City FROM CITY")
    citylanguagelist = query("SELECT DISTINCT Lang FROM CITY_LANGUAGE")
    return render_template('ratings.html', ratinglist= ratinglist, citylist = tupletolist(citylist), languagelist=tupletolist(citylanguagelist))

#Goes to a page where they can search for countries
@app.route('/country-search')
def countrysearch():
    countrylist = query("SELECT Country FROM COUNTRY")
    languagelist = query("SELECT DISTINCT LANG FROM COUNTRY_LANGUAGE")
    return render_template('country-search.html', countrylist=tupletolist(countrylist), languagelist=tupletolist(languagelist))

#Goes to a page where they can search for events
@app.route('/event')
def event():
    citylist = query("SELECT City FROM CITY")
    eventlist = query("SELECT Event_Name FROM MASKEVENT")
    categorylist = query("SELECT DISTINCT Category FROM MASKEVENT")
    return render_template('event.html', citylist=tupletolist(citylist), eventlist=tupletolist(eventlist), categorylist=tupletolist(categorylist))

#Goes to a page where they can search for locations
@app.route('/location')
def location():
    locationlist = query("SELECT Location_Name FROM Location")
    citylist = query("SELECT City FROM CITY")
    typelist = query("SELECT DISTINCT LocationType FROM LOCATION")
    return render_template('location.html', locationlist=tupletolist(locationlist), citylist=tupletolist(citylist), typelist=tupletolist(typelist))


def tupletolisteventcrap(data):
    CLevent = []
    tempS = ''
    print(data)
    for lst in data:
        CLevent.append(lst[0] + ', ' + lst[1] + ', ' + lst[2] + ', ' + str(lst[3]) + ', ' + str(lst[4]))
        tempS = ''
    return CLevent

def tupletolistlc(data):
    masterlist = []
    for element in data:
        list = []
        list.append(element[0])
        list.append(element[1])
        masterlist.append(list)
    return masterlist

def tupletolistcitycrap(data):
    CLevent = []
    tempS = ''
    print(data)
    for lst in data:
        CLevent.append(lst[0] + ', ' + lst[1])
        tempS = ''
    return CLevent

#Goes to a page where they can make a review if they are a user
@app.route('/makereview')
def makereview():
    isuser = len(query("SELECT * FROM NORMAL_USER WHERE Email='" + currentUser + "';"))
    if (isuser and currentUser):
        events = query('SELECT City, Address, Event_Name, EventDate, Start_Time FROM MASKEVENT')
        CLevent = tupletolisteventcrap(events)
        print(CLevent)
        locations = (query('SELECT City, Location_Name FROM LOCATION'))
        CLocation = tupletolistcitycrap(locations)
        cities = tupletolistMakeReview(query('SELECT City FROM CITY'))
        events = CLevent + CLocation + cities
        for string in events:
            print(string)
        return render_template('review.html', Subjects=events)
    else:
        return render_template('search.html')

#Goes to update review page
@app.route('/updatereview')
def updatereview():
    global currentUser
    ismanager = len(query("SELECT * FROM MANAGER WHERE Mgr_Username='" + currentUser + "';")) > 0
    if (ismanager):
        return render_template('search.html')
    isuser = len(query("SELECT * FROM NORMAL_USER WHERE Email='" + currentUser + "';")) > 0
    if (isuser and currentUser):
        data = query('SELECT DISTINCT Subject FROM REVIEW')
        return render_template('updatereview.html', subjectlist=tupletolist(data))
    else:
        return render_template('search.html')

#Goes to a page where they can update a review, key is username and date
@app.route('/loadupdatereview', methods=['POST'])
def loadupdatereview():
    if request.method == 'POST':
        subject = str(request.form['subjectDropDown'])
        date = str(request.form['inputdate'])
        score = str(request.form['score'])
        description = str(request.form['description'])
        username = query("SELECT Username FROM Normal_User WHERE Email='" + currentUser + "';")[0][0]
        query("UPDATE REVIEW SET Score='" + score + "', Description='" + description
                + "' WHERE Subject='" + subject + "' AND " + "Username='" + username + "' AND ReviewDate='" + date + "';")
        return render_template('search.html')

@app.route('/countryindividual/<country>')
def countryindividual(country):
    countryresult = query("SELECT * FROM COUNTRY WHERE Country='" + country + "';")
    cityresult = query("SELECT * FROM CITY WHERE Country='" + country + "';")
    return render_template('countryindividual.html', result = countryresult, city = cityresult)

@app.route('/cityindividual/<city>.html')
def cityindividual(city):
    print(str(city))
    cityresult = query("SELECT * FROM CITY NATURAL JOIN CITY_LANGUAGE WHERE City='" + str(city) + "';")
    locationresult = query("SELECT City, Location_Name FROM Location WHERE City='" + str(city) + "';")
    reviewid = query("SELECT Review_ID FROM City WHERE City='" + str(city) + "';")
    reviewlist = query("SELECT * FROM REVIEW WHERE Review_ID='" + str(reviewid[0][0]) + "';")
    print(reviewid)
    return render_template('cityindividual.html', result=tupletolistcitynoscore(cityresult),
                           locationresult=tupletolistlc(locationresult), reviewlist = tupletolistreview(reviewlist))


@app.route('/locationindividual/<location>')
def locationindividual(location):
    location = location.replace("\'", "\\'")
    print(location)
    locationresult = query("SELECT * FROM LOCATION WHERE Location_Name='" + str(location) + "';")


    address = query("SELECT Address FROM LOCATION WHERE Location_Name='" + str(location) + "';")[0][0]
    eventresult = query("SELECT * FROM MASKEVENT WHERE Address='" + str(address) + "';")
    reviewid = query("SELECT Review_ID FROM LOCATION WHERE Location_Name='" + str(location) + "';")
    print(reviewid)
    locationreview = query("SELECT * FROM REVIEW WHERE Review_ID='" + str(reviewid[0][0]) + "';")
    return render_template('locationindividual.html', result = tupletolistlocationratings(locationresult),
                           event = tupletolisteventratings(eventresult), reviewlist = tupletolistreview(locationreview))

@app.route('/eventindividual/<event>')
def eventindividual(event):
    eventresult = query("SELECT * FROM MASKEVENT WHERE Event_Name='" + str(event) + "';")
    reviewid = query("SELECT Review_ID FROM MASKEVENT WHERE Event_Name='" + str(event) + "';")
    eventreview = query("SELECT * FROM REVIEW WHERE Review_ID ='" + str(reviewid[0][0]) + "';")
    return render_template('eventindividual.html', result = tupletolisteventratings(eventresult), reviewlist = tupletolistreview(eventreview))

@app.route('/capitalcities')
def capitalcities():
    capitalcities = query("SELECT * FROM CAPITALS")
    return render_template("capitalcities.html", result=tupletolistcapital(capitalcities))

#Signs in a user
@app.route('/signIn', methods=['POST', 'GET'])
def signIn():
    if request.method == 'POST':
        _email = request.form['inputName']
        _password = request.form['inputPassword']

        conn = mysql.connection
        cursor = conn.cursor()


        if (_email.split("@")[1] == "gttravel.com"):
            cursor.execute("SELECT Mgr_Email FROM MANAGER WHERE Mgr_Email='" + _email + "';")
        else:
            cursor.execute("SELECT Email FROM NORMAL_USER WHERE Email='" + _email + "' AND UserPassword='" + _password + "';")

        data = cursor.fetchall()

        loginSucceeded = ["Please enter your email again", "Please enter your password again"]

        if len(data) > 0:
            global currentUser
            currentUser = data[0][0]
            loginSucceeded = ['Login successful', 'Login successful']
            return render_template("search.html")

        return render_template("signinresult.html")


#Super helpful method for doing queries. Thanks Steven
def query(queryString):
    conn = mysql.connection
    cursor = conn.cursor()

    cursor.execute(queryString)
    data = cursor.fetchall();
    conn.commit()
    return data

#Main method
@app.route("/loadMain")
def loadMain():
    return render_template('index.html')

#Calculates results from event page
@app.route('/loadEvent', methods=['POST', 'GET'])
def loadEvent():
    if request.method == 'POST':
        date = str(request.form['inputdate'])
        cost1 = str(request.form['lowerbound'])
        cost2 = str(request.form['upperbound'])
        event = str(request.form['eventDropDown'])
        city = str(request.form['cityDropDown'])
        category = str(request.form['categoryDropDown'])
        if (date and event and city and category):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "' AND City='" + city + "' AND Category='" + category + "';")
        if (date and event and city and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "' AND City='" + city + "';")
        if (date and event and not(city) and category):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "' AND Category='" + category + "';")
        if (date and event and not(city) and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "';")
        if (date and not(event) and city and category):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND City='" + city + "' AND Category='" + category + "';")
        if (date and not(event) and city and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND City='" + city + "';")
        if (date and not(event) and not(city) and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "';")
        if (not(date) and event and city and category):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "' AND City='" + city + "' AND Category='" + category + "';")
        if (not(date) and event and city and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "' AND City='" + city + "' AND Category='" + category + "';")
        if (not(date) and event and city and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE EventDate='" + date + "' AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "' AND City='" + city + "' AND Category='" + category + "';")
        if (not(date) and event and not(city) and category):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "' AND Category='" + category + "';")
        if (not(date) and event and not(city) and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Event_Name='" + event + "';")
        if (not(date) and not(event) and city and category):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND City='" + city + "' AND Category='" + category + "';")
        if (not(date) and not(event) and city and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND City='" + city + "';")
        if (not(date) and not(event) and not(city) and category):
            print("hi")
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE AND Cost<='" + cost2 + "' AND Cost>='" + cost1
                                + "' AND Category='" + category + "';")
        if (not(date) and not(event) and not(city) and not(category)):
            eventresult = query("SELECT * FROM MASKEVENT NATURAL LEFT JOIN AverageRating WHERE Cost<='" + cost2 + "' AND Cost>='" + cost1 + "';")
        if (len(tupletolist(eventresult)) < 1):
            return render_template("noresult.html")
        else:
            return render_template("eventresult.html", result=tupletolistevent(eventresult))

#Calculates results from city page
@app.route('/loadCity', methods=['POST', 'GET'])
def loadCity():
    if request.method == 'POST':
        country = request.form['countryDropDown']
        pop1 = request.form['lowerbound']
        pop2 = request.form['upperbound']

        city = str(request.form['cityDropDown'])
        print(city)
        language = request.form['languageDropDown']
        print(language)
        if (country and language and city):
            cityResult = query("SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating WHERE COUNTRY='" + country + "' AND POPULATION >='" + pop1
                               + "' AND POPULATION <='" + pop2
                               + "' AND City='" + city + "' AND Lang='" + language + "';")
            print(cityResult)
            print("calling here")
        if(country and language and not(city)):
            cityResult = query(
                "SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating WHERE COUNTRY='" + country + "' AND POPULATION >='" + pop1
                + "' AND POPULATION <='" + pop2
                + "' AND Lang='" + language + "';")
        if(country and not(language) and city):
            cityResult = query(
                "SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating WHERE COUNTRY='" + country + "' AND POPULATION >='" + pop1
                + "' AND POPULATION <='" + pop2
                + "' AND City='" + city + "' AND Lang='" + language + "';")
        if (country and not(language) and not(city)):
            cityResult = query(
                "SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating WHERE COUNTRY='" + country + "' AND POPULATION >='" + pop1
                + "' AND POPULATION <='" + pop2
                + "';")
        if(not(country) and language and city):
            cityResult = query(
                "SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating WHERE City='" + city + "' AND POPULATION >='" + pop1
                + "' AND POPULATION <='" + pop2
                + "' AND Lang='" + language + "';")
        if (not (country) and language and not(city)):
            cityResult = query(
                "SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating WHERE Lang='" + language + "' AND POPULATION >='" + pop1
                + "' AND POPULATION <='" + pop2
                + "';")
        if(not(country) and not(language) and city):
            cityResult = query(
                "SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating WHERE City='" + city + "' AND POPULATION >='" + pop1
                + "' AND POPULATION <='" + pop2
                + "';")
        if(not(country) and not(language) and not(city)):
            cityResult = query(
                "SELECT DISTINCT * FROM CITY NATURAL JOIN CITY_LANGUAGE NATURAL LEFT JOIN AverageRating;")
        if (len(tupletolistcity(cityResult)) < 1):
            return render_template("noresult.html")
        else:
            return render_template("cityresult.html", result=tupletolistcity(cityResult))

#Calculates results from country page
@app.route('/loadCountry', methods=['POST', 'GET'])
def loadCountry():
    if request.method == 'POST':
        pop1 = request.form['lowerbound']
        pop2 = request.form['upperbound']
        country = request.form['countryDropDown']
        language = str(request.form['languageDropDown'])

        if (country and language):
            countryresult = query(
                "SELECT DISTINCT Country, Population FROM COUNTRY NATURAL JOIN COUNTRY_LANGUAGE NATURAL JOIN CAPITALS WHERE COUNTRY='" + country + "' AND POPULATION>='" + pop1+ "' AND POPULATION<='" + pop2
                + "' AND Lang='" + language + "';")
        if (country and not (language)):
            countryresult = query(
                "SELECT DISTINCT Country, Population, City FROM COUNTRY NATURAL JOIN COUNTRY_LANGUAGE NATURAL JOIN CAPITALS WHERE COUNTRY='" + country + "' AND POPULATION>='" + pop1+ "' AND POPULATION<='" + pop2
                + "';")
        if (not (country) and language):
            countryresult = query(
                "SELECT DISTINCT Country, Population, City FROM COUNTRY NATURAL JOIN COUNTRY_LANGUAGE NATURAL JOIN CAPITALS WHERE POPULATION>='" + pop1+ "' AND POPULATION<='" + pop2
                + "' AND Lang='" + language + "';")
        if (not (country) and not (language)):
            countryresult = query(
                "SELECT DISTINCT Country, Population, City FROM COUNTRY NATURAL JOIN COUNTRY_LANGUAGE NATURAL JOIN CAPITALS WHERE POPULATION>='" + pop1+ "' AND POPULATION<='" + pop2 + "';")
        if len(tupletolistcountrycapital(countryresult)) < 1:
            return render_template("noresult.html")
        else:
            return render_template("countryresult.html", result=tupletolistcountrycapital(countryresult))

def getCountryLanguage(country):
    return query("SELECT Lang FROM COUNTRY NATURAL JOIN COUNTRY_LANGUAGE WHERE COUNTRY='" + country + "';")

def getCityLanguage(city):
    return query("SELECT Lang FROM CITY NATURAL JOIN CITY_LANGUAGE WHERE City='" + city + "';")

#Calculates results from location page
@app.route('/loadLocation', methods=['POST'])
def loadLocation():
    location = str(request.form['locationDropDown'])
    city = str(request.form['cityDropDown'])
    cost1 = str(request.form['lowerbound'])
    cost2 = str(request.form['upperbound'])

    category = str(request.form['categoryDropDown'])

    if (location and city and category):
        locationresult = query("SELECT * FROM LOCATION NATURAL LEFT JOIN AverageRating WHERE LOCATION_NAME='" + location + "' AND City='" + city
                               + "' AND COST<='" + cost2 + "' AND COST>='" + cost1 + "' AND LocationType='" + category + "' ORDER BY LocationType;")

    if (location and city and not (category)):
        locationresult = query("SELECT * FROM LOCATION NATURAL LEFT JOIN AverageRating WHERE LOCATION_NAME='" + location + "' AND City='" + city
                               + "' AND COST<='" + cost2 + "' AND COST>='" + cost1  + "' ORDER BY LocationType;")
    if (location and not (city) and category):
        locationresult = query("SELECT * FROM LOCATION NATURAL LEFT JOIN AverageRating WHERE LOCATION_NAME='" + location + "' AND COST<='" + cost2 + "' AND COST>='" + cost1
                               + "' AND LocationType='" + category + "' ORDER BY LocationType;")
    if (location and not (city) and not (category)):
        locationresult = query("SELECT * FROM LOCATION NATURAl LEFT JOIN AverageRating WHERE LOCATION_NAME='" + location + "' AND COST<='" + cost2 + "' AND COST>='" + cost1  + "' ORDER BY LocationType;")
    if (not (location) and city and category):
        locationresult = query("SELECT * FROM LOCATION NATURAL LEFT JOIN AverageRating WHERE CITY='" + city
                               + "' AND COST<='" + cost2 + "' AND COST>='" + cost1  + "' AND LocationType='" + category + "' ORDER BY LocationType;")
    if (not (location) and city and not (category)):
        locationresult = query("SELECT * FROM LOCATION NATURAL LEFT JOIN AverageRating WHERE CITY='" + city
                               + "' AND COST<='" + cost2 + "' AND COST>='" + cost1  + "' ORDER BY LocationType;")
    if (not (location) and not (city) and category):
        locationresult = query("SELECT * FROM LOCATION NATURAL LEFT JOIN AverageRating WHERE COST<='" + cost2 + "' AND COST>='" + cost1
                               + "' AND LocationType='" + category + "' ORDER BY LocationType;")
    if (not (location) and not (city) and not (category)):
        locationresult = query("SELECT * FROM LOCATION NATURAL LEFT JOIN AverageRating WHERE COST<='" + cost2 + "' AND COST>='" + cost1
                               + "' ORDER BY LocationType;")
    if (len(tupletolistlocation(locationresult)) < 1):
        return render_template("noresult.html")
    else:
        return render_template("locationresult.html", result=tupletolistlocation(locationresult))

#Adds a city based on user input
@app.route('/loadAddCity', methods=['POST'])
def loadAddCity():
    cityname = str(request.form['cityname'])
    countryname = str(request.form['countryDropDown'])
    population = str(request.form['population'])
    gpslong = str(request.form['GPSlong'])
    gpslang = str(request.form['GPSlang'])
    language = str(request.form['languageDropDown'])

    highestIDCity = int(query("SELECT Max(Review_ID) FROM CITY;")[0][0])
    highestIDLocation = int(query("SELECT Max(Review_ID) FROM LOCATION;")[0][0])
    highestIDEvent = int(query("SELECT Max(Review_ID) FROM MASKEVENT;")[0][0])
    reviewid = str(max(max(highestIDCity, highestIDLocation), highestIDEvent) + 1)
    print(reviewid)
    query("INSERT INTO REVIEWABLE VALUES ('" + reviewid + "');")
    query("INSERT INTO CITY VALUES ('" + countryname + "', '" + cityname + "', '" + gpslong + "', '" + gpslang + "', '"
          + reviewid + "', '" + population + "');")
    print('inserted into city values')
    query("INSERT INTO CITY_LANGUAGE VALUES ('" + countryname + "', '" + cityname + "', '" + language + "');")
    print('inserted into city language')
    return render_template('search.html')


def tupletolistbonus(data):
    masterlist = []
    for element in data:
        dict = {'Location Name': element[0], 'Individual Cost': element[1], 'Location Type': element[2], 'Total Cost': element[3]}
        masterlist.append(dict)
    return masterlist


def tupletolistbogus(data):
    list = []
    for element in data:
        list.append(element[0])
    return list

@app.route('/loadbonus', methods=['POST'])
def loadbonus():
    cityname = str(request.form['cityDropDown'])
    locationtype = str(request.form['ltypeDropDown'])
    data = query(
        "SELECT Location_Name, Cost, LocationType, Total FROM (SELECT Location_Name, Cost, LocationType FROM LOCATION WHERE City='" + cityname + "' AND LocationType='" + locationtype + "') l1"
        + " NATURAL JOIN (SELECT LocationType, SUM(Cost) AS Total FROM LOCATION WHERE City='" + cityname + "' GROUP BY LocationType) l2;")
    print(data)
    print(tupletolistbonus(data))
    return render_template("loadbonus.html", result=tupletolistbonus(data))


@app.route('/bonus')
def bonus():
    cities = query("SELECT DISTINCT City FROM CITY;")
    ltype = query("SELECT DISTINCT LocationType FROM LOCATION;")
    print(cities)
    print(ltype)
    return render_template('bonus.html', citylist=tupletolistbogus(cities), ltypelist=tupletolistbogus(ltype))

#Loads results of free or student discount events in a location
@app.route('/loadFreeOrDiscount', methods=['POST'])
def loadFreeOrDiscount():
    city = str(request.form['cityDropDown'])



    
    if(city):
        results = query("SELECT MASKEVENT.Country, MASKEVENT.City, MASKEVENT.Address, MASKEVENT.Event_Name, "
                    "MASKEVENT.EventDate, MASKEVENT.Start_Time, MASKEVENT.End_Time, MASKEVENT.STD_Discount, "
                    "MASKEVENT.Description, MASKEVENT.Category, MASKEVENT.Cost, "
                    "AverageRating.Score FROM City as C, MASKEVENT "
                    "NATURAL LEFT JOIN AverageRating WHERE (MASKEVENT.STD_Discount='1' OR MASKEVENT.Cost ='0') "
                    "AND C.CITY= MASKEVENT.CITY and C.City ='" + city +"';")
    else:
        results = query("SELECT MASKEVENT.Country, MASKEVENT.City, MASKEVENT.Address, MASKEVENT.Event_Name, "
                    "MASKEVENT.EventDate, MASKEVENT.Start_Time, MASKEVENT.End_Time, MASKEVENT.STD_Discount, "
                    "MASKEVENT.Description, MASKEVENT.Category, MASKEVENT.Cost, "
                    "AverageRating.Score FROM MASKEVENT "
                    "NATURAL LEFT JOIN AverageRating WHERE (MASKEVENT.STD_Discount='1' OR MASKEVENT.Cost ='0') "
                    ";")

    if len(results) < 1:
        return render_template("noresult.html")
    else:
        return render_template('freeordiscountresult.html', result=tupletofreeordiscount(results))

#Adds a review based on user input
@app.route('/addreview', methods=['POST'])
def addreview():
    if request.method == 'POST':
        subject = str(request.form['Subjects'])
        date = str(request.form['inputdate'])
        score = str(request.form['score'])
        description = str(request.form['description'])
        subj = subject.split(', ')
        reviewid = []
        if len(subj) == 5:
            reviewid = query("SELECT Review_ID FROM MASKEVENT WHERE City='" + subj[0] + "' AND Address='" + subj[1] + "' AND Event_Name='"
                              + subj[2] + "' AND EventDate='"
                              + subj[3] + "' AND Start_Time='" + subj[4] + "';")
        elif len(subj) == 2:
            reviewid = query("SELECT Review_ID FROM LOCATION WHERE City='" + subj[0] + "' AND Location_Name='" + subj[1] + "';")
        else:
            reviewid = query("SELECT Review_ID FROM CITY WHERE City='" + subj[0] + "';")
        #reviewid = [list(x) for x in reviewid]
        #reviewid = ''.join(reviewid)
        reviewid1 = str(reviewid[0][0])
        global currentUser
        username = query("SELECT Username FROM NORMAL_USER WHERE Email='" + currentUser + "';")[0][0]
        query("INSERT INTO REVIEW(Username, Subject, ReviewDate, Score, Description, Review_ID) VALUES ('" + str(username) + "', '" + subject + "', '" + date + "', '" + score
              + "', '" + description + "', '" + reviewid1 + "');")
        return render_template('search.html')

#Shows all reviews to the user
@app.route('/loadRatings', methods=['POST'])
def loadRatings():

    if request.method == 'POST':

        forma = str(request.form['ratingDropDown'])

        city = str(request.form['cityDropDown'])

        language = str(request.form['citylanguageDropDown'])
        if (forma == 'Highest rated city' and not(language)):
            ratingsresult = query("SELECT Country, City, Longitude, Latitude, Population, MAX(Score) FROM (CITY NATURAL JOIN AverageRating);")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistcityratings(ratingsresult)
                return render_template('cityratingsresult.html', result=result)
        if (forma == 'Lowest rated city' and not (language)):
            ratingsresult = query("SELECT Country, City, Longitude, Latitude, Population, MIN(Score) FROM (CITY NATURAL JOIN AverageRating);")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistcityratings(ratingsresult)
                return render_template('cityratingsresult.html', result=result)
        if (forma == 'Highest rated city' and language):
            ratingsresult = query("SELECT Country, City, Longitude, Latitude, Population, MAX(Score) FROM (CITY NATURAL JOIN "
                                  + "AverageRating NATURAL JOIN CITY_LANGUAGE) WHERE Lang='" + language + "';")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistcityratings(ratingsresult)
                return render_template('cityratingsresult.html', result=result)
        if (forma == 'Lowest rated city' and language):
            ratingsresult = query("SELECT Country, City, Longitude, Latitude, Population, MIN(Score) FROM (CITY NATURAL JOIN "
                                  + "AverageRating NATURAL JOIN CITY_LANGUAGE) WHERE Lang='" + language + "';")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistcityratings(ratingsresult)
                return render_template('cityratingsresult.html', result=result)
        if (forma == 'Highest rated location' and not(city)):
            ratingsresult = query(
                "SELECT Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, MAX(Score) FROM (Location NATURAL JOIN AverageRating);")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template('locationratingsresult.html', result=result)
        if (forma == 'Lowest rated location' and not (city)):
            ratingsresult = query(
                "SELECT Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, MIN(Score)"
                + " FROM (Location NATURAL JOIN AverageRating);")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template('locationratingsresult.html', result=result)
        if (forma == 'Lowest rated location' and city):
            ratingsresult = query("SELECT Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, MIN(Score)"
                                  + " FROM (Location NATURAL JOIN AverageRating) WHERE City ='" + city + "';")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template('locationratingsresult.html', result=result)
        if (forma == 'Highest rated location' and city):
            ratingsresult = query(
                "SELECT Country, City, Address, Location_Name, Cost, LocationType, STD_Discount, MAX(Score) "
                + "FROM (Location NATURAL JOIN AverageRating) WHERE City='" + city + "';")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template('locationratingsresult.html', result=result)
        if (forma == 'Highest rated event' and city):
            ratingsresult = query("SELECT Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, "
                                  + "Category, Cost, MAX(Score) FROM (MASKEVENT NATURAL JOIN AverageRating) WHERE City='" + city + "';")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template("eventratingsresult.html", result=result)
        if (forma == 'Highest rated event' and not(city)):
            ratingsresult = query(
                "SELECT Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, "
                + "Category, Cost, MAX(Score) FROM (MASKEVENT NATURAL JOIN AverageRating);")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template("eventratingsresult.html", result= result)
        if (forma == 'Lowest rated event' and not(city)):
            ratingsresult = query(
                "SELECT Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, "
                + "Category, Cost, MIN(Score) FROM (MASKEVENT NATURAL JOIN AverageRating);")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template("eventratingsresult.html", result=result)
        if (forma == 'Lowest rated event' and city):
            ratingsresult = query(
                "SELECT Country, City, Address, Event_Name, EventDate, Start_Time, End_Time, STD_Discount, Description, "
                + "Category, Cost, MIN(Score) FROM (MASKEVENT NATURAL JOIN AverageRating) WHERE City='" + city + "';")
            if (len(ratingsresult) < 1):
                return render_template("noresult.html")
            else:
                result = tupletolistlocationratings(ratingsresult)
                return render_template("eventratingsresult.html", result=result)

#Converts country tuples to a list
def tupletolistcountry(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[0], 'Population': element[1]}
        masterlist.append(dict)
        languages = getCountryLanguage(element[0])
        dict['Language0'] = languages[0][0]
        if (len(languages) > 1):
            dict['Language1'] = languages[1][0]
            if (len(languages) > 2):
                dict['Language2'] = languages[2][0]
        masterlist.append(dict)
    return masterlist

#Converts country tuples to a list with capital
def tupletolistcountrycapital(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[0], 'Population': element[1], 'Capital': element[2]}
        masterlist.append(dict)
        languages = getCountryLanguage(element[0])
        dict['Language0'] = languages[0][0]
        if (len(languages) > 1):
            dict['Language1'] = languages[1][0]
            if (len(languages) > 2):
                dict['Language2'] = languages[2][0]
        masterlist.append(dict)
    print(masterlist)
    return masterlist

#Converts city tuples to a list
def tupletolistcity(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[1], 'City': element[2], 'Longitude': element[3], 'Latitude': element[4],
                'Population': element[5], 'Score': element[7]}
        languages = getCityLanguage(element[2])
        dict['Language0'] = languages[0][0]
        if (len(languages) > 1):
            dict['Language1'] = languages[1][0]
            if (len(languages) > 2):
                dict['Language2'] = languages[2][0]
        masterlist.append(dict)
    return masterlist

#Converts city tuples to a list
def tupletolistcitynoscore(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[0], 'City': element[1], 'Longitude': element[2], 'Latitude': element[3],
                'Population': element[5]}
        languages = getCityLanguage(element[1])
        dict['Language0'] = languages[0][0]
        if (len(languages) > 1):
            dict['Language1'] = languages[1][0]
            if (len(languages) > 2):
                dict['Language2'] = languages[2][0]
        masterlist.append(dict)
    return masterlist

def tupletolistcapital(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[0], 'City': element[1]}
        masterlist.append(dict)
    return masterlist

#Converts city tuples to a list
def tupletolistcitycapital(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[1], 'City': element[2], 'Longitude': element[3], 'Latitude': element[4],
                'Population': element[5], 'Score': element[7]}
        languages = getCityLanguage(element[2])
        dict['Language0'] = languages[0][0]
        if (len(languages) > 1):
            dict['Language1'] = languages[1][0]
            if (len(languages) > 2):
                dict['Language2'] = languages[2][0]
        masterlist.append(dict)
    return masterlist

#Converts city tuples to a list
def tupletolistcityratings(data):
    masterlist = []
    for element in data:
        list = []
        list.append(element[0])
        list.append(element[1])
        list.append(element[2])
        list.append(element[3])
        list.append(element[4])
        list.append(element[5])
        masterlist.append(list)
    return masterlist


def tupletolisteventratings(data):
    masterlist = []
    for element in data:
        list = []
        list.append(element[0])
        list.append(element[1])
        list.append(element[2])
        list.append(element[3])
        list.append(element[4])
        list.append(element[5])
        list.append(element[6])
        list.append(element[7])
        list.append(element[8])
        list.append(element[9])
        list.append(element[10])
        list.append(element[11])
        masterlist.append(list)
    return masterlist


def tupletofreeordiscount(data):
    masterlist = []
    for element in data:
        list = []
        list.append(element[0])
        print(element[0])
        list.append(element[1])
        list.append(element[2])
        list.append(element[3])
        list.append(element[4])
        list.append(element[5])
        list.append(element[6])
        list.append(element[7])
        list.append(element[8])
        list.append(element[9])
        list.append(element[10])
        masterlist.append(list)
    return masterlist

def tupletolistlocationratings(data):
    masterlist = []
    for element in data:
        list = []
        list.append(element[0])
        list.append(element[1])
        list.append(element[2])
        list.append(element[3])
        list.append(element[4])
        list.append(element[5])
        list.append(element[6])
        list.append(element[7])
        masterlist.append(list)
    return masterlist

#Converts event tuples to a list
def tupletolistevent(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[1], 'City': element[2], 'Address': element[3], 'Event_Name': element[4], 'EventDate': element[5],
                'Start_Time': element[6], 'End_Time': element[7], 'STD_Discount': element[8], 'Description': element[9],
                'Category': element[10], 'Cost': element[11], 'Score': element[12]}
        masterlist.append(dict)
    return masterlist

#Converts location tuples to a list
def tupletolistlocation(data):
    masterlist = []
    for element in data:
        dict = {'Country': element[1], 'City': element[2], 'Address': element[3], 'Location_Name': element[4],
                'Cost': element[5], 'LocationType': element[6], 'STD_Discount': element[7], 'Score': element[8]}
        masterlist.append(dict)
    return masterlist

#Converts review tuples to a list
def tupletolistreview(data):
    masterlist = []
    for element in data:
        list = []
        list.append(element[0])
        list.append(element[1])
        list.append(element[2])
        list.append(element[3])
        masterlist.append(list)
        print(list)
    return masterlist

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
