# Vježba: Nino Telefonino

def ocisti_broj(broj: str) -> str:
    for znak in [" ", "-", "(", ")", "+"]:
        broj = broj.replace(znak, "")
    if broj.startswith("00385"):
        broj = broj[5:]
    elif broj.startswith("385"):
        broj = broj[3:]
    if not broj.startswith("0"):
        broj = "0" + broj
    return broj


def validiraj_broj_telefona(broj: str) -> dict:
    broj = ocisti_broj(broj)

    rezultat = {
        "pozivni_broj": None,
        "broj_ostatak": None,
        "vrsta": None,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    pozivni = {
        "01": ("Grad Zagreb i Zagrebačka županija", "fiksna mreža"),
        "020": ("Dubrovačko-neretvanska županija", "fiksna mreža"),
        "021": ("Splitsko-dalmatinska županija", "fiksna mreža"),
        "022": ("Šibensko-kninska županija", "fiksna mreža"),
        "023": ("Zadarska županija", "fiksna mreža"),
        "031": ("Osječko-baranjska županija", "fiksna mreža"),
        "032": ("Vukovarsko-srijemska županija", "fiksna mreža"),
        "033": ("Virovitičko-podravska županija", "fiksna mreža"),
        "034": ("Požeško-slavonska županija", "fiksna mreža"),
        "035": ("Brodsko-posavska županija", "fiksna mreža"),
        "040": ("Međimurska županija", "fiksna mreža"),
        "042": ("Varaždinska županija", "fiksna mreža"),
        "043": ("Bjelovarsko-bilogorska županija", "fiksna mreža"),
        "044": ("Sisačko-moslavačka županija", "fiksna mreža"),
        "047": ("Karlovačka županija", "fiksna mreža"),
        "048": ("Koprivničko-križevačka županija", "fiksna mreža"),
        "049": ("Krapinsko-zagorska županija", "fiksna mreža"),
        "051": ("Primorsko-goranska županija", "fiksna mreža"),
        "052": ("Istarska županija", "fiksna mreža"),
        "053": ("Ličko-senjska županija", "fiksna mreža"),
        "091": ("A1 Hrvatska", "mobilna mreža"),
        "092": ("Tomato", "mobilna mreža"),
        "095": ("Telemach", "mobilna mreža"),
        "097": ("bonbon", "mobilna mreža"),
        "098": ("Hrvatski Telekom", "mobilna mreža"),
        "099": ("Hrvatski Telekom", "mobilna mreža"),
        "0800": ("Besplatni pozivi", "posebne usluge"),
        "060": ("Komercijalni pozivi", "posebne usluge"),
        "061": ("Glasovanje telefonom", "posebne usluge"),
        "064": ("Usluge s neprimjerenim sadržajem", "posebne usluge"),
        "065": ("Nagradne igre", "posebne usluge"),
        "069": ("Usluge namijenjene djeci", "posebne usluge"),
        "072": ("Jedinstveni pristupni broj za cijelu državu", "posebne usluge")
    }

    for kod in sorted(pozivni.keys(), key=len, reverse=True):
        if broj.startswith(kod):
            rezultat["pozivni_broj"] = kod
            rezultat["broj_ostatak"] = broj[len(kod):]
            mjesto_operater, vrsta = pozivni[kod]
            rezultat["vrsta"] = vrsta
            if vrsta == "fiksna mreža":
                rezultat["mjesto"] = mjesto_operater
            elif vrsta == "mobilna mreža":
                rezultat["operater"] = mjesto_operater
            else:
                rezultat["mjesto"] = mjesto_operater
            break

    if rezultat["pozivni_broj"] is None:
        return rezultat

    ostatak = rezultat["broj_ostatak"]

    if not ostatak.isdigit():
        return rezultat

    duljina = len(ostatak)

    if rezultat["vrsta"] in ["fiksna mreža", "mobilna mreža"]:
        if duljina in [6, 7]:
            rezultat["validan"] = True
    elif rezultat["vrsta"] == "posebne usluge" and duljina == 6:
        rezultat["validan"] = True

    return rezultat


unos = input("Unesite broj telefona: ")
rezultat = validiraj_broj_telefona(unos)

for kljuc, vrijednost in rezultat.items():
    print(f"{kljuc}: {vrijednost}")
