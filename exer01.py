import re

class Cliente:
    def __init__(self, nome, endereco, cep, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cep = cep
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_endereco(self):
        return self.endereco
    
    def set_endereco(self, endereco):
        self.endereco = endereco
    
    def get_cep(self):
        return self.cep
    
    def set_cep(self, cep):
        self.cep = cep
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf


validaCEP = re.compile(r"^([0-9]{5}[-][0-9]{3})$")
validaCPF = re.compile(r"\d{3}\.\d{3}\.\d{3}\-\d{2}")

def exibirDados(cliente):
    print("Nome:", cliente.get_nome())
    print("Endereço:", cliente.get_endereco())
    print("CEP:", cliente.get_cep())
    print("CPF:", cliente.get_cpf())
    print()

def main():
    clientes = []

    while True:
        sair = input("Se deseja encerrar o cadastro digite: 'sair' se quiser continuar aperte qualquer tecla: ")
        if sair.lower() == "sair" or sair.lower == "Sair":
            break
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        cep = input("Digite o CEP do cliente: ")
        if validaCEP.search(cep):
            print(f"\nO CEP: {cep} é válido!!\n")
        else:
            print(f"\nO CEP: {cep} é inválido!!\n")
            break
        cpf = input("Digite o CPF do cliente: ")
        if validaCPF.search(cpf):
            print(f" \nO CPF: {cpf} é válido")
        else:
            print(f"\nO CPF: {cpf} é inválido")
            break

        
        cliente = Cliente(nome, endereco, cep, cpf)
        clientes.append(cliente)
    
        print("\nClientes:\n")
        for cliente in clientes:
            exibirDados(cliente)

if __name__ == "__main__":
    main()
