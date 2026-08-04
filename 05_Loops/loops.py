# 1. While Loop

count = 1 # Iterators

while count <= 5:
    print("Hello", count) # Iteration
    count += 1

print(count)

i = 1

while i <= 5:
    print(i)
    i += 1

print("Loop ended")

j = 5

while j >= 1:
    print(j)
    j -= 1

# Break & Continue

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter value: "))
i = 0

while i < len(tup):
    if(tup[i] == x):
        print("FOUND", x, "at idx", i)
        break
    else:
        print("Finding..")
    i += 1

i = 0

while i <= 10 :
    if (i%2 == 0):
        i += 1
        continue # act as skip
    print(i)
    i += 1

# 2. For Loop

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

veggies = ["potato", "brijal", "ladyfinger", "cucumber"]

for val in veggies:
    print(val)

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for num in tup:
    print(num)

str = "omgaikwad"

for char in str:
    if(char == 'k'):
        print("k found")
        break
    print(char)
else:
    print("END")

# 3. range(start?, stop, step?)

sqe = range(5)

for el in sqe:
    print(el)

for el in range(10): # range(stop)
    print(el)

for el in range(2, 10): # range(start?, stop)
    print(el)

for el in range(2, 10, 2): # range(start?, stop, step)
    print(el)

for el in range(1, 101, 2):
    print("Odd num:", el)

for el in range(5):
    pass # for empty loop

print("some useful work")
