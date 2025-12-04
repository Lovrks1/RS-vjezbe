import asyncio
import aiohttp



async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    async with session.get(url) as response:
        data = await response.json()

        return data["data"][0]["attributes"]["body"]




async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        return data["fact"]


async def mix_facts(dog_facts, cat_facts):
    mixed = []

    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed.append(dog_fact)
        else:
            mixed.append(cat_fact)

    return mixed



async def main():
    async with aiohttp.ClientSession() as session:

       
        dog_facts_tasks = [asyncio.create_task(get_dog_fact(session)) for _ in range(5)]
        cat_facts_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)]

    
        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

   
    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

 
    mixed = await mix_facts(dog_facts, cat_facts)

    print("Konačne odabrane činjenice:\n")
    for fact in mixed:
        print(fact)
        print()


asyncio.run(main())
