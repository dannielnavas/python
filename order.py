class Order:

    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)

# No es necesario instanciar la clase para usar el método estático
Order.calculate_tax(100, 15)  # 15.0
print(Order.calculate_tax(100, 15))
