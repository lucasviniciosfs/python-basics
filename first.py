list1 = [1,2,3,4]
list2 = [3,4,5,6]

answer = [num for num in list2 if num in list1]

list3 = ["Elie", "Tim", "Matt"]

answer2 = [name[::-1].lower() for name in list3]

print(answer2)