# Tuples in python
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# Creating a tuple
my_tuple = ("apple", "banana", "cherry", 1, 2, 3, True, False, None, 3.14)
print(my_tuple)  # Output: ('apple', 'banana', 'cherry', 1, 2, 3, True, False, None, 3.14)
print(my_tuple[0])  # Output: apple
print(my_tuple[1])  # Output: banana
print(my_tuple[-1])  # Output: 3.14 


a=(1,)
print(type(a))  # Output: <class 'tuple'>

# Tuples are immutable, meaning that you cannot change, add, or remove items after the tuple has been created. However, you can create a new tuple that contains the items of the original tuple along with any new items you want to add.
my_tuple = my_tuple + ("grape",)  # Adding an item to the tuple
print(my_tuple)  # Output: ('apple', 'banana', 'cherry', 1, 2, 3, True, False, None, 3.14, 'grape')


# methods of tuple
print(my_tuple[1:4])  # Output: ('banana', 'cherry', 1) 
print(my_tuple.count(1))  # Output: 1   
print(my_tuple.index("banana"))  # Output: 1   
print(len(my_tuple))  # Output: 11
print(False in my_tuple)  # Output: True
print("kiwi" not in my_tuple)  # Output: True
print(my_tuple * 2)  # Output: ('apple', 'banana', 'cherry', 1, 2, 3, True, False, None, 3.14, 'grape', 'apple', 'banana', 'cherry', 1, 2, 3, True, False, None, 3.14, 'grape') 




# In Python, tuples are immutable, so they have very few built-in methods compared to lists.

# Tuple Methods
# Method	Description
# count(x)	Returns the number of times x appears in the tuple
# index(x)	Returns the index of the first occurrence of x