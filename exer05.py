from datetime import datetime

class calcularDatas:
    def __init__(self, dt1, dt2):
        self.dt1 = datetime.strptime(dt1, "%Y-%m-%d")
        self.dt2 = datetime.strptime(dt2, "%Y-%m-%d")

    def dif_dias(self):
        difere = self.dt2 - self.dt1
        return difere.days

dt1 = input("Digite a primeira data nesse formato (YYYY-MM-DD)(ANO-MÊS-DIA): ")
dt2 = input("Digite a segunda data com o mesmo formato (YYYY-MM-DD): ")

calcular = calcularDatas(dt1, dt2)
print("Números de dias de diferença entre essas datas: ", calcular.dif_dias())