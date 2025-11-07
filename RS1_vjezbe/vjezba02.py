# Vježba 02

godina=int(input("Unesi godinu"))

if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(f"godina {godina}. je prijestupna.")
else:
    print(f"godina {godina}. niej prijestupna.")
    
