# 1. Store following word meanings in a python dictionary :

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}

print(dictionary)

""" 2. You are given a list of subjects for students. Assume one classroom is required for 1
    subject. How many classrooms are needed by all students. """

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print(len(subjects))

""" 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
    an empty dictionary & add one by one. Use subject name as key & marks as value"""

marks  = {}

x = int(input("Enter phy: "))
marks.update({"phy" : x})

x = int(input("Enter chem: "))
marks.update({"chem" : x})

x = int(input("Enter math: "))
marks.update({"math" : x})

print(marks)

""" 4. Figure out a way to store 9 & 9.0 as separate values in the set. 
    (You can take help of built-in data types)"""

values = {9, "9.0"}

print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)