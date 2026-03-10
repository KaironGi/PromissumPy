from dominio.excecoes import ExcecaoDeDominio
from dominio.sessao import Sessao

class VerificadorLogin:

    def __init__(self, repositorio_sessao):
        # Armazena repositório de sessões
        self.repositorio_sessao = repositorio_sessao  

    def criar_sessao(self, user_id):
        # Cria nova sessão
        sessao = Sessao(user_id)  

        # Salva sessão no repositório       
        self.repositorio_sessao.salvar(sessao)  

         # Retorna a sessão criada
        return sessao                                 
    def verificar_acesso(self, user_id, token):
        # Busca sessão pelo token
        sessao = self.repositorio_sessao.buscar_por_token(token)  

        if not sessao:
             # Token não encontrado
            raise ExcecaoDeDominio("Sessão inválida")           

        if not sessao.ativa:
             # Sessão foi encerrada
            raise ExcecaoDeDominio("Sessão encerrada")          

        if sessao.user_id != user_id:
            # Token não pertence ao usuário
            raise ExcecaoDeDominio("Usuário inválido")           