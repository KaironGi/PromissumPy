class RepositorioTransacaoMemoria:
   #REPOSITORIO DE TRANSACOES EM MEMORIA

    def __init__(self):
        self.transacoes = []  # lista que guarda todas as transações

    def registrar(self, transacao):
        #adicona as transacoes a lista
        self.transacoes.append(transacao)

    def listar_por_conta(self, conta):
        #Retorna todas as transacoes da conta
        resultado = []
        for t in self.transacoes:
            # conta pode ser origem ou destino
            if t.conta_origem == conta or t.conta_destino == conta:
                resultado.append(t)
        return resultado