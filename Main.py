from Barrio import Neighborhood
from Ciudad import City
from Estado import State
from Pais import Country
from Continente import Continent
from Base import List


while True:

    Input = input("1 - Add\n"
                  "2 - Delete\n"
                  "3 - Update\n"
                  "4 - Population\n"
                  "5 - Stats\n"
                  "6 - Exit\n")

    if Input == "1":
        while True:
            Input = input("1 - Add Neighborhood\n"
                          "2 - Add City\n"
                          "3 - Add State\n"
                          "4 - Add Country\n"
                          "5 - Add Continent\n"
                          "6 - Exit\n")

    elif Input == "2":
        while True:
            Input = input("1 - Delete Neighborhood\n"
                          "2 - Delete City\n"
                          "3 - Delete State\n"
                          "4 - Delete Country\n"
                          "5 - Delete Continent\n"
                          "6 - Exit\n")

    elif Input == "3":
        while True:
            Input = input("1 - Update Neighborhood\n"
                          "2 - Update City\n"
                          "3 - Update State\n"
                          "4 - Update Country\n"
                          "5 - Update Continent\n"
                          "6 - Exit\n")

    elif Input == "4":
        Print("")

    elif Input == "5":
        Lista1.Write()

    elif Input == "6":
        exit()
