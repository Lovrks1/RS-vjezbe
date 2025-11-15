# Vježba 07

def provjera_lozinke(lozinka):
   
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova.")
        return

   
    ima_veliko = any(znak.isupper() for znak in lozinka)
    ima_broj = any(znak.isdigit() for znak in lozinka)
    if not (ima_veliko and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
        return


    lozinka_mala = lozinka.lower()
    if "password" in lozinka_mala or "lozinka" in lozinka_mala:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")
        return


    print("Lozinka je jaka!")


unesena_lozinka = input("Unesite lozinku: ")
provjera_lozinke(unesena_lozinka)