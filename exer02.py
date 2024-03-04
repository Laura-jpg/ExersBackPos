class verificarPrimos:
    def contarPrimos(self, ini, fim):
        qntPrimos = 0
        for n in range(ini, fim + 1):
            if self.primo(n):
                qntPrimos += 1
        return qntPrimos

    def primo (self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

obj = verificarPrimos()
x = obj.contarPrimos(5, 20)
print("\nA quantidade de números primos nesse intervalo é: ", x)

