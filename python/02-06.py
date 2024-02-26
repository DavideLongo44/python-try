#funzioni

print ("guten morgen")

zahl = -5
print(zahl)
positivezahl = abs(zahl)
print(positivezahl)
text = "guten morgen"
leangeVomtext  = len(text)
print(leangeVomtext)
zahler =[-3, 5, -5, 10, 1]

maxwert =max(zahler)

for x in range(6):
    print(x)
for x in range(7):
    y= x*x 
    #nelle parentesi graffe con l aggiunta di f all inizio vengono tirate fuori le variabili
 
    print(f"ergebnis = {x}:{y}")   
    #def si usa per definire
    def schleifen():
        for x in range(7):
         y= x*x 
         print(f"ergebnis = {x}:{y}")
    schleifen()  
    schleifen()
def  istgerade(zal) -> bool:
   if zal % 2 ==0:
       return true
    print("gerade")
   else:
    print("nicht gerade") 
istgerade(4)        
for x