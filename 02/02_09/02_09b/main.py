def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second = float('inf')
    for i in my_list:
        if i < smallest:
            second = smallest
            smallest = i
        elif i < second:
            second = i
    return second

print(find_second_smallest([5, 8, 3, 2, 6]))
