class Buch:
    # __init__ heißt Kontruktor
    def __init__(self, title, autor, preis, menge):
        self.title = title
        self.autor = autor
        self.preis = preis
        self.__menge = menge

    def verkaufen(self, verkaufteMenge) -> float:
        self.__menge -= verkaufteMenge

        return verkaufteMenge * self.preis

    def kaufen(self):
        self.__menge += 1

    def gesamterPreis(self) -> float:
        return self.preis * self.__menge
    
    def menge(self):
class Buch:
    # __init__ heißt Kontruktor
    def __init__(self, title, autor, preis, menge):
        self.title = title
        self.autor = autor
        self.preis = preis
        self.__menge = menge

    def verkaufen(self, verkaufteMenge) -> float:
        self.__menge -= verkaufteMenge

        return verkaufteMenge * self.preis

    def kaufen(self):
        self.__menge += 1

    def gesamterPreis(self) -> float:
        return self.preis * self.__menge
    
    def menge(self):
buch1 = Buch("Harry Potter", "JK Rowling", 10.0, 250)
#buch2 = Buch("Harry Potter 2", "JK Rowling", 15.99, 100)
# buch3 = Buch("Harry Potter 3")

# wir verkaufen das Buch 5 Mal
betrag = buch1.verkaufen(5)
print("Der Preis von verkauften Büchern ", betrag)
print("Gesamter Preis nach dem Verkauf ", buch1.gesamterPreis())
menge = buch1.menge()
print("Menge", menge)

menge = 0

print("Menge", buch1.menge())
# betrag = buch1.verkaufen(7)

# print("Neue Menge", buch1.__menge)


# # wir bestellen eine
