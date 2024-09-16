print('Question1')
# Write a program that asks the user to enter the ICAO code of an airport.
# what is ICAO https://en.wikipedia.org/wiki/ICAO_airport_cod
import mysql.connector

def get_ai_info(ICAO):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{ICAO}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
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

def get_code_info(code):
    sql = (f"SELECT airport.name,airport.type "
           f"FROM airport JOIN country "
           f"ON airport.iso_country = country.iso_country "
           f"WHERE country.iso_country = %s ORDER BY airport.type;")

    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql,(code,))
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
        print(f'{code} has {heliport_counter} heliport, {large_counter} large airport, {small_counter} small airport'
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
