
#lec 4
#dictionaries and tuple

my_tuple = ('a','b','c','d','e')

print(my_tuple[0:2])

my_car = { 
    'color':'purple',
    'maker':'honda',
    'year':'2017'
         }
print(my_car)

print(my_car['color'])

print(my_car.items())

print(my_car.keys())

print(my_car.values())

print(my_car.get('color'))

print(my_car['color'])

my_car['model']='odyssey'

print(my_car)

my_car['model']='accord'

print(my_car)

print(len(my_car))

print('color' in my_car)

print('make' in my_car)

print('purple' in my_car.values())