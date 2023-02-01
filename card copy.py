from csv import writer, reader, DictWriter

with open('teste.csv', 'w') as file:
    headers = ('Name', 'LastName', 'Age')
    csv_file = DictWriter(file, fieldnames=headers)
    csv_file.writeheader()
    csv_file.writerow({
        'Name': 'Lucas',
        'LastName': 'Vinicios',
        'Age': 27
    })
    
