# Importa classe cliente
from dominio.cliente import Cliente

# Segurança
from dominio.seguranca.verificacao_login import VerificadorLogin

# Repositórios
from dominio.enums import StatusConta
from infraestrutura.repositorio_conta_memoria import RepositorioContaMemoria
from infraestrutura.repositorio_transacao_memoria import RepositorioTransacaoMemoria
from infraestrutura.repositorio_sessao_memoria import RepositorioSessaoMemoria

# Serviço
from servicos.servico_conta import ServicoConta

# Criação dos repositórios
repositorio_conta = RepositorioContaMemoria()
repositorio_transacao = RepositorioTransacaoMemoria()
repositorio_sessao = RepositorioSessaoMemoria()

# Criação do verificador de login
verificador_login = VerificadorLogin(repositorio_sessao)

# Criação do serviço bancário
servico = ServicoConta(
    repositorio_conta,
    repositorio_transacao,
    verificador_login
)

# Criação de clientes
cliente1 = Cliente("Ana")
cliente2 = Cliente("Carlos")

# Simulação de login
sessao1 = verificador_login.criar_sessao(cliente1.id)
sessao2 = verificador_login.criar_sessao(cliente2.id)

token1 = sessao1.token
token2 = sessao2.token

# Criação das contas
conta1 = servico.criar_conta(cliente1)
conta2 = servico.criar_conta(cliente2)

# Operações bancárias
servico.depositar(cliente1.id, token1, conta1, 1000)
servico.transferir(cliente1.id, token1, conta1, conta2, 300)
servico.sacar(cliente2.id, token2, conta2, 100)

# Consulta de saldo direto da conta (usa lógica interna da entidade)
saldo1 = conta1.saldo
saldo2 = conta2.saldo

# Exibição dos resultados
print("Saldo conta Ana:", saldo1)     # Esperado: 700
print("Saldo conta Carlos:", saldo2)  # Esperado: 200