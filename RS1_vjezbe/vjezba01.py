# Vježba 01

broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))

operator = input("Unesite operator (+, -, *, /): ")

if operator == '+':
    rezultat = broj1 + broj2
    print(f"{broj1} + {broj2} = {rezultat}")
elif operator == '-':
    rezultat = broj1 - broj2
    print(f"{broj1} - {broj2} = {rezultat}")
elif operator == '*':
    rezultat = broj1 * broj2
    print(f"{broj1} * {broj2} = {rezultat}")
elif operator == '/':
    if broj2 == 0:
        print("Greška: Dijeljenje s nulom nije dopušteno!")
    else:
        rezultat = broj1 / broj2
        print(f"{broj1} / {broj2} = {rezultat}")
else:
    print("Greška: Nepodržani operator! Molimo koristite +, -, * ili /.")
