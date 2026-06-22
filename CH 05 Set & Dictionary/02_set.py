# Set in Pyton

# Creating a set
my_set = set()  # This creates an empty set

my_set = {"apple", "banana", "cherry", 1, 1, 2, 2, 3, True, False, None, 3.14}
print(my_set)  # Output: {False, 1, 2, 3, None, 'banana', 'cherry', 3.14, 'apple', True}
print(type(my_set))  # Output: <class 'set'>


# Methods of set
# add() method adds an element to the set.
my_set.add("grape")  # Adding an element to the set
print(my_set)  # Output: {False, 1, 2, 3, None, 'banana', 'cherry', 3.14, 'apple', True, 'grape'}

# remove() method removes an element from the set. If the element is not present, it raises a KeyError.
my_set.remove("banana")  # Removing an element from the set #keyerror if the element is not present

print(my_set)  # Output: {False, 1, 2, 3, None, 'cherry', 3.14, 'apple', True, 'grape'}

# discard() method removes an element from the set if it is present. If the element is not present, it does nothing.
my_set.discard("cherry")  # Removing an element from the set  #No error if missing.
print(my_set)  # Output: {False, 1, 2, 3, None, 3.14, 'apple', True, 'grape'}

# pop() method removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.
# "arbitrary element" = an element chosen automatically by Python, without any guaranteed order.
popped_element = my_set.pop()  # Removing and returning an arbitrary element from the set
print(popped_element)  # Output: (An arbitrary element from the set)
print(my_set)  # Output: (The set after popping an element)

# clear() method removes all elements from the set.
my_set.clear()  # Clearing the set
print(my_set)  # Output: set()  

# union() method returns a new set that contains all the elements from both sets, without duplicates.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Union of two sets
print(union_set)  # Output: {1, 2, 3, 4, 5}

# intersection() method returns a new set that contains only the elements that are present in both sets.
intersection_set = set1.intersection(set2)  # Intersection of two sets
print(intersection_set)  # Output: {3}  

# difference() method returns a new set that contains the elements that are present in the first set but not in the second set.
difference_set = set1.difference(set2)  # Difference of two sets
print(difference_set)  # Output: {1, 2} 

# symmetric_difference() method returns a new set that contains the elements that are present in either of the sets but not in both.
symmetric_difference_set = set1.symmetric_difference(set2)  # Symmetric difference of two sets
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}




# Properties of Set
# 1. Sets are unordered collections of unique items.
# 2. Sets are mutable, meaning that you can change, add, or remove items after the set has been created.
# 3. Sets are defined using curly braces {} or the set() constructor.
# 4. Sets do not allow duplicate elements. If you try to add a duplicate element, it will be ignored.
# 5. Sets can be used to perform mathematical operations like union, intersection, difference, and symmetric difference.



