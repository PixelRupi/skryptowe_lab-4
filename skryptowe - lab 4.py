import math

class Punkt():
    def __init__(self, x=0, y=0, r=1):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.r = r if r is not None else 1

    def odleglosc_poczatek(self): #od poczatku ukladu 
        return(math.pow(self.x**2 + self.y**2, 0.5))
    
    def dystans(self, drugi_punkt): #miedzy dwoma punktami 
        return(math.sqrt((self.x - drugi_punkt.x)**2 + (self.y - drugi_punkt.y)**2))

    def __str__(self):
        return f"x: {self.x} ; y: {self.y}"

    def __repr__(self):
        return f"x: {self.x} ; y: {self.y}"


class Kolo(Punkt):
    def __str__(self):
        return f"x: {self.x} ; y: {self.y} ; r: {self.r}"
    
    def obwod(self):
        return(2*math.pi*self.r)
    
    def pole(self):
        return(math.pi * (self.r**2))
    
    def przesun(self, wektor_x, wektor_y):
        self.x += wektor_x
        self.y += wektor_y
    
    def cz_wsp(self, drugi_okrag):
        dystans_srodkow = math.sqrt((self.x - drugi_okrag.x)**2 + (self.y - drugi_okrag.y))
        #print(dystans_srodkow)

        if(self.r + drugi_okrag.r >= dystans_srodkow):
            return True
        else:
            return False
    

        

#tworzenie obiektow:
pkt1 = Punkt(3, 4)
pkt2 = Punkt(6, 8)

okrag1 = Kolo(1, 1, 2)
okrag2 = Kolo(-3, -3, 3)


#testowanie czesci wspolnej okregow:
#print(okrag1.cz_wsp(okrag2))


#testowanie przesuwania
#print("przed: ")
#print(okrag1)
#okrag1.przesun(-3,4)
#print("po: ")
#print(okrag1)


#testowanie obwodu:
#print(okrag1.obwod())
#print(okrag2.obwod())


#testowanie pola:
#print(okrag1.pole())
#print(okrag2.pole())


#testowanie odleglosci:
#print(pkt1.odleglosc_poczatek())
#print(pkt2.odleglosc_poczatek())


#testowanie dystansu:
#print(pkt1.dystans(pkt2))
#print(pkt2.dystans(pkt1))


#wyswietlanie punktu:
#print(pkt1)
#print(pkt2)


