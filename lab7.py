#lab 7 while loop in python

#3.1
i = -1
while i <= 4:
    i = i+1
    
    if i == 3:
        continue
    
    print(i)

#3.2
i = 1
result = 1

while i <= 5:
    result = result * i
    i = i + 1

print(result)

#3.3
i = 1
result = 0

while i <= 5:
    result = result + i
    i = i +1

print(result)

#3.4
i = 3
result = 1

while i <= 8:
    result = result * i
    i = i + 1

print(result)

#3.5
result = 8
i = 1

while result >=1:
    i = i * result
    result = result - 1

resultt = 3
k = 1

while resultt >= 1:
    k = k * resultt
    resultt = resultt -1

    
print(i/k)

#3.6

num_list = [12,32,43,35]

while num_list:
    num_list.pop()

print(num_list)
    