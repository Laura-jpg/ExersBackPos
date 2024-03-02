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
        cpf = input("Digite o CPF do cliente: ")
        
        cliente = Cliente(nome, endereco, cep, cpf)
        clientes.append(cliente)
    
        print("\nClientes:\n")
        for cliente in clientes:
            exibirDados(cliente)

if __name__ == "__main__":
    main()
