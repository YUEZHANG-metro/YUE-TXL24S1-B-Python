# module 7
print('question 1')
season = ['spring','summer','autumn','winter']
number_of_month = int(input('Enter a number of months(1-12):'))
if number_of_month in (12,1,2):
    print(f"Is {season[3]}");
elif number_of_month in (3,4,5):
    print(f"Is {season[0]}");
elif number_of_month in (6,7,8):
    print(f"Is {season[1]}");
else:
    print(f"Is {season[2]}")


print('question 2')
nameSet = {'suzy','mike','lily','joe'}

while True:
    name = input("Enter a name or enter to stop")
    if name == '':
        break
    if name in nameSet:
        print("Existing name")
    else:
        print("New name")
print('Stopped')


print('question 3')
airport = {
    'ZBAA': 'Beijing Capital International Airport',
    'ZBAD': 'Beijing Daxing International Airport',
    'ZGBH': 'Beihai Fucheng Airport'}

while True:
    choices = input('Enter a new airport(enter N) or '
                    'fetch airport information(enter F) or '
                    'quit(Enter Q')

    if choices == 'Q':
        print('you choose to stop')
        break

    elif choices == 'N'.upper():
        name = input('Enter an airport name')
        icao_code = input('Enter an icao code')
        airport[name] = icao_code;
        print(f'you enter a new airport{name} by code {icao_code}')

    elif choices == 'F'.upper():
        icao_code = input('Enter an icao code')
        if icao_code in airport.keys():
            print(f'the airport of your {icao_code} is {airport[icao_code]}')