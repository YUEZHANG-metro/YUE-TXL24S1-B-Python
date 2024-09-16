print('Question1')
#Write a program that asks the user to enter the ICAO code of an airport.
#what is ICAO https://en.wikipedia.org/wiki/ICAO_airport_cod
import mysql.connector

def get_ai_info(ICAO):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (ICAO,))
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! The airport with that ICAO code is {row[1]} located at {row[0]}.")
    else:
        print("No results found.")
    cursor.close()

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='110422'
)

ICAO = input("Enter an ICAO code: ")
get_ai_info(ICAO)

connection.close()

print('question 2')
def get_code_info(area_code):
    sql = (f"SELECT airport.name,airport.type "
           f"FROM airport JOIN country "
           f"ON airport.iso_country = country.iso_country "
           f"WHERE country.iso_country = %s ORDER BY airport.type;")

    cursor = connection.cursor()
    cursor.execute(sql,(area_code,))
    result = cursor.fetchall() #get back tuple

    heliport_counter = 0
    small_counter = 0
    medium_counter = 0
    closed_counter = 0
    large_counter = 0

    if cursor.rowcount > 0:
        for row in result:
            airport_type = row[1]
            if airport_type == 'heliport':
                heliport_counter += 1
            elif airport_type == 'small_airport':
                small_counter += 1
            elif airport_type == 'medium_airport':
                medium_counter += 1
            elif airport_type == 'closed':
                closed_counter += 1
            elif airport_type == 'large_airport':
                large_counter += 1
        print(f'{area_code} has {heliport_counter} heliport, {large_counter} large airport, {small_counter} small airport'
              f'and {medium_counter} medium and {closed_counter} closed')

    cursor.close()

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='110422',
)

code = input("Enter a code: ")
get_code_info(code)
connection.close()


print('Question3')
# 1.input two airport name(check if is in the list)
# 2.get the latitude_deg and longitude_deg
# 3.use distance.distance

import mysql.connector
from geopy import distance
name1 = input("Enter an airport name")
name2 = input("Enter another airport name")
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='110422')

def get_distance(name1, name2):
    sql = ("Select latitude_deg,longitude_deg FROM airport "
           "WHERE name IN (%s,%s)") #using to %s to have two parameters
    cursor = connection.cursor()
    cursor.execute(sql, (name1, name2))
    result = cursor.fetchall()
    if len(result) == 2:
        latitude1,longitude1= result[0]
        latitude2,longitude2= result[1]
        airport1 = (latitude1,longitude1)
        airport2 = (latitude2,longitude2)
        distance_airports = distance.distance(airport1,airport2) .km
        print(f'Distance between two airports id {distance_airports:.2f} km')
    else:
        print("Try other airports")
    cursor.close()

get_distance(name1,name2)
connection.close()







