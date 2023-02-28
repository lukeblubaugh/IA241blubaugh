# lecture 7 while loop

i = 5
while i > 0:
    i = i-1
    
    if i == 3:
        pass
    
    print(i)
    
try:
    print(1/0)
except:
    print('error')

i = 5
while i >= 5:
    i = i - 1
    try:
        print(1/(i - 3))
    except:
        pass