# Repositório responsável por armazenar contas em memória
class RepositorioContaMemoria:

    # Construtor do repositório
    def __init__(self):

        # Lista que armazenará todas as contas criadas
        self.contas = []

    # Salva uma nova conta
    def salvar(self, conta):

        # Adiciona a conta na lista
        self.contas.append(conta)

    # Busca uma conta pelo ID
    def buscar_por_id(self, id_conta):

        # Percorre todas as contas
        for conta in self.contas:

            # Se encontrar o ID correspondente
            if conta.id == id_conta:
                return conta

        # Caso não encontre
        return None