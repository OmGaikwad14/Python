# 1. WAF to print the length of a list. ( list is the parameter)

cities = ["Delhi", "Mumbai", "Pune", "Gujrat", "Banglore"]

def print_len(list):
    print(len(list))

print_len(cities)

# 2. WAF to print the elements of a list in a single line. ( list is the parameter)

heroes = ["Thor", "Ironman", "Captain America", "Shaktiman"]

def print_list(list):
    for items in list:
        print(items, end=" ")

print_list(heroes)

# 3. WAF to find the factorial of n!. (n is the parameter)

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(6)

# 4. WAF to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(73)

# Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Mango", "Litchi", "Apple", "Banana"]

print_list(fruits)