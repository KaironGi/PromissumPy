class RepositorioTransacaoMemoria:

    # Construtor do repositório
    def __init__(self):

        self.transacoes = []

    def registrar(self, transacao):

        self.transacoes.append(transacao)

    def listar_por_conta(self, conta):

        resultado = []

        #Percorre as transacoes
        for t in self.transacoes:

            if t.conta_origem == conta or t.conta_destino == conta:

                resultado.append(t)

        return resultado