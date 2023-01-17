first_list = []
second_list = []

def isEven(num):
    return num % 2 == 0

def partition(list, fn):
    for item in list:
        if fn(item):
            global first_list
            first_list.append(item)
        else:
            global second_list
            second_list.append(item)
    return [first_list, second_list]
            
print(partition([1,2,3,4], isEven))