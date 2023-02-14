alphabet = {chr(i+96):i for i in range(1,27)}

def is_odd_string(text):
    sum = 0
    for char in text:
        sum += dict(alphabet).get(char)
    return False if sum % 2 == 0 else True


print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False