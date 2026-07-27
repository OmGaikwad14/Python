# indentation - tab/4 spacing

light = "pink"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("Light is broken")

marks = int(input("enter student marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student ->", grade)

# Nesting

age = int(input("enter age: "))

if(age >= 18):
    if(age >= 70):
        print("can not drive over age")
    else:
        print("can drive")
else:
    print("cannot drive")