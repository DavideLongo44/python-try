
#punk 3 
#tastatuer eingabe des name ein
name = input("gip deinen namen ein")
#if(wenn) das name ist Max Mustermann" wird gezeikt mit print "du hast zugriff"
if name == "Max Mustermann":
    print("du hast Zugriff")
#elif wenn was haben wir als input gegeben ist nicht korret
elif name:
    print("Du hast leider keine zugriff.")
#else für wieder eingabe die namen ein 
else:
    print("Bitte wiederhole den Vorgang und gebe einen Namen ein.")
#punkt 5    
alter = input("gipt deine alter ein:")
if alter >= 18:
    print("bist du volljaerig") 
elif     alter >= 12 and alter <= 17:
    print("teenager ")
else: 
    print("bist du ein kind!")
