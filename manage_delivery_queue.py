from collections import deque

def manage_delivery_queue() -> deque:
    # crea una cola de entregas
    delivery_queue = deque(['order1', 'order2', 'order3'])
    delivery_queue.append('order4')  # añade una nueva orden al final
    delivery_queue.appendleft('order0')  # añade una nueva orden al inicio
    delivery_queue.popleft()  # procesa la primera orden
    delivery_queue.pop()  # procesa la última orden
    return delivery_queue

queue = manage_delivery_queue()
print(queue)
