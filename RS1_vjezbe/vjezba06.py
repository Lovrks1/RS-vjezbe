# Vježba 06

#Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).
#for verzija
suma =0
for i in range(1,101):
    if i % 2 == 0:
        suma += i
print(f"zbroj parnih brojeva od 1 do 100 je {suma}")

#while verzija
suma=0
i=1
while i <= 100:
    if i % 2 == 0:
        suma+= i
    i += 1
print(f"zbroj parnih brojeva od 1 do 100 je {suma}")

#Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu
#for verzija
neparni=[]
for i in range (1,20,2):
    neparni.append(i)
neparni.reverse()
print(f"prvih 10 neparnih brojeva obrnutim redosljedom ide {neparni}")

#while verzija
neparni=[]
i=1
while len(neparni)<10:
    if i % 2 !=0:
        neparni.append(i)
    i+=1
neparni.reverse()
print(f"prvih 10 neparnih brojeva obrnutim redosljedom ide {neparni}")

#Napišite program koji ispisuje Fibonaccijev niz do 1000. Fibonaccijev niz počinje s brojevima 0 i 1, a 
#svaki sljedeći broj je zbroj prethodna dva broja.
#for verzija

a,b =0, 1
fibonacci = [a,b]
for i in range(2,100):
     c=a+b
     if c >1000 :
         break
     
     fibonacci.append(c)
     a,b=b,c
print(f"fibonaccijev niz do 1000 {fibonacci}")

#while verzija
a, b = 0, 1
fibonacci = [a, b]
while True:
    c = a + b
    if c > 1000:
        break
    fibonacci.append(c)
    a, b = b, c
print(f"Fibonaccijev niz do 1000 {fibonacci}")

