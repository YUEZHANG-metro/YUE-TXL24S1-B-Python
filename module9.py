## Exercise 9 OOP

class Car:
    def __init__(self,registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = int(maximum_speed)
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


    def change_initial_speed(self, given_speed):
        self.current_speed = given_speed
        return self.current_speed

    def change_travelled_distance(self, new_travelled_distance):
        self.travelled_distance = new_travelled_distance
        return self.travelled_distance

    def accelerate(self, acceleration):
        self.current_speed = self.current_speed + acceleration
        # The speed of the car must stay below the set maximum and cannot be less than zero.
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        else:
            return self.current_speed

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed
        return self.travelled_distance


    def __str__(self):
        return (f"The car numbered {self.registration_number} has a maximum speed {self.maximum_speed} km/h, "
                f"and the current speed is {self.current_speed} km/h, travelled {self.travelled_distance} km")

# 1. create a new car and print out all the properties of the new car.
car1 = Car("ABC-123","142")
print(car1)

# 2. Change the speed and print it out.
car1.accelerate(30)
print(f" Car 1 current speed is {car1.current_speed}")
car1.accelerate(70)
print(f" Car 1 current speed is {car1.current_speed}")
car1.accelerate(50)
print(f" Car 1 current speed is {car1.current_speed}")
car1.accelerate(-200)
print(f" Car 1 current speed is {car1.current_speed}")

# 3.test method drive
car2= Car("ABC-1234","150")
car2.change_initial_speed(60)
car2.change_travelled_distance(2000)
car2.drive(1.5)
print(f" Car 2 runs {car2.travelled_distance} km")

# car race
import random
car_list = []
car_number = 1
while len(car_list) < 10:
    registration_number = f'ABC-{car_number}'
    car_number += 1
    maximum_speed = random.randint(100, 200)
    car_list.append(Car(registration_number,maximum_speed))
# check the car we created and their maximum speed
for car in car_list:
    print(car)


total_distance = 10000
race_time = 0

while True:
    race_time +=1
    print(f"\n--- Race Time: {race_time} hour(s) ---")
    for car in car_list:
        # it is more close to a real life that the car is start at a speed instead of 0.
        car.change_initial_speed(120)
        car.accelerate(random.randint(-10,15))
        car.drive(1)

        print(f'{car.registration_number} -> {car.current_speed} km/h, travelled {car.travelled_distance} km')

        if car.travelled_distance >= total_distance:
            print(f"{car.registration_number} win!")
            break

    else:
        continue
    break
