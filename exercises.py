def find_greater_numbers(lista):
    count = 0
    for i in range(0, len(lista)):
        for item in lista[i:]:
            #print(lista[i], item)
            if lista[i] < item:
                count +=1
    return count

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0