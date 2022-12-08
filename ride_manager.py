class RideManager:
    def __init__(self):
        print('Ride manager activated')
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []
    
    def add_a_vehicle(self,vehicle_type,vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)

    def get_available_cars(self,vehicle_type):
        return self.__available_cars


    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type == 'car':
            if len(self.__available_cars) == 0:
                print("Sorry No Cars is available")
                return False
            for car in self.__available_cars:
                print("Potential", rider.location, car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    print("Find a match for You ")
                    return True

uber = RideManager()

 

        
