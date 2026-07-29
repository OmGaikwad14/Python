# Strings - immutable, value are not change
# List - mutable, value are change

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["Om", 21, "Mumbai"]
print(student[0])
print(student[1])
student[0] = "Vishal"
student[1] = 22
print(student)

# List methods

list = [5, 4, 3, 5, 2, 1]
fruitList = ["banana", "litchi", "apple"]

# Slicing -> list[starting_idx : ending_idx] - ending idx is not included

print(list[0:4])
print(list[3:len(list)])
print(list[:4]) # [0:6]
print(list[4:]) # [6:len(list)]
print(list[-3:-1]) # reverse indexing

list.append(6) # Add value in last
print(list)

list.sort() # values arrange in ascending order
print(list)

list.sort(reverse=True) # values arrange in Descending order
print(list)

fruitList.sort()
print(fruitList)

fruitList.sort(reverse=True)
print(fruitList)

list.reverse() # reverse list
print(list)

fruitList.insert(1, "coconut") # insert element at index
print(fruitList)

list.remove(5) #removes first occurrence of element
print(list)

list.pop(2) # remove element at index
print(list)
