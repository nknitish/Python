# range(start, stop, step)
# Note: stop is NOT included

for i in range(1, 6):
    print(f"i is: {i}")
else:
    print("Loop completed\n")


# for-else executes the else block only if the loop
# finishes normally (without a break)

numbers = [1, 3, 4, 5, 6, 7]

for num in numbers:
    print(num)
else:
    print("List iteration completed\n")


# Tuple iteration with break
# Since break is encountered when i == 3,
# the else block will NOT execute.

t = (7, 6, 5, 4, 3, 2, 1)

for i in t:
    if i == 3:
        print("Found 3. Stopping loop.\n")
        break

    print(i)
else:
    print("Tuple iteration completed\n")


# continue skips the current iteration
# Here we skip spaces while printing characters.

name = "Nitish Mishra"

for ch in name:
    if ch == " ":
        continue

    print(ch)
else:
    print("String iteration completed\n")


# pass is a placeholder statement.
# It does nothing and is useful when writing code skeletons.

for i in range(20):
    pass