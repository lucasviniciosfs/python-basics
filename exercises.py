def find_factors(num):
    return [ n for n in range(1,num+1) if num % n == 0]

print(find_factors(10)) # [1,2,5,10 ]
print(find_factors(11)) # [1,11]
print(find_factors(111)) # [1,3,37,111 ]
print(find_factors(321421)) # [1,293,1097,321421 ]