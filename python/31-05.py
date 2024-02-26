#punkt 1
sum = 1 
for i in range(1,11):
    sum += i
    print("produkt", sum)
#punkt 2
quad = 0
for a in range(1, 11):
    quad = a*a
    print("quadrad",quad)    
#punkt 3
list = ["mancaversa" ,"banana", "macchina"]
for wort in list:
    wortlange = len(wort)
    print(wortlange)
#punkt 4
for c in range(10, 0, -1):
    print(c)
#punkt 5 
eingabe = int(input("gip eine ganze zahl ein: "))
sum = 0
for d in range(1 , eingabe +1):
     sum = d + sum
     print(sum)
