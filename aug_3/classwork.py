# Create a class Employee, with attributes: name, emp_code, designation.
#   a. Generate 4 digit emp code (using static method)
#   b. Create a method to create an employee object and emp_code for it should be generated using the method: that you created in Q.3.a.
#   c. Create objects :
#        i. One directly by passing parameters to the class. 
#        ii. Another by the method you created in Q.3.b.


from ast import arg
from random import randint
from unicodedata import name


class Employee:
    def __init__(self, name='none', emp_code=0000, designation="None"):
        self.name = name
        self.emp_code = emp_code
        self.designation = designation

    @staticmethod
    def generate():
        emp_code = randint(1000,9999)
        # print("emm_code = ", emp_code)
        return emp_code

    @classmethod
    def emp_meth(cls,name,designation):
        emp_code = cls.generate()
        return cls(name,emp_code,designation)
        

a0 = Employee("Ram",1235,"student")
a1 = Employee.emp_meth('Sailesh',"Employer")

print(a0.name,a0.emp_code,a0.designation)
print(a1.name,a1.emp_code,a1.designation)

# ooutput code

