def two_oldest_ages(lista):
    oldest = max(lista)
    lista.remove(oldest)
    second_oldest = max(lista)
    return [second_oldest, oldest]

print(two_oldest_ages([1, 2, 10, 8]))