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


# Q2. create a class Point where initial x,y values are initialized with 0.
#  a. create objects of class Point with x and y values passed to it. 
#    Eg. Point p1 with x = 2 and y with y= 3 should be created.
#  b. Create a method to Calculate distance between two points.
#   Formula res = sqrt((x2-x1)^2 +(y2-y1)^2), where x1 and x2 are x values of p1 and p2 points resp. , y1 and y2 are y values of p1 and p2 respectively.
#  c. Represent the point objects with x,y values in the format (x,y). Eg:(2,3).
import math
class Point:
    def __init__(self):
        x = 0
        y = 0
    
    def getvalue(self,x,y):
        print(x,y)

    def distform(self,x,y):
        print('hello')
        res = math.sqrt((p1.x-p2.x)^2 +(p1.y-p2.y)^2)
        print(res)

p1 = Point()
p2 = Point()
p1.getvalue(10,12)
p1.distform(5, 6)

