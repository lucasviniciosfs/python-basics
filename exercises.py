def remove_every_other(lista):
    return lista[0:len(lista):2]

print(remove_every_other([1,2,3,4,5]))
print(remove_every_other([5,1,2,4,1]))  # [5,2,1]
print(remove_every_other([1]))  # [1] 