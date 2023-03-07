#lecture 8 python functions

def cal_plus(input1,input2):
    result = input1+input2
    return result
print(cal_plus(12, 34))
print(cal_plus(49494, 23543))

def calculate_abs(a):
    if type(a) is str:
        return('wrong datatype')
    elif a > 0:
        return a
    else:
        return -a
print(calculate_abs(3))

def cal_sigma(m,n):
    result = 0
    for i in range(n,m+1):
        result = result + i
    return result
print(cal_sigma(10,1))

def cal_pi(m,n):
    result = 1
    for i in range(n,m+1):
        result = result * i
    return result
print(cal_pi(10,3))

def cal_f(m):
    if m == 0:
        return 1
    else:
        return m * cal_f(m-1)
print(cal_f(5))

def cal_perm(m,n):
    return cal_f(m)/cal_f(m-n)
print(cal_perm(4,2))