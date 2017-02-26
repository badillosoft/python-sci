import math

class Robot:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
    
    def avanzar(self):
        d = 1
        self.x += d * math.cos(self.a)
        self.y += d * math.sin(self.a)
    
    def girar_izq(self):
        da = 2 * math.pi / 36
        self.a -= da
    
    def girar_der(self):
        da = 2 * math.pi / 36
        self.a += da

    def __str__(self):
        return "%.2f %.2f (%.2f)" % (self.x, self.y, self.a)

r = Robot()

print r

r.avanzar()

print r

r.girar_izq()
r.avanzar()

print r
