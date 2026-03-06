from enum import Enum

#Representa o estado possivel de uma conta
class StatusConta (Enum):
    ATIVO = "ATIVO"
    ENCERRADO = "ENCERRADO"
    BLOQUEADO = "BLOQUEADO"

#CLiente
class StatusCliente(Enum):
    ATIVO = "ATIVO"
    ENCERRADO = "ENCERRADO"
    BLOQUEADO = "BLOQUEADO"

#Tipos de transação
class TipoTransacao(Enum):
    DEPOSITAR = "DEPOSITAR"
    SACAR = "SACAR"
    TRANSFERENCIA = "TRANSFERENCIA"