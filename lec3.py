
#lec3
#list and set
my_list = [1,2,3,4,5]

print (my_list)

my_nested_list = [1,2,3,my_list]

print (my_nested_list)

my_list[0]=6

print(my_list)

print(my_list[3])

print(my_list[:])

x,y = ['a','b']

print(x)
print(y)

my_list.append(7)
print(my_list)

my_list.remove(3)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

my_list + [7,3]
print(my_list + [7,3])

my_list.extend([7,3])
print(my_list)

print(7 in my_list)

print(len(my_list))

print(len(my_nested_list))

print('hello\tworld')

print('hello world\nhello brave new world')

print(len('hello world'))

print('hello|world|hello|brave|new|world'.split('|'))

print('hello world.' [0:5])

my_letters = ['a', 'a', 'b','c','b']

print(set(my_letters))

print(my_letters)

my_letters_set = set(my_letters)

print('a' in my_letters_set)

print('d' in my_letters_set)

print(list(my_letters_set)[0])

