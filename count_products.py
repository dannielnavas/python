from collections import defaultdict

def count_products(products):
    # crea diccionario con valor por defecto 0
    product_count = defaultdict(int)
    for product in products:
        product_count[product] += 1
    return product_count

products = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
product_count = count_products(products)
print(product_count)
