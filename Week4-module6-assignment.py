print('Module 6')
print("question1")
import random
def roll_dice():
    return random.randint(1,6)

def main():
   roll = 0
   while roll != 6:
       roll = roll_dice()
       print(f'you roll is {roll}')
main()


print("question2")
import random

def main():
    side = int(input("Decide how many sides you want:"))
    roll = 0
    while roll < side :
        roll = roll_dice(side)
        print(f'you roll is {roll}')
    print("you got the biggest number")

def roll_dice(side):
    return random.randint(1,side)

main()

print("question3")
def gasoline_litre(gallon_quantity):
    return round((gallon_quantity * 3.79),2)

def main():

    while True:
        gallon_quantity = int(input("How many gallons:"))

        if gallon_quantity < 0:
            print("You give a negative number")
            break
        else:
            print(f'{gallon_quantity} gallons is {gasoline_litre(gallon_quantity)}litres')

main()


print("question4")
numbers = []

def st1(numbers):
    return sum(numbers)

def main():
    while True:
        number = input("Enter a number or enter Q to quit").upper()

        if number == "Q":
            break
        numbers.append(int(number))

    print(st1(numbers))

main()



print("question5")

def even(numbers):
    return [number
            for number in numbers if number % 2 == 0]

def main():
    numbers = []
    numbers_cut = []

    while True:
        number = input("Enter a number or enter Q to quit").upper()
        if number == "Q":
            break
        else:
            numbers.append(int(number))
        numbers_cut= even(numbers)

    print(numbers_cut)
    print(numbers)

main()
print(type(is_uneven_you_will_die))


print("question6")

def unit_price(cm,price):
    area =3.14 * (cm/2) **2 / 10000
    unit_price = round(price/area,2)
    return unit_price

def main():
    unit_price_list = []
    for i in range(2):
        cm = float(input("Enter the diameter of your pizza in cm:"))
        price = float(input("Enter the total price of your pizza in euro:"))
        calculate_price=unit_price(cm,price)
        unit_price_list.append(calculate_price)

    if unit_price_list[0] > unit_price_list[1]:
        print(f'The second one is affordable.')
    elif unit_price_list[0] < unit_price_list[1]:
        print(f'The first one is affordable.')
    else:
        print(f'The unit price is the same.')

main()
