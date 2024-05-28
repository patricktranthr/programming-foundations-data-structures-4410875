from collections import deque

printer_queue = deque()
printer_queue.append("Resume.pdf")
printer_queue.append("Homework1.docx")
printer_queue.append("Profile_Pic.png")

while len(printer_queue) > 0:
  document = printer_queue.popleft()
  print(f'Printing {document}')