class Libro(object):
    _next_id = 0

    def __init__(self, titulo):
        self.titulo = titulo
        self.autor = None
        self.editorial = None
        self.id = Libro._next_id
        Libro._next_id += 1

    def set_autor(self, autor):
        self.autor = autor
    
    def set_editorial(self, editorial):
        self.editorial = editorial


if __name__ == "__main__":
    from persona import Autor
    
    libro = Libro("asd")
    libro.asignar_editorial("jijodebu)")
    Marquez = Autor("Gabriel Garcia Marquez", 29500458)
    Marquez.Agregar_biografia("Escritor colombiano, conocido por su obra 'Cien años de soledad'.")
    libro.asignar_autor(Marquez)