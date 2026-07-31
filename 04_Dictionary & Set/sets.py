# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
# Duplicate items are not allow in sets
# Set is mutable

collecion = {1, 2, 2, 2, "hello", "world", "world"}

print(collecion)
print(type(collecion))
print(len(collecion)) # total number of items

# Set Methods

empty_set = set() # empty set; syntax

empty_set.add(1)
empty_set.add(2)
empty_set.add(2)
empty_set.add(3)
empty_set.add("Om")
empty_set.add((7, 8, 9))
# empty_set.add([1, 2, 3]) # unhashable type: 'list'

empty_set.remove(1)

empty_set.clear() # clear all set

print(empty_set)
print(len(empty_set))

store = {"hello", "world", "coding", "python"}

print(store)
print(store.pop()) # remove random value
print(store.pop())

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) # combines both sets
print(set1.intersection(set2)) # get similer value