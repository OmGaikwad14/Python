# Redundant - repeat
# def - function definition
""" def func_name(parameter): 
    some work
    return val
    
func_name(argument) function call """

def calc_sum(a, b):
    sum = a + b
    # print(sum)
    return sum

result = calc_sum(5, 10)
print(result)

def func_name(a, b):
    return a + b

sum = func_name(2, 4)
print(sum)

def print_hello():
    print("Hello")

print_hello()
print_hello()

# average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(8, 10, 6)

print("Om", end=" ") # sep = " "
print("Vishal") # end = \n

def calc_prod(a=2, b=5): # default parameter
    print(a * b)
    return a * b

calc_prod()
