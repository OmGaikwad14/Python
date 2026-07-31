# Dictionary -> Mutable(changeable) & don't allow duplicate keys

info = {
    "key" : "value",
    "name" : "Om",
    "subjects" : ["Python", "JS", "Java"],
    "topics" : ("dict", "set"),
    "learning" : "coding",
    21 : "age",
    True : "is_adult",
    94.4 : "marks"
}

print(type(info))
print(info)

print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["learning"])

info["name"] = "Vishal" # overwrite
info["surname"] = "Babar"
print(info)

null_dict = {}
null_dict["name"] = "Om"
print(null_dict)

# Nested Dictionary

student = {
    "name" : "Om Gaikwad",
    "subjects" : {
        "phy" : 98,
        "chem" : 94,
        "math" : 99,
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

# Dictionary Methods

print(student.keys()) # return all keys
print(len(student))
print(list(student.keys()))
print(tuple(student.keys()))

print(student.values()) # return all values
print(len(student))
print(list(student.values()))
print(tuple(student.values()))

print(student.items()) # return all (key, val) pairs as tuples
print(list(student.items()))

pairs = list(student.items())
print(pairs[1])

# print(student["name2"]) # error
print(student.get("name2")) # no error -> None

new_dict = {
    "name" : "Vishal Babar", # overwrite
    "city" : "Mumbai",
    "age" : 20,
}

student.update(new_dict) # add new (key, value)
print(student)
