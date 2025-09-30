import csv

# Leer un archivo CSV y convertirlo en una lista de diccionarios
with open('products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)  # Cada fila es un diccionario con claves basadas en los encabezados del CSV


# Mostrar la informacion en columnas
with open('products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Product: {row['name']}, Price: {row['price']}, Quantity: {row['quantity']}")

# Agregar una nueva fila a un archivo CSV existente
new_product = {'name': 'Tablet', 'price': '299.99', 'quantity': '15', 'brand': 'TechBrand', 'category': 'Electronics', 'entry_date': '2024-06-15', 'total_value': '4499.85'}
with open('products_updated.csv', mode='a', newline='') as file:
    file.write('\n')  # Asegurarse de que la nueva fila comience en una nueva línea
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)


# nueva columna
file_path = 'products_updated.csv'
updated_file_path = 'products_final.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['total_value_final']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() # Escribir los encabezados en el nuevo archivo

        for row in csv_reader:
            row['total_value_final'] = (float(row['price']) * 1.9) * int(row['quantity'])
            csv_writer.writerow(row)  # Escribir la fila actualizada en el nuevo archivo
