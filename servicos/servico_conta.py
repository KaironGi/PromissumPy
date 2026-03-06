from uuid import uuid4
from decimal import Decimal

from dominio.enums import TipoTransacao, StatusConta
from dominio.transacao import Transacao
from dominio.conta import Conta
from dominio.excecoes import ExcecaoDeDominio


#Classe da logica 
class ServicoConta:

    #Construtor
    def __init__(self, repositorio_conta, repositorio_transacao):

        self.repositorio_conta = repositorio_conta
        self.repositorio_transacao = repositorio_transacao

    def criar_conta(self, cliente):

        conta = Conta(cliente.id)

        self.repositorio_conta.salvar(conta)

        return conta

    #Calculo de saldo baseado nas transacoes
    def calcular_saldo(self, conta):

        transacoes = self.repositorio_transacao.listar_por_conta(conta)

        saldo = Decimal("0")

        for t in transacoes:

            if t.tipo == TipoTransacao.DEPOSITAR and t.conta_destino == conta:
                saldo += t.valor

            elif t.tipo == TipoTransacao.SACAR and t.conta_origem == conta:
                saldo -= t.valor

            elif t.tipo == TipoTransacao.TRANSFERENCIA:

                if t.conta_origem == conta:
                    saldo -= t.valor

                if t.conta_destino == conta:
                    saldo += t.valor

        return saldo

    #Realiza depósito
    def depositar(self, conta, valor):

        if valor <= 0:
            raise ExcecaoDeDominio("Valor inválido")

        # Verifica se conta está ativa
        if conta.status != StatusConta.ATIVO:
            raise ExcecaoDeDominio("Conta não está ativa")

        # Cria transação de depósito
        transacao = Transacao(
            tipo=TipoTransacao.DEPOSITAR,
            operacao_id=uuid4(),
            valor=valor,
            conta_destino=conta
        )

        self.repositorio_transacao.registrar(transacao)

    # Realiza saque
    def sacar(self, conta, valor):

        if valor <= 0:
            raise ExcecaoDeDominio("Valor inválido")

        if conta.status != StatusConta.ATIVO:
            raise ExcecaoDeDominio("Conta não está ativa")

        saldo = self.calcular_saldo(conta)

        if saldo < valor:
            raise ExcecaoDeDominio("Saldo insuficiente")

        transacao = Transacao(
            tipo=TipoTransacao.SACAR,
            operacao_id=uuid4(),
            valor=valor,
            conta_origem=conta
        )

        self.repositorio_transacao.registrar(transacao)

    # Realiza transferência entre contas
    def transferir(self, origem, destino, valor):

        if valor <= 0:
            raise ExcecaoDeDominio("Valor inválido")

        if origem.status != StatusConta.ATIVO:
            raise ExcecaoDeDominio("Conta origem inativa")

        if destino.status != StatusConta.ATIVO:
            raise ExcecaoDeDominio("Conta destino inativa")

        saldo = self.calcular_saldo(origem)

        if saldo < valor:
            raise ExcecaoDeDominio("Saldo insuficiente")

        transacao = Transacao(
            tipo=TipoTransacao.TRANSFERENCIA,
            operacao_id=uuid4(),
            valor=valor,
            conta_origem=origem,
            conta_destino=destino
        )

        self.repositorio_transacao.registrar(transacao)