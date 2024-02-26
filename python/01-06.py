#Aufgabe 1
#punk 1 
#variable eingabe
print()
print("Aufgabe1 punk 1:")
hoehe = 4
breite = 5
#range eingabe
for x in range(hoehe):
    #print 
    print("*" * breite )
#punkt 2
print()
print("punkt 2:")
h = 6
for a in range(1, h + 1):
    print("*" * a) 
#punkt 3
print()
print("punkt 3:")
for c in range(1, 10):
    print(str(c) * c)


#Aufgabe2
print()
print("Aufgabe 2")
for b in range(1, h +1):
    print("*" * b)
for b in range(h - 1, 0, -1):
    print("*" * b)
print()    
#Aufgabe 3

f= 6
for d in range(1, f, +1):
    for t in range(1 ,d +1):
        print(t, end="")
    print()
#hier habe ich ein Problem, das ich nicht lösen konnte, 
# weil das Ergebnis nicht den Anforderungen entspricht
for d in range(f -1, 0, -1):
    for t in range(1 ,d +1):
        print(f -1, end="")
    print()

        