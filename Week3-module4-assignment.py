# Exercise1 print out all numbers divisible by three in the range of 1-1000.
num = 1
while 1 <= num <= 1000:
    if num % 3 ==0:
        print(f'{num}, is divisible by 3!')
    num += 1

# Exercise2 converts inches to centimeters until the user inputs a negative value.
inches= float(input("Enter inches:"))
centimeters = inches * 2.54
while inches >= 0:
    print(f'{inches} equals to {centimeters}')
    inches = float(input("Enter inches:"))
print('Ends')

# Exercise3 asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
num_list = [] #using list function
while True:
    num = input("Enter a number or enter "" to stop")
    if num != "":
        num_list.append(int(num))
    else:
        break
num_list.sort()
print(f'The min number you put is {num_list[0]}, and the max one is {num_list[-1]}')


largest = smallest = None
while True:
    user_num = input("Enter a number or enter "" to stop")
    if user_num == "":
        break
    number = float(user_num)
    if largest is not None and largest > number:
        largest = number
    if smallest is not None and smallest < number:
        smallest = number
    if smallest is None and largest is None:
        smallest = number
        largest = number

print(largest)
print(smallest)

# Exercise4 guess number
import random
num = random.randint(1,10)
while True:
    i = int(input("Guess a number between 1 and 10"))
    if i == num:
        print("Correct!")
        break
    elif i < num:
        print("Too low!")
    elif i > num:
        print("Too high!")

# Exercise5 Write a program that asks the user for a username and password.
attempts = 0

while  attempts < 5 :
    username = input("Enter your username:")
    password = input("Enter your code:")

    if username == "python" and password == "rules":
        print("welcome")
        break
    else:
        print("Wrong username or password!")
        attempts += 1

if attempts == 5:
    print("Assess denied")

# Exercise6 calculating an approximation for the value of pi (π)
import random
points = int(input("Enter how many points to generate"))
inCircle = 0
counter = 0

while counter < points:
    xOfPoint = float(random.uniform(-1, 1))
    yOfPoint = float(random.uniform(-1, 1))

    if xOfPoint**2 + yOfPoint **2 <= 1: #the point is in
        inCircle += 1
    counter +=1

pi = 4 * inCircle / points
print(pi)