class perro(object): 
    def __init__(self, nombre, color, raza, edad):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.edad = edad

    def hablar(self):
        print ("Guau!")

    def __str__(self):
        return  f"perro nombre {self.nombre}"

p= perro ("jaime", "azul", "calle", 2)
print (p)