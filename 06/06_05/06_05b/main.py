from collections import deque

def matching_paren(my_str):
  stack = deque()
  for letter in my_str:
    if letter == '(':
      stack.append(letter)
    if letter == ')':
      if not stack:
        return False
      stack.pop()
  return len(stack) == 0
  
print(matching_paren('((linkedin))learning'))