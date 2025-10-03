import asyncio

async def process_data(data):
    print(f"Processed data: {data}")
    await asyncio.sleep(10)  # Simula una operación asíncrona
    print(f"Finished processing data: {data}")
    return data * 2

async def main():
    print("Starting data processing...")
    result = await process_data(5)
    print(f"Result: {result}")
    print("Data processing completed.")

asyncio.run(main())
