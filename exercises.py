def make_song(count=99, beverage="soda"):
    while count > 0:
        yield f"{count} bottles of {beverage} on the wall."
        count -= 1

kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))