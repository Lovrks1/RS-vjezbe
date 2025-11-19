import asyncio

# odbrojava i svaki krug smanji za 1 sekundu
async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        
        # pauzira se
        await asyncio.sleep(1)

    # nakon što petlja završi i task završava
    print(f'{name}: Vrijeme je isteklo!')

async def main():

    # 3 taska se kreiraju i ubacuju u event loop 
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),  # traje 3 sekunde
        asyncio.create_task(timer('Timer 2', 5)),  # traje 5 sekundi
        asyncio.create_task(timer('Timer 3', 7))   #  traje 7 sekundi
    ]

    # asyncio.gather čeka da taskovi završe
    # izvršava sve 3 korutine
    await asyncio.gather(*timers)

asyncio.run(main())
