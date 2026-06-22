# List in Python
# A list is a collection of items that are ordered and changeable.
# Lists are written with square brackets [].
# Creating a list

my_list = ["apple", "banana", "cherry",1, 2, 3, True, False, None, 3.14]
print(my_list)  # Output: ['apple', 'banana', 'cherry',
print(my_list[0])  # Output: apple
print(my_list[1])  # Output: banana
print(my_list[-1])  # Output: 3.14


# Changing the value of a list item
my_list[1] = "orange"  # Changing the value of the second item
print(my_list)  # Output: ['apple', 'orange', 'cherry',

# methods of list 
print(my_list[1:4])  # Output: ['orange', 'cherry', 1]

# List methods are built-in functions that can be used to manipulate lists. Some common list methods include append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), and copy().

# append() method adds an item to the end of the list.
my_list.append("grape")  # Adding an item to the end of the list
print(my_list)  # Output: ['apple', 'orange', 'cherry', 1, 2, 3, True, False, None, 3.14, 'grape']


# extend() method adds multiple items to the end of the list.
my_list.extend(["kiwi", "mango"])  # Adding multiple items to the end
print(my_list)  # Output: ['apple', 'orange', 'cherry', 1, 2, 3, True, False, None, 3.14, 'grape', 'kiwi', 'mango']


# Inserting an item at a specific index
my_list.insert(1, "pear") 
print(my_list)  # Output: ['apple', 'pear', 'orange', 'cherry', 1, 2, 3, True, False, None, 3.14, 'grape', 'kiwi', 'mango'] 

# Removing an item from the list
my_list.remove("cherry")  # Removing an item from the list
print(my_list)  # Output: ['apple', 'pear', 'orange', 1, 2, 3, True, False, None, 3.14, 'grape', 'kiwi', 'mango']

# Popping an item from the list
popped_item = my_list.pop()  # Popping the last item from the list
print(popped_item)  # Output: mango
print(my_list)  # Output: ['apple', 'pear', 'orange', 1, 2, 3, True, False, None, 3.14, 'grape', 'kiwi']    

# Clearing the list
my_list.clear()  # Clearing the list
print(my_list)  # Output: []


numbers = [1, 2, 3, 3,2,1,4,5]

#sort() method sorts the list in ascending order.
numbers.sort()  # Sorting the list in ascending order
print(numbers)  # Output: [1, 1, 2, 2, 3, 3, 4, 5]

#reverse() method reverses the order of the list.
numbers.reverse()  # Reversing the order of the list
print(numbers)  # Output: [5, 4, 3, 3, 2, 2, 1, 1]