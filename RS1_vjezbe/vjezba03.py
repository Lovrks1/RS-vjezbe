# Vježba 03

import random
tajni_broj = random.randint(1, 10)

broj_je_pogoden = False
broj_pokusaja=0

print("pogodi broj između 1 i 100")

while not broj_je_pogoden:
    pokusaj=int(input("Unesi broj:"))
    broj_pokusaja+=1

    if pokusaj < tajni_broj:
     print("tvoj broj je manji od trazenog broja")

    elif pokusaj > tajni_broj:
       print("tvoj broj je veći od trazenog broja")

    else:
       broj_je_pogoden=True
       print(f"Bravo, pogodio si u {broj_pokusaja} pokusaja")

