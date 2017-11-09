import pymysql
from Barrio import Neighborhood
from Ciudad import City
from Estado import State
from Pais import Country
from Continente import Continent


class List (object):

    db = None
    c = None

    def __init__(self):
        self.db = pymysql.connect(host="localhost", user='root', passwd='', db='mydb', autocommit=True)
        self.c = self.db.cursor(pymysql.cursors.DictCursor)

    def InsertNeighbourhood(self, neighbourhood):
        self.c.execute(
            "insert into Barrio values('" + neighbourhood.ID + "', '" + neighbourhood.Name + "', '" + neighbourhood.Population + "')")

    def InsertCity(self, city):
        self.c.execute(
            "insert into Ciudad values('" + city.ID + "', '" + city.Name + "')")

    def InsertState(self, state):
        self.c.execute(
            "insert into Estado values('" + state.ID + "', '" + state.Name + "')")

    def InsertCountry(self, country):
        self.c.execute(
            "insert into Pais values('" + country.ID + "', '" + country.Name + "')")

    def InsertContinent(self, continent):
        self.c.execute(
            "insert into Continente values('" + continent.ID + "', '" + continent.Name + "')")