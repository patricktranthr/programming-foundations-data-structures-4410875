def has_unique_characters(data):
    unique_set = set(data)
    return len(data) == len(unique_set)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
