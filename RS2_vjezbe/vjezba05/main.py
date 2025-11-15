from shop.proizvodi import dodaj_proizvod, skladiste
from shop.narudzbe import napravi_narudzbu

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]


for p in proizvodi_za_dodavanje:
    dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

print("\nStanje skladišta:")
for proizvod in skladiste:
    proizvod.ispis()


narudzba1 = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Miš", "cijena": 100, "narucena_kolicina": 1}
]

nar = napravi_narudzbu(narudzba1, skladiste)

if nar:
    nar.ispis_narudzbe()
