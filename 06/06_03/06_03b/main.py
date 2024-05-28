from collections import deque

history_stack = deque()

history_stack.append("https://www.google.com")
history_stack.append("https://www.facebook.com")
history_stack.append("https://www.stackoverflow.com")

print(history_stack[-1])
print(history_stack.pop())