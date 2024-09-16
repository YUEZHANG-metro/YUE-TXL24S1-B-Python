# Q1 The program rolls all the dice once and prints out the sum of the numbers.
print("Question1")
import random
dice = int(input("How many dices? "))
diceSet = []
for i in range(dice):
    dic = random.randint(1,6)  #i is hard to identify,use dice_roll.
    diceSet.append(i)
sum_of_dices = sum(diceSet)
# total_sum += dice_roll
print(diceSet)
print(sum_of_dices)


print("Question2")
numbers = []
while True:
    number = input("Enter a number: or '' to quit: ")
    if number == '':
        if len(numbers) < 5:
            print(f'You add {len(numbers)} numbers, and you exit the game.')
        break

    if number.isdigit():
        numbers.append(int(number))
        print(f'you need to put {5 - len(numbers)} more numbers')
    else:
        print("Add numbers or put "" to quit")

if len(numbers) >=5:
    numbers.sort(reverse=True)
    max_five = numbers[:5]
    print(f'The largest five number is {max_five}')
else:
    print("You did not enter enough numbers.")

print("Question3")
prime_or_not = int(input("Enter a number"))
factor = range(2,prime_or_not)
for d in factor:
    if prime_or_not % d == 0:
        print(f'{prime_or_not} is not a prime number')
        break
else:
    print(f'{prime_or_not} is a prime number')

print("Question4")
cities = []
for i in range(5):
    city = input("Enter a city")
    cities.append(city)

for city in cities:
    print(city)
#list出现时，基本必须用for loop和index