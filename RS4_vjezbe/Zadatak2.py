import asyncio
import aiohttp

async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()   
        return data["fact"]
    

async def filter_cat_facts(facts):
    filtered = []

    for fact in facts:
        text = fact.lower()  
        if "cat" in text or "cats" in text:
            filtered.append(fact)

    return filtered

async def main():
    async with aiohttp.ClientSession() as session:

        
        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]

        
        cat_facts = await asyncio.gather(*tasks)

    
    filtered = await filter_cat_facts(cat_facts)

    print("Filtrirane činjenice o mačkama:")
    for fact in filtered:
        print("-", fact)



asyncio.run(main())