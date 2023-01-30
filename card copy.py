days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def week():
    while days_of_week:
        yield days_of_week[0]
        days_of_week.remove(days_of_week[0])

days = week()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))


