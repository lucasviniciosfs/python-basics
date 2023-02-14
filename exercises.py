def sum_up_diagonals(listas):
  posInicial = 0
  posFinal = len(listas) - 1
  sum_diag = 0
  for lista in listas:
    sum_diag += lista[posInicial] + lista[posFinal]
    posInicial += 1
    posFinal -= 1
  return sum_diag

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1))

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
print(sum_up_diagonals(list2))  # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

print(sum_up_diagonals(list3))  # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
print(sum_up_diagonals(list4))  # 68