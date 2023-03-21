# lecture 9 class

import lec8

print(lec8.calculate_abs(-9))

class car:
    maker = 'Toyota'
#    def report_maker(self):
#        return self.maker
    def __init__(self,input_model):
        self.model = input_model
    def report(self):
        return self.maker,self.model
my_camry = car('Camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())
#print(my_car_instance.report_maker())

my_highlander = car('Highlander')
print(my_highlander.maker)
print(my_highlander.model)

my_camry.maker = 'Ford'
print(my_camry.report())

import numpy
print(numpy)