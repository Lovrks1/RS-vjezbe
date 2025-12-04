import asyncio
import aiohttp
import time

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()
    
async def main():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        
        tasks = [asyncio.create_task(fetch_users(session)) for _ in range(5)]

       
        results = await asyncio.gather(*tasks)

    
    users = results[0]

    imena = [u["name"] for u in users]
    emailovi = [u["email"] for u in users]
    usernameovi = [u["username"] for u in users]

    total = time.perf_counter() - start
    print("Imena:", imena)
    print("Emailovi:", emailovi)
    print("Usernameovi:", usernameovi)
    print(f"Ukupno vrijeme: {total:.2f} s")

asyncio.run(main())