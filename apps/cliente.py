from apps import bdContas

class Cliente:
    def __init__(self,nome,senha,email,saldo):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.saldo = saldo
        self.historico = []
        self.bens = []
        
    def depositar(self,valor):
        valor = int(valor)
        self.saldo += valor
        self.mostrarSaldo()

    def sacar(self,valor):
        valor = int(valor)
        if(self.saldo > valor):
            self.saldo -= valor
            self.mostrarSaldo()
        else:
            print("Saldo Insuficiente !")

    def mostrarSaldo(self):
        print(f"Saldo: {self.saldo}")

    def mostrarDados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nSaldo: {self.saldo}")

def criarConta(nome,senha,confirmSenha,email):
    if (senha == confirmSenha):
        user = Cliente(nome,senha,email,0)
        bdContas.contas.append(user)

        print("Conta Criada Com Sucesso !")
    else:
        print("Erro no Cadastro")