## Exercise 10 Association
import random
import prettytable

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = int(maximum_speed)
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def change_initial_speed(self, given_speed):
        self.current_speed = given_speed
        return self.current_speed

    # def change_travelled_distance(self, new_travelled_distance):
    #     self.travelled_distance = new_travelled_distance
    #     return self.travelled_distance

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

    # def __str__(self):
    #     return (f"The car numbered {self.registration_number} has a maximum speed {self.maximum_speed} km/h, "
    #             f"and the current speed is {self.current_speed} km/h, travelled {self.travelled_distance} km")

class Race:
    def __init__(self, name:str, kilometers:int, car_list:list):
        self.name = name
        self.kilometers = kilometers
        self._car_list = car_list

    def add_car(self,car):
        self._car_list.append(car)
        return self._car_list

    def hour_passes(self,hours:int):
        for car in self._car_list:
            car.drive(hours)
        return f"{car.registration_number} moves {car.travelled_distance} km "

    def print_status(self):
        table= prettytable.PrettyTable(["registration_number","current_speed","travelled_distance"])
        for car in self._car_list:
            table.add_row([car.registration_number, car.current_speed, car.travelled_distance])
        print(table)

    def race_finished(self):
        for car_instance in self._car_list:
            if car_instance.travelled_distance >= self.kilometers :
                return f"{car_instance.registration_number} has finished the race"

GDD_list = []
race1 = Race("Grand Demolition Derby",8000,GDD_list)


car_number = 1
while len(GDD_list) < 10:
    registration_number = f'ABC-{car_number}'
    car_number += 1
    maximum_speed = random.randint(100, 200)
    GDD_list.append(Car(registration_number,maximum_speed))
    for car in GDD_list:
        # it is more close to a real life that the car is start at a speed instead of 0.
        car.change_initial_speed(100)
        car.accelerate(random.randint(-10, 15))

play_hour = 0
while True:
    if race1.race_finished():
        print(f"{race1.race_finished()}")
        break
    else:
        play_hour += 1
        race1.hour_passes(1)
        if play_hour % 10 == 0:
            race1.print_status()

print("Final race status:")
race1.print_status()