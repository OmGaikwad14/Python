# 1. Read mode

f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

f = open("demo.txt", "w") # 2. Write mode
f = open("demo.txt", "a") # 3. Append mode

f.write("I want to learn JavaScript tomorrow.")
f.write("\nThen I'll move to React.js")
f.write("\nAfter that node.js")

f.close()

# 4. create a new file and open it for writing

f = open("sample.txt", "x")
f.close()

# 5. open a disk file for updating (reading 'r+' and writing 'w+')

f = open("demo.txt", "r+") # overwrite - No truncate
f.write("abc")
print(f.read())
f.close()

f = open("demo.txt", "w+") # overwrite - Truncate: empty file
f.write("abc")
print(f.read())
f.close()

f = open("demo.txt", "a+") # No truncate
f.write("abc")
print(f.read())
f.close()

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("New Data")

import os

os.remove("sample.txt")