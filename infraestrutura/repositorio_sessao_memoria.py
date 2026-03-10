from dominio.sessao import Sessao
from uuid import UUID

class RepositorioSessaoMemoria:

    def __init__(self):
        # Dicionário token: Sessao
        self._sessoes: dict[UUID, Sessao] = {}

    def salvar(self, sessao: Sessao):
       #salva ou atualiza a sessao
        self._sessoes[sessao.token] = sessao

    def buscar_por_token(self, token: UUID) -> Sessao | None:
        #retorna a sessao pelo token
        return self._sessoes.get(token)

    def remover(self, token: UUID):
        #Remove a sessao pelo token
        if token in self._sessoes:
            del self._sessoes[token]

    def listar_todas(self) -> list[Sessao]:
        #retorna todas as sessoes
        return list(self._sessoes.values())