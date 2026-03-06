from decimal import Decimal
from uuid import UUID, uuid4

from dominio.enums import StatusConta, TipoTransacao
from dominio.excecoes import ExcecaoDeDominio
from dominio.transacao import Transacao

class Conta:
    #Construtor da conta
    def __init__(self,cliente_id:UUID):
        #Cliente é obrigatorio
        if not cliente_id:
            raise ExcecaoDeDominio("Cliente obrigatório")
        
        #Identificador
        self.id = uuid4()

        #dono da conta
        self.cliente_id = cliente_id

        #conta inicia ativa
        self.status = StatusConta.ATIVO

        #lista interna de transações
        self._transacoes: list[Transacao] = []

        #guarda operações já processadas
        self._operacoes_processadas = set[UUID] = set()

        #Controle de concorrencia otimista
        self._versao = 0

    #Retorna a versao atual
    @property
    def versao(self) -> int:
        return self._versao
    
    #saldo é calculado dinamicamente
    @property
    def saldo(self) -> Decimal:
        saldo = Decimal("0")

        #percorre as transaçoes
        for t in self._transacoes:
            #soma
            if t.tipo == TipoTransacao.DEPOSITAR:
                saldo += t.valor

            #saque
            else:
                saldo -= t.valor

        return saldo
    
    #OPERAÇÔES DE NEGOCIO
    #OPERAÇÔES DE NEGOCIO
    #OPERAÇÔES DE NEGOCIO
    #OPERAÇÔES DE NEGOCIO
    #OPERAÇÔES DE NEGOCIO
    #OPERAÇÔES DE NEGOCIO


def depositar(self, operacao_id:UUID, valor:Decimal, versao_esperada: int):

    #valida status, versao e duplicidade
    self._validar_operacao(operacao_id, versao_esperada)

    #cria nova transacao
    transacao = Transacao(operacao_id, TipoTransacao.DEPOSITAR, valor)

    #Registra no sistema
    self._registrar(transacao)


def sacar(self, operacao_id:UUID, valor:Decimal, versao_esperada: int):

    self._validar_operacao(operacao_id, versao_esperada)

    #verifica saldo
    if valor > self.saldo:
        raise ExcecaoDeDominio("Saldo insuficiente")
    
    transacao = Transacao(operacao_id, TipoTransacao.SACAR, valor)

    self._registrar(transacao)

def estornar(self, operacao_id:UUID, valor:Decimal, versao_esperada: int):

    self._validar_operacao(operacao_id, versao_esperada)

    #busca transacao original
    original = next(
        (t for t in self.transacoes if t.id == transacao_id),
        None,
    )

    #impede estorno duplicado
    if any(t.transacao_original == transasao._id for t in self._transacoes):
        raise ExcecaoDeDominio("Transação já estornada")
    
    estorno = original.criar_estorno(operacao_id)

    self.registrar(estorno)

def bloquear (self):
    if self.status != StatusConta.ATIVO:
        raise ExcecaoDeDominio("Conta não pode ser bloqueada")
    self.status = StatusConta.BLOQUEADO

def encerrar (self):
    if self.status == StatusConta.ENCERRADO:
        raise ExcecaoDeDominio("Conta já encerrada")
    
    if self.saldo != Decimal("0"):
        raise ExcecaoDeDominio("Conta com saldo não pode ser encerrada")
    
    self.status = StatusConta.ENCERRADO

#METODOS INTERNOS
#METODOS INTERNOS
#METODOS INTERNOS
#METODOS INTERNOS
#METODOS INTERNOS
#METODOS INTERNOS

def _validar_operacao(self, operacao_id:UUID, versao_esperada: int):

    #conta deve estar ativa
    if self.status != StatusConta.ATIVO:
        raise ExcecaoDeDominio("Conta não está ativa")
    
    #Idempotência
    if operacao_id in self._operacoes_processadas:
        raise ExcecaoDeDominio("Operação já processada")
    
    #Controle de concorrencia otimista
    if self._versao != versao_esperada:
        raise ExcecaoDeDominio("Conflito de concorrência")

def _registrar(self, transacao: Transacao):

    #adiciona transação
    self._transacoes.append(transacao)

    #marca como processada
    self._operacoes_processadas.add(transacao.operacao_id)

    #versao
    self._versao += 1
    