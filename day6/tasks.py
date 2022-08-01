#q1: Create a class Vehicle with attributes: color, brand, vehicle_type(car,bike,truck, etc.),number_of_wheels(make default=4),price. Then create its object, along with a method to access its brand, vehicle type and price. 
class vehicle:
    def __init__(self):
        color = 'white'
        brand = 'yatri'
        vehicle_type = 'bike'
        number_of_wheels = 2
        price = 1800000

    def get_data(self,color='green',brand='yamuna',vehicle_type='car',number_of_wheels=4,price=1500000):
        print(color,brand,vehicle_type,number_of_wheels,price)


v = vehicle()
v.get_data('red','tata','car',4,1500000)
v.get_data()