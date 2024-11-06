class Car:
    def __init__(self,registration_number, maximum_speed,
                 current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = int(maximum_speed)
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


    def change_initial_speed(self, given_speed):
        self.current_speed = given_speed
        return self.current_speed

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

class ElectricCar(Car):
    def __init__(self,registration_number, maximum_speed,capacity_battery):
        super().__init__(registration_number, maximum_speed)
        self.capacity_battery = capacity_battery
        pass

    def print_kilometers(self,hours):
        self.drive(hours)
        print(f"{self.registration_number} runs {self.travelled_distance} in {hours} hours")

class GasolineCar(Car):
    def __init__(self,registration_number, maximum_speed,volume_tank):
        super().__init__(registration_number, maximum_speed)
        self.volume_tank = volume_tank
        pass

    def print_kilometers(self,hours):
        self.drive(hours)
        print(f"{self.registration_number} runs {self.travelled_distance} in {hours} hours")


car1 = ElectricCar("ABC-15",180,52.5)
car2 = GasolineCar("ACD-123",165,32.3)

car1.change_initial_speed(100)
car2.change_initial_speed(120)
car1.print_kilometers(3)
car2.print_kilometers(3)

