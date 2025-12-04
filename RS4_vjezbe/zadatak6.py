import asyncio
import random

async def fetch_weather_data(station_id: int) -> float:
    await asyncio.sleep(random.uniform(1, 5))
    return random.uniform(20, 25)

async def main():
    tasks = [
        asyncio.wait_for(fetch_weather_data(i), timeout=2)
        for i in range(10)
    ]

    results = []
    for task in asyncio.as_completed(tasks):
        try:
            value = await task
            results.append(value)
        except asyncio.TimeoutError:
            results.append(None)

    print("Rezultati mjernih stanica:", results)

    valid = [t for t in results if t is not None]

    if valid:
        avg_temp = sum(valid) / len(valid)
        print(f"Prosječna temperatura: {avg_temp:.2f} °C")
    else:
        print("Nema dostupnih podataka za izračun prosjeka.")

if __name__ == "__main__":
    asyncio.run(main())
