suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
lues = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

res = []
for key in lues:
    for value in suits:
        res.append({ key: value})


print(res)


