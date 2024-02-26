# durch eine liste woertern gehen und die laenge jedes wortes ausgeben

# 1. wir legen unser Array mit worten fest
woerter = ["baum", "Autos", "Ruediger", "Ahmet", "Techstarter"]

# 2. zeahlrvariable anlegen
i = 0


while i < len(woerter):
#inhalt aus Array "woerter" an der stelle 0 wird der variablen "wort" zugewissen!
    wort = woerter[i]
    
    #Laenge des wortes aus der variable "wort" wird einer neuen variable zugewissen!
    laenge = len(wort)
    #Aufgabe im terminal der lange
    print("das Wort: ", wort, "hat eine Laenge von: ", laenge)
#Zaehlervariable / Indexzaehler wird um +1 hochgezaehlt!
    i += 1