card_stack = []

card_stack.append("J of H")
card_stack.append("3 of C")
card_stack.append("A of S")

top_card = card_stack.pop()
print(top_card)
top_card = card_stack[-1]
print(top_card)

if not card_stack:
  print("Card stack is empty")
else:
  print(len(card_stack))