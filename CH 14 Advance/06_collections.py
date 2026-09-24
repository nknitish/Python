from collections import Counter, defaultdict, deque

# Counter: counts repeated elements
items = ["apple", "banana", "apple", "grape", "banana", "apple"]
count = Counter(items)
print("Counter:", count)
print("Most common:", count.most_common(2))

# defaultdict: default value for missing keys
student_grades = defaultdict(list)
student_grades["Alice"].append(90)
student_grades["Alice"].append(85)
student_grades["Bob"]  # creates empty list automatically
print("Defaultdict:", dict(student_grades))

# deque: efficient append/pop from both ends
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
print("Deque:", list(queue))
print("Popped from right:", queue.pop())
print("Popped from left:", queue.popleft())
