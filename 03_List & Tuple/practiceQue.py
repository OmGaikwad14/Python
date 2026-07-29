# 1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movies = []

mov1 = str(input("Enter 1st movie: "))
mov2 = str(input("Enter 2nd movie: "))
mov3 = str(input("Enter 3rd movie: "))

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# 2. WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = ["m", "a", "a", "m"]

copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("Panlindrome")
else:
    print("Not Palindrome")

# 3. WAP to count the number of students with the “A” grade in the following tuple.

grade = ("C", "D", "A", "A", "B", "B", "A")

print(grade.count("A"))

# 4. Store the above values in a list & sort them from “A” to “D”.

grade = ["C", "D", "A", "A", "B", "B", "A"]

grade.sort()
print(grade)