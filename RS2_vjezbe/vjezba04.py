#vjezba 4
import datetime
import math
class Automobil:
    def __init__(self, marka, model,godina_proizvodnej, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje=godina_proizvodnej
        self.kilometraza=kilometraza

    def ispis(self):
            print(f"Marka: {self.marka}, Model: {self.model}, Godina: {self.godina_proizvodnje}, Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        print(f"Automobil je star {trenutna_godina - self.godina_proizvodnje} godina.")
    
auto = Automobil("Audi", "A4", 2017, 85000)
auto.ispis()
auto.starost()

class Kalkulator:
     def __init__(self,a,b):
          self.a=a
          self.b=b

     def zbroj(self):
          return self.a + self.b
     
     def oduzimanej(self):
          return self.a - self.b
     
     def mnozenje(self):
        return self.a * self.b

     def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno."
        
     def potenciranje(self):
        return self.a ** self.b

     def korijen(self):
        return math.sqrt(self.a)
    
calc = Kalkulator(9, 3)

print(calc.zbroj())       
print(calc.dijeljenje())  
print(calc.korijen()) 
print(calc.oduzimanej())       
print(calc.potenciranje())  


class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
    

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
studenti_objekti = [Student(**s) for s in studenti]

najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())
print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime} s prosjekom {najbolji_student.prosjek():.2f}")


class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * self.r ** 2
    
krug = Krug(5)
print(krug.opseg())     
print(krug.povrsina())  


class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")



class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"{radnik.ime} je dobio povišicu, nova plaća je {radnik.placa}€.")

radnik1 = Radnik("Toni", "Programer", 1500)
manager1 = Manager("Ante", "Voditelj", 2500, "IT")
radnik1.work()           
manager1.work()           
manager1.give_raise(radnik1, 200)  
