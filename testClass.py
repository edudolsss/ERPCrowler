from apps import cliente as defs
from apps import bdContas as bd


cliente = defs.criarConta("Eduardo Pinheiro","eduardosp04@outlook.com")
# cliente.depositar(100)
# cliente.sacar(20)
# cliente.mostrarDados()

for cliente in bd.contas:
    print(f"Nome: {cliente['nome']} \nE-mail: {cliente['email']} \nSaldo: {cliente['saldo']}\n")
