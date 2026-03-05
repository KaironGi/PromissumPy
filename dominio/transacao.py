from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from dominio.enums import TipoTransacao
from dominio.excecoes import ExcecaoDeDominio

# frozen = true torna a transação imutavel
# uma vez criada, nao altera
# Isso é importante para consistencia financeira