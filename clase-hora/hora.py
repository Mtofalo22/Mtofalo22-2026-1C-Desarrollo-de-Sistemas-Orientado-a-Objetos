class hora(object): 
    def __init__(self, hh = 0, mm = 0, ss = 0):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    
    def mostar_hora(self):
        print(f"{self.hh}:{self.mm}:{self.ss}")

    def __str__(self):
        return f"{self.hh}:{self.mm}:{self.ss}"

h = hora (0,10,0)
h.mostar_hora()
print(h)


class hora2(object): 
    def __init__(self, hh = 0, mm = 0, ss = 0):
        self.ss = mm*60 + ss + hh*3600
    
    def sumar(self, other):
        total_ss = self.ss + other.ss
        

    def convertir_horario(self):
        hh = self.ss // 3600
        tmp = self.ss % 3600
        mm = tmp // 60
        ss = tmp % 60

        return (hh,mm,ss)
    

h = hora2 (0,10,0)
print(h.convertir_horario)