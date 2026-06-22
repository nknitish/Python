
#Dictionary is a collection of keys-value pairs.

mark = {"John": 85,
"Jane": 92,
"Jim": 78,
"Jill": 90,
"Jack": 88}


print(mark)  # Output: {'John': 85, 'Jane': 92, 'Jim': 78, 'Jill': 90, 'Jack': 88}
print(type(mark))  # Output: <class 'dict'>
print(mark["Jane"])  # Output: 92  # Throw KeyError if key is not present
print(mark.get("Jim"))  # Output: 78 #Print none if key is not present

# Properties of Dictionary
# 1. Dictionaries are unordered collections of items.
# 2. Dictionaries are mutable, meaning that you can change, add, or remove items after the dictionary has been created.
# 3. Dictionaries are indexed by keys, which can be of any immutable type (e.g., strings, numbers, tuples).
# 4. Dictionaries are defined using curly braces {} and key-value pairs are separated by colons (:).
# 5. Dictionaries can be nested, meaning that you can have dictionaries within dictionaries.    


# Methods of Dictionary

# keys()	Returns a view object that displays a list of all the keys in the dictionary
print(mark.keys())  # Output: dict_keys(['John', 'Jane', 'Jim', 'Jill', 'Jack'])

# values()	Returns a view object that displays a list of all the values in the dictionary
print(mark.values())  # Output: dict_values([85, 92, 78, 90, 88])

# items()	Returns a view object that displays a list of all the key-value pairs in the dictionary
print(mark.items())  # Output: dict_items([('John', 85), ('Jane', 92), ('Jim', 78), ('Jill', 90), ('Jack', 88)])

# get(key)	Returns the value associated with the specified key 
print(mark.get("Jane"))  # Output: 92
print(mark.get("Alice", "Key not found"))  # Output: Key not found

# update()	Updates the dictionary with the specified key-value pairs
mark.update({"Jane": 90, "Alice": 95})
print(mark)  # Output: {'John': 90, 'Jane': 90, 'Jim': 78, 'Jill': 90, 'Jack': 88, 'Alice': 95}




