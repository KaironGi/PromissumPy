from uuid import uuid4


class Sessao:

    def __init__(self, user_id):
        # ID do usuário dono da sessão
        self.user_id = user_id

        # Token único usado para autenticação
        self.token = uuid4()

        # Define se a sessão ainda está ativa
        self.ativa = True

    def encerrar(self):
        # Método usado para logout
        self.ativa = False