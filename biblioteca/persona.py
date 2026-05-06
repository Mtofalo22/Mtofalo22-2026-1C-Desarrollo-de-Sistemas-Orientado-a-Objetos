class Persona(object):
    _next_id = 0
    def __init__(self, nombre):
        self.nombre = nombre
        self.dni = None
        self.id = Persona._next_id
        Persona._next_id += 1

class Autor(Persona):
    def Agregar_biografia(self, biografia):
        self.bio = biografia


a = Autor("Gabriel Garcia Marquez", 29500458)
a.Agregar_biografia("Escritor colombiano, conocido por su obra 'Cien años de soledad'.")

