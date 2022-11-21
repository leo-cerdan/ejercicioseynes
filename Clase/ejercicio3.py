import math

class Cirulo:
    
    def __init__(self,radio, n=1):

        if radio <= 0 or n <= 0:
            print("El radio o su multiplo deben ser mayor que cero.")
        else:
            self.radio = radio * n
            
    def area(self):
        return "El área del círuculo es " + str(round(math.pi*self.radio**2,2))

    def perimetro(self):
        return "El perímetro del círculo es " + str(round(2*math.pi*self.radio,2))

    def __str__(self):
        return "El círculo tiene un radio de " + str(self.radio) 

if __name__ == "__main__":

    circulo1 = Cirulo(0)
    circulo2 = Cirulo(4,0)
    circulo3 = Cirulo(5,2)

    circulo1 = Cirulo(2,2)
    print(circulo1)
    print(circulo1.area())
    print(circulo1.perimetro())

