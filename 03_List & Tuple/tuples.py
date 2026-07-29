# List -> Mutable
# Tuples -> Immutable, just like strings

tup = (2, 4, 5, 4, 1, 3, 4)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])

tup1 = () # empty tuple
print(tup1)
print(type(tup1))

tup2 = (14,)
print(tup2)
print(type(tup2))

# Tuples Methods

# Slicing -> tuple[starting_idx : ending_idx] - ending idx is not included

print(tup[0:4])
print(tup[3:len(tup)])
print(tup[:4]) # [0:6]
print(tup[4:]) # [6:len(tup)]
print(tup[-3:-1]) # reverse indexing

print(tup.index(4)) #returns index of first occurrence

print(tup.count(4))