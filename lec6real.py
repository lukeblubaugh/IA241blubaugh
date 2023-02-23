#lecture 6 for loop
#prior mistake with numbering, this is the actual lecture 6

for num in [1,2,3]:
    print(num)

for str_item in 'this is my string':
    print(str_item)

for num in [1,2,3]:
    print(num+1)
    print(num)

for c in 'this is lecture 6'.split():
    print(c)

for c in 'i do not like python at all'.split():
    print(c)

for num in [1,2,3]:
    if num>1:
        print(num)

for num in [5,89,32,7,12,77,1000]:
    if num>21:
        print(num)
    
for word in 'this is lec6'.split():
    print(word)
    for c in word:
        print(c)
        
for i in range(1,100,10):
    print(i)

#for i in range(1,1000000000000000000000000000000000000000000):
  #  print(i)

for i in range(1,5):
    print(i)
    
my_num_list = [213,321,123,312]

possible_max_num = my_num_list[0]

for num in my_num_list:
    if num > possible_max_num:
        possible_max_num = num

print(possible_max_num)


