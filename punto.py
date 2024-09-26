#OK crea una classe punto (che ha in insegresso 2 valori (x e y) e potrà ipotenticamente avere un terzo)
#OK fare un eq che paragona i 2 punti
#?fare un punto centrale origin (0,0,0) CREARE UN COSTRUTTORE CHE RITORNA IL PUNTO DI ORIGINE
#fare un > < che mi paragona i due punti (da un punto centrale 0,0), guarda se c'è qualcosa tipo eq
#funzione che mi stampa il punto "punto (x,y,z)"
#funzione che mi stampa solo la posizione dei punti (x, y,z)
#add mi somma il punto 1 e il punto 2

import math

X_ORIGINE = 0
Y_ORIGINE = 0

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self,punto:object):
        return (self.x == punto.x and self.y == punto.y)  
    
    def __lt__(self, punto:object):
        #ritorna se la radice quadrata di selfx alla seconda + self y alla seconda è minore di quella di punto
        pit1 = Punto.pitagora(self)
        pit2 = Punto.pitagora(punto)
        return (pit1 < pit2)

    def __gt__(self, punto:object):
        #ritorna se la radice quadrata di selfx alla seconda + self y alla seconda è minore di quella di punto
        #TODO guarda se posso eviare di scriverlo 2 volte
        pit1 = Punto.pitagora(self)
        pit2 = Punto.pitagora(punto)
        #print(f"pit1 = {pit1} e pit2 = {pit2}")
        return (pit1 > pit2)
    
    #TODO si dovrebbe chiamare draw(?) richiedi specifiche progetto
    def __str__(self):
        #questo è quello per printare
        return f"punto ({self.x},{self.y})"

    def __add__ (self, point):
        #credo A(self.val + other) 
        return Punto(self.x + point.x, self.y + point.y)

    def punto_origine():
        return Punto(X_ORIGINE,Y_ORIGINE)
    
    def pitagora (self):
        return  math.sqrt((self.x - X_ORIGINE) **2 + (self.y - Y_ORIGINE) ** 2) # 2 ** 4 = 16
    


if __name__ == "__main__":
    p1 = Punto (5,5)
    p2 = Punto (2,2)   
    p3 = p1 + p2
    p4 = p3
    p0 = Punto.punto_origine()
    print(f"P0: {p0}\nP1: {p1}\nP2: {p2}\nP3: {p3}")
    if (p2<p1):
        print("p2 è più piccolo")
    if (p1 != p2):
        print("p1 e p2 sono diversi")
    if (p3 > p1):
        print("p3 > p1")
    if (p4 == p3):
        print("p4 = p3")
    
