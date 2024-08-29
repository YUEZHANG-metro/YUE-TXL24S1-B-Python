# Length of Zander
lengthOfZander = int(input("Enter the length of Zander: "))
belowTheLimit =None
if lengthOfZander < 42:
    belowTheLimit = 42-lengthOfZander
    print(f"The length of the fish you caught is {belowTheLimit} below the size limit.")
else:
    print("The length is over the limit, you can keep it.")

# Cabin class
cabinClass = str(input("Enter the cabin class: ")).upper()
if cabinClass == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabinClass == "A":
    print("above the car deck, equipped with a window.")
elif cabinClass == "B":
    print("windowless cabin above the car deck.")
elif cabinClass == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

# biological gender and hemoglobin value
gender = str(input("Enter your gender: (female or male)")).lower()
hemoglobin = float(input("Enter your hemoglobin:  (g/l)"))
if (gender == "female" and hemoglobin >=155) or (gender == "male" and hemoglobin >= 167):
    print("Your hemoglobin value is high!")
elif (gender == "female" and hemoglobin <= 117) or (gender == "male" and hemoglobin <= 134):
    print("Your hemoglobin value is low!")
else:
    print("Your hemoglobin value is normal.")

# Leap year
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")