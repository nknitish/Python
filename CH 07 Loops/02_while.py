# WHILE LOOP
# Repeats as long as the condition is True.

i = 0

while i < 10:
    print(f"i is {i}")
    i += 1  # Same as i = i + 1


# PRINTING A LIST USING A WHILE LOOP

print("\nPrinting List\n")

items = ["A", 1, 2, 45, False]

i = 0

while i < len(items):
    print(items[i])
    i += 1