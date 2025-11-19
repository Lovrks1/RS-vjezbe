import asyncio

async def secure_data(podaci):
    """
    Simulira enkripciju osjetljivih podataka (3 sekunde).
    """
    await asyncio.sleep(3)  

    return {
        "prezime": podaci["prezime"],
        "broj_kartice": hash(str(podaci["broj_kartice"])),
        "CVV": hash(str(podaci["CVV"]))
    }

async def main():
  
    osjetljivi_podaci = [
        {"prezime": "Horvat", "broj_kartice": "1234567890123456", "CVV": "123"},
        {"prezime": "Kovač",  "broj_kartice": "9876543210987654", "CVV": "999"},
        {"prezime": "Marić",  "broj_kartice": "5555222233331111", "CVV": "321"},
    ]

    
    zadaci = [
        asyncio.create_task(secure_data(p))
        for p in osjetljivi_podaci
    ]

    
    rezultati = await asyncio.gather(*zadaci)

   
    for r in rezultati:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
