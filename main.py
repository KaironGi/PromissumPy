# Importa classe cliente
from dominio.cliente import Cliente

# Importa repositórios
from infraestrutura.repositorio_conta_memoria import RepositorioContaMemoria
from infraestrutura.repositorio_transacao_memoria import RepositorioTransacaoMemoria

# Importa serviço bancário
from servicos.servico_conta import ServicoConta


# Criação dos repositórios
repositorio_conta = RepositorioContaMemoria()
repositorio_transacao = RepositorioTransacaoMemoria()

# Criação do serviço bancário
servico = ServicoConta(repositorio_conta, repositorio_transacao)


# Criação de clientes
cliente1 = Cliente("Ana")
cliente2 = Cliente("Carlos")


# Criação das contas
conta1 = servico.criar_conta(cliente1)
conta2 = servico.criar_conta(cliente2)


# Operações bancárias
servico.depositar(conta1, 1000)

servico.transferir(conta1, conta2, 300)

servico.sacar(conta2, 100)


# Consulta de saldo
saldo1 = servico.calcular_saldo(conta1)
saldo2 = servico.calcular_saldo(conta2)


# Exibição dos resultados
print("Saldo conta Ana:", saldo1)
print("Saldo conta Carlos:", saldo2)