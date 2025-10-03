import threading
import time


def process_request(request_id):
    print(f"Processing request {request_id}")
    time.sleep(3)  # Simula una operación que toma tiempo
    print(f"Request {request_id} processed")

threads = []
for i in range(3):
    # crear un hilo para cada solicitud
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    # asegurarse de que cada hilo haya terminado
    thread.join()
print("All requests processed")
