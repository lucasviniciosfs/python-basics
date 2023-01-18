def is_all_strings(list):
    return all(type(item) == str for item in list)

print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2,'a', 'b', 'c']))