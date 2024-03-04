import math

class calcularAreas:
    def calcularCirc(self, areaCirculo):
        return math.pi * areaCirculo ** 2

    def calcularQuad(self, l1, l2):
        return l1 * l2

    def calcularPerTri(self, l1, l2, l3):
        return l1 + l2 + l3

    def calcularAreaTri(self, base, altura):
        return (base * altura) / 2

    def calcularTriCoor(self, x, y):
        area = 0 
        for i in range (len(x) - 1):
            area += (x[i] * y[i + 1]) - (x[i + 1] * y[i])
        area += (x[-1] * y[0]) - (x[0] * y[-1])
        return abs(area / 2)

    def calcular(self, texto):
        return "Uso incorreto!"

calcularFormas = calcularAreas()

print("Área do círculo: ", calcularFormas.calcularCirc(5.0))
print("Área do quadrado:", calcularFormas.calcularQuad(4.0, 5.0))
print("Perímetro do triângulo: ", calcularFormas.calcularPerTri(3, 4, 5))
print("Área do triângulo: ", calcularFormas.calcularAreaTri(5, 3.0))
print("Área do triangulo com coordenadas: ", calcularFormas.calcularTriCoor([0, 3, 0], [0, 0, 4]))
print("Uso incorreto: ", calcularFormas.calcular("texto"))