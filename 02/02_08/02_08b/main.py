my_list = [1, 7, 3]
#print(sorted(my_list, reverse=True))

student_grades = [("Adam", 93), ("Bob", 78), ("Charles", 84)]
print(sorted(student_grades, key=lambda x: x[1], reverse = True))