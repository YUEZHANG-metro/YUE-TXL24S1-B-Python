# 1.Write a program that asks your name and then greets you by your name
name= str(input("Enter your name:"))
print("Hello,",name)

import math

# 2.Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius = float(input("Enter your radius:"))
area = math.pi*radius **2
print("The area is",area)

# # 3.Write a program that asks the user for the length and width of a rectangle.
# # The program then prints out the perimeter and area of the rectangle.
# # The perimeter of a rectangle is the sum of the lengths of each four sides.
length = float(input("Enter your length:"))
width = float(input("Enter your width:"))
area = length*width
perimeter = 2*(length+width)
print("The area is",area,"The perimeter is",perimeter)
#
# # 4.Write a program that asks the user for three integer numbers.
# # The program prints out the sum, product, and average of the numbers.
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
sum = num1+num2+num3
product = num1*num2*num3
average = int(sum/3)
print(sum,product,average)

import random

# 5.Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
talents = float(input("Enter your talent:"))
pounds = float(input("Enter your pounds:"))
lots = float(input("Enter your lots:"))
total_pounds = talents* 20 + pounds
total_lots = total_pounds* 32+ lots
total_grams = total_lots* 13.3
#convert to kg
total_kilograms = int(total_grams / 1000)
remainder_grams = total_grams % 1000
print("There are",total_kilograms,"kgs,and",remainder_grams,"grams")

# 6.Write a program that draws two random combinations of numbers for a combination lock
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.
num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
codeA = f"{num1}{num2}{num3}"

num4 = random.randint(1,6)
num5 = random.randint(1,6)
num6 = random.randint(1,6)
num7 = random.randint(1,6)
codeB =f"{num4}{num5}{num6}{num7}"

print(f'The 3digit code is {codeA}')
print(f'The 3digit code is {codeB}')