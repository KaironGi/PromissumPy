from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from dominio.enums import TipoTransacao
from dominio.excecoes import ExcecaoDeDominio

# frozen = true torna a transação imutavel
# uma vez criada, nao altera
# Isso é importante para consistencia financeira
@dataclass(frozen=True)
class Transacao:

    tipo: TipoTransacao
    operacao_id:UUID
    valor:Decimal
    transacao_original:UUID | None = None
    conta_destino:UUID | None = None
    conta_origem:UUID | None = None

    id:UUID = field(default_factory=uuid4)

    #data/hora
    criada_em: datetime = field(default_factory = datetime.utcnow)

    #executar automaticamente apois init
    def __post_init__(self):

        #operação nao pode ser nula
        if not self.operacao_id:
            raise ExcecaoDeDominio("Operação obrigatória")
        
        #tipo deve existir
        if not self.tipo:
            raise ExcecaoDeDominio("Tipo obrigatório")
        
        #valor deve ser positivo
        if not self.valor or self.valor <= Decimal("0"):
            raise ExcecaoDeDominio("Valor inválido")
        
    #Cria uma transaçãop de estorno com base na atual
    def criar_estorno(self, operacao_estorno: UUID) -> "Transacao":

        #Impedir estorno de estorno
        if self.transacao_original:
            raise ExcecaoDeDominio("Estorno de estorno não é permitido")
        
        #inverte o tipo
        tipo_estorno = (
            TipoTransacao.SACAR
            if self.tipo == TipoTransacao.DEPOSITAR
            else TipoTransacao.DEPOSITAR
        )

        #retorna uma nova transação com base na original
        return Transacao(
            tipo = tipo_estorno,
            operacao_id = operacao_estorno,
            valor = self.valor,
            transacao_original = self.id,
        )