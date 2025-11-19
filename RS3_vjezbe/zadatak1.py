import asyncio

async def dohvati_podatke():
    await asyncio.sleep(3)  
    
    podaci = [i for i in range(1, 11)]  
    
    print("Podaci dohvaćeni.")
    return podaci

if __name__ == "__main__":
    rezultat = asyncio.run(dohvati_podatke())
    print("Vraćeni podaci:", rezultat)
