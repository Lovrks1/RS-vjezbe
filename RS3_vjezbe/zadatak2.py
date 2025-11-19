import asyncio

async def dohvati_korisnike():
    await asyncio.sleep(3)
    korisnici = [
        {"id": 1, "ime": "Marko"},
        {"id": 2, "ime": "Ana"},
        {"id": 3, "ime": "Iva"}
    ]
    print("Korisnici dohvaćeni.")
    return korisnici

async def dohvati_proizvode():
    await asyncio.sleep(5)
    proizvodi = [
        {"id": 10, "naziv": "Laptop"},
        {"id": 11, "naziv": "Monitor"},
        {"id": 12, "naziv": "Tipkovnica"}
    ]
    print("Proizvodi dohvaćeni.")
    return proizvodi

async def main():
    print("Pokrećem dohvaćanje...")

    korisnici, proizvodi = await asyncio.gather(
        dohvati_korisnike(),
        dohvati_proizvode()
    )

    print("\n--- Rezultati ---")
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)

if __name__ == "__main__":
    asyncio.run(main())
