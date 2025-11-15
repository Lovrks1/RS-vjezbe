class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        items = ", ".join(
            [f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi]
        )
        print(f"Naručeni proizvodi: {items}, Ukupna cijena: {self.ukupna_cijena} eur")


narudzbe = []


def napravi_narudzbu(lista_proizvoda, skladiste):

   
    if not isinstance(lista_proizvoda, list):
        print("Greška: naruceni_proizvodi mora biti lista!")
        return None


    if len(lista_proizvoda) == 0:
        print("Greška: lista naručenih proizvoda je prazna!")
        return None


    for p in lista_proizvoda:
        if not isinstance(p, dict):
            print("Greška: svaki element mora biti rječnik!")
            return None

       
        if not {"naziv", "cijena", "narucena_kolicina"}.issubset(p.keys()):
            print("Greška: rječnik mora imati ključeve naziv, cijena, narucena_kolicina!")
            return None

    
        proizvod = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if proizvod is None or proizvod.dostupna_kolicina < p["narucena_kolicina"]:
            print(f'Proizvod "{p["naziv"]}" nije dostupan!')
            return None


    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in lista_proizvoda)

    narudzba = Narudzba(lista_proizvoda, ukupna_cijena)
    narudzbe.append({"narudzba": narudzba})

    return narudzba
