# vjezba 3

#Parni kvadrati brojeva od 20 do 50

parni_kvadrati = [x**2 for x in range (20,51) if x%2==0]
print(parni_kvadrati)

#Duljine riječi koje sadrže slovo "a"

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
duljina_sa_slovom_a = [len(x) for x in rijeci if "a" in x]
print(duljina_sa_slovom_a)

#Lista rječnika — kubovi za neparne, broj za parne

kubovi= [{x: x**3 if x%2 !=0 else x} for x in range (1,11)]
print(kubovi)

# korijeni brojeva

import math
korijeni= {x: round(math.sqrt(x), 2) for x in range(50, 501, 50)}
print (korijeni)

#Rječnici s prezimenom i zbrojem bodova

studenti = [
  {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
  {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
  {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
  {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
  {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
  {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbroj_bodova = [{x["prezime"]: sum(x["bodovi"])} for x in studenti]
print(zbroj_bodova)

#liste faktorijela

faktorijeli= {x:[math.factorial(i) for i in range(1,x+1)] for x in range(1,11)}
print(faktorijeli)