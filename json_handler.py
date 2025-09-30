import json

with open('data.json', mode='r') as file:
    products = json.load(file)

products.append({
    'name': 'Smart TV',
    'price': 2000,
    'quantity': 20
})

with open('data.json', mode='w') as file:
    json.dump(products, file, indent=4)

for product in products:
    # print(product)
    print(f"Name: {product['name']} Price: {product['price']} Stock: {product['quantity']}")
