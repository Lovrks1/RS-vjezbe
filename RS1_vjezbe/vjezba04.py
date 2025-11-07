# Vježba 04

zbroj=0
print ("unesi cijele brojeve za prekid unesi 0: ")
while True:
    broj= int(input("unesi cijeli broj: "))
    if broj ==0:
        break
    zbroj= zbroj+broj

print(f"Zbroj svih brojeva prije unosa 0 je {zbroj}")