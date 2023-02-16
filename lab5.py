#lab 5 if statement in python

#3.1
alien_color = 'yellow'
if alien_color == 'green' :
    print('you got 5 points')
    
#3.2
alien_color = 'green'
if alien_color == 'green' :
    print('you got five points')
else:
    print('you got ten points')

#3.3
favorite_fruits = ['kiwi', 'green apple', 'blackberries']
if 'kiwi' in favorite_fruits :
    print('You love kiwi')
else:
    print('Kiwi is not your favorite')
if 'banana' in favorite_fruits :
    print('You love bananas')
else:
    print('Bananas are not your favorite')
if 'blackberries' in favorite_fruits :
    print('You love blackberries')
else:
    print('Blackberries are not your favorite')

#3.4
age = 66
if age<10 :
    print('person is kid')
elif 20>age>=10 :
    print('person is teenager')
else :
    print('person is adult')
    if age>=65 :
        print('person is elder')