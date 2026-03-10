from uuid import uuid4
from decimal import Decimal

from dominio.enums import TipoTransacao
from dominio.transacao import Transacao
from dominio.conta import Conta
from dominio.excecoes import ExcecaoDeDominio
from dominio.validadores.validador_conta import ValidadorConta


# Classe da lógica
class ServicoConta:

    # Construtor
    def __init__(self, repositorio_conta, repositorio_transacao, verificador_login):

        self.repositorio_conta = repositorio_conta
        self.repositorio_transacao = repositorio_transacao
        self.verificador_login = verificador_login


    def criar_conta(self, cliente):

        conta = Conta(cliente.id)

        self.repositorio_conta.salvar(conta)

        return conta


    # Calculo de saldo baseado nas transacoes
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


    # Realiza depósito
    def depositar(self, user_id, token, conta, valor):

        self.verificador_login.verificar_acesso(user_id, token)

        if conta.cliente_id != user_id:
            raise ExcecaoDeDominio("Usuário não autorizado a operar esta conta")

        if valor <= 0:
            raise ExcecaoDeDominio("Valor inválido")

        ValidadorConta.verificar_conta_ativa(conta)

        # chama a lógica da entidade
        conta.depositar(
            operacao_id=uuid4(),
            valor=valor,
            versao_esperada=conta.versao
        )

        # salva a conta atualizada
        self.repositorio_conta.salvar(conta)


    # Realiza saque
    def sacar(self, user_id, token, conta, valor):

        self.verificador_login.verificar_acesso(user_id, token)

        if conta.cliente_id != user_id:
            raise ExcecaoDeDominio("Usuário não autorizado a operar esta conta")

        if valor <= 0:
            raise ExcecaoDeDominio("Valor inválido")

        ValidadorConta.verificar_conta_ativa(conta)

        # chama a lógica da entidade
        conta.sacar(
            operacao_id=uuid4(),
            valor=valor,
            versao_esperada=conta.versao
        )

        # salva conta atualizada
        self.repositorio_conta.salvar(conta)


    # Realiza transferência entre contas
    def transferir(self, user_id, token, origem, destino, valor):

        self.verificador_login.verificar_acesso(user_id, token)

        if origem.cliente_id != user_id:
            raise ExcecaoDeDominio("Usuário não autorizado a operar esta conta")

        if valor <= 0:
            raise ExcecaoDeDominio("Valor inválido")

        ValidadorConta.verificar_conta_ativa(origem)
        ValidadorConta.verificar_conta_ativa(destino)

        saldo = origem.saldo

        if saldo < valor:
            raise ExcecaoDeDominio("Saldo insuficiente")

        # saque da origem
        origem.sacar(
            operacao_id=uuid4(),
            valor=valor,
            versao_esperada=origem.versao
        )

        # depósito no destino
        destino.depositar(
            operacao_id=uuid4(),
            valor=valor,
            versao_esperada=destino.versao
        )

        # salva ambas contas
        self.repositorio_conta.salvar(origem)
        self.repositorio_conta.salvar(destino)