# 1. Create a new file “practice.txt” using python. Add the following data in it:

# Hi everyone
# we are learning File I/O
# using Java. 
# I like programming in Java.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/o\n")
    f.write("using Java.\nI like programming in Java.")

# 2. WAF that replace all occurrences of “java” with “python” in above file.

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# 3. Search if the word “learning” exists in the file or not.

def check_for_word(word):
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

check_for_word("learning")

# 4. WAF to find in which line of the file does the word “learning”occur first. 
#    Print -1 if word not found.

def check_for_line(word):
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line("programming")

# 5. From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    # print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)