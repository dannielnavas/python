from collections import Counter

def count_sales(products: list[str]) -> Counter:
    # utiliza Counter para contar productos
    return Counter(products)

products = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
product_count = count_sales(products)
print(product_count)
