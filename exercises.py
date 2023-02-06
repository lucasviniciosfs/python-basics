def list_check(lista):
    if [item for item in lista if type(item) is not list]:
        return False
    return True

print(list_check([[],[1],[2,3], (1,2)])) # False
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True