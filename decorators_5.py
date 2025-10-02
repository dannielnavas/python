class Counter:
    count = 0

    @classmethod # Incrementa el contador cada vez que se llama al método por medio de el decorador
    def increment(cls):
        cls.count += 1
        return cls.count

print(Counter.increment())
print(Counter.increment())
print(Counter.increment())
