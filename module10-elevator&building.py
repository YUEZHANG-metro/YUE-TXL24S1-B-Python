class Elevator:
    def __init__(self,name,floor_top,floor_bottom):
        self.floor_top = floor_top
        self.floor_bottom = floor_bottom
        self.floor_number = floor_bottom
        self.name = name

    def floor_up(self):
        if self.floor_number < self.floor_top:
            self.floor_number += 1
        else:
            self.floor_number = self.floor_top
        # return self.floor_number
        print(f"{self.name} moving up to {self.floor_number}")

    def floor_down(self):
        if self.floor_number > self.floor_bottom:
            self.floor_number -= 1
        else:
            self.floor_number = self.floor_bottom
        # return self.floor_number
        print(f"{self.name} moving up to {self.floor_number}")

    def go_to_floor(self,floor_given):
        while floor_given != self.floor_number:
            if self.floor_number < floor_given:
                self.floor_up()
            elif self.floor_number > floor_given:
                self.floor_down()
        return f"{floor_given} has arrived."

    def __str__(self):
        return f"the elevator {self.name}"

class Building:
    def __init__(self,building_top,building_bottom,total_elevators):
        self.building_top = building_top
        self.building_bottom = building_bottom
        self.total_elevators = total_elevators
        self.elevators = []

    def get_elevator(self,elevator):
        self.elevators.append(elevator)
        return self.elevators

    def __str__(self):
        return f"{self.elevators} ...."

    def run_elevator(self,index_of_elevator,destination):
        elevator_instance = self.elevators[index_of_elevator]
        elevator_instance.go_to_floor(destination)
        return f"The {elevator_instance} have arrived {destination} floor."

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.floor_bottom)
        return f"All {len(self.elevators)} elevators have arrived bottom floor."


# 1.create class Elevator
h = Elevator("main",6,1)
h.go_to_floor(5)
print(h.go_to_floor(5))

h.go_to_floor(1)
print(h.go_to_floor(1))

# 2. extend the elevator.
b1= Building(7,1,3) #create building object
h1= Elevator("A",7,1)
b1.get_elevator(h1)
h2= Elevator("B",7,1)
b1.get_elevator(h2)
h3= Elevator("C",7,1)
b1.get_elevator(h3)


if len(b1.elevators) >= b1.total_elevators:
    print(f"Enough elevators")
else:
    print(f"Add more elevators")

print(b1.run_elevator(2,5))
print(b1.run_elevator(0,4))

# 3.extend the fire_alarm method
print(b1.fire_alarm())