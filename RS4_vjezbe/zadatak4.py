import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

async def autentifikacija(username, password):
    await asyncio.sleep(2)
    if username in korisnici and korisnici[username] == password:
        return True
    raise ValueError("Neispravni podaci")

async def autentifikacija_timeout(username, password):
    await asyncio.sleep(3)
    raise TimeoutError("Autentifikacijski servis ne odgovara")

async def main():
    zahtjevi = [
        autentifikacija("korisnik1", "lozinka1"),
        autentifikacija("korisnik2", "krivo"),
        autentifikacija("korisnik3", "lozinka3"),
        autentifikacija_timeout("korisnikX", "123"),
        asyncio.wait_for(autentifikacija("korisnik1", "lozinka1"), timeout=1),
    ]

    try:
        rezultati = await asyncio.gather(*zahtjevi)
        print("Rezultati:", rezultati)
    except Exception as e:
        print("Dogodila se greška:", e)

if __name__ == "__main__":
    asyncio.run(main())
