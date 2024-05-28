from collections import deque

def gen_binary_nums(n):
  if n <= 0:
    return
  binary_num = deque()
  binary_num.append(1)
  for i in range(n):
    binary = binary_num.popleft()
    print(binary)
    binary_num.append(binary*10)
    binary_num.append(binary*10 + 1)
  

print(gen_binary_nums(10))