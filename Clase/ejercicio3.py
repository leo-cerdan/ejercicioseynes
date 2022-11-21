class Cirulo:
    
    def __init__(self,radio, n=1):
        if radio <= 0 or n <= 0:
            print("El radio o su multiplo deben ser mayor que cero.")
        else:
            self.radio = radio * n