from csv import DictWriter

with open("arq.csv", "w") as file:
    headers = ("Name", "Lastname", "Age")
    writer = DictWriter(file, fieldnames=headers)
    DictWriter.writeheader(writer)
    writer.writerow({
        "Name": "Lucas",
        "Lastname": "Vinicios",
        "Age": "27"
    })