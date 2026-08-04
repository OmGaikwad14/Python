# 1. Print numbers from 1 to 100. 

i = 1

while i <= 100:
    print(i)
    i += 1

# 2. Print numbers from 100 to 1.

i = 100

while i >= 1:
    print(i)
    i -= 1

# 3. Print the multiplication table of a number n.

n = int(input("Enter number: "))
i = 1

while i <= 10:
    print(n * i)
    i += 1

# 4. Print the elements of the following list using a loop: (traverse)

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0

while idx < len(nums):
    print(nums[idx])
    idx += 1

# 5. Linear Search for a number x in this tuple using loop:

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter value: "))
i = 0

while i < len(nums):
    if (nums[i] == x):
        print("FOUND", x, "at idx:", i)
    else:
        print("finding...")
    i += 1

# 6. Print the elements of the following list using a loop:

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

# 7. Linear Search for a number x in this tuple using loop:

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter value: "))
i = 0

for el in nums:
    if (el == x):
        print("FOUND", x, "at idx:", i)
        break
        i += 1
    else:
        print("finding...")

# 8. Print numbers from 1 to 100.

for i in range(1, 101):
    print(i)

# 9. Print numbers from 100 to 1.

for i in range(100, 0, -1):
    print(i)

# 10. Print the multiplication table of a number n.

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)

# 11. WAP to find the sum of first n numbers. (using for)

n = int(input("Enter number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

for i in range(1, n+1):
    sum += i

print("Total sum =", sum)

# 12. WAP to find the factorial of first n numbers. (using for)

n = int(input("Enter number: "))
fact = 1
i = 1

for i in range(1, n+1):
    fact *= i

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)