import math

class Operacoes:
    def soma(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2
    
    def multi(self, n1, n2):
        return n1 * n2
    
    def rad(self, n):
        return math.sqrt(n)
    
    def fatorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.fatorial(n - 1)

calcular = Operacoes()

print("Soma: ", calcular.soma(5, 5))
print("Subtração: ", calcular.sub(6, 2))
print("Multiplicação: ", calcular.multi(3, 2))
print("Radiciação: ", calcular.rad(25))
print("Fatorial: ", calcular.fatorial(5))