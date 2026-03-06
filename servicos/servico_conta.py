from uuid import UUID
from dominio.conta import Conta
from dominio.excecoes import ExcecaoDeDominio

class RepositorioContaMemoria:
    """
    Repositório em memória que simula um banco de dados
    Vai armazenar contas em um dicionario onde
    chave = id da conta
    valor = obj da conta
    """

    def __init__(self):
        #Estrutura interna que guarda as contas
        self._contas: dict[UUID, Conta] = {}

    def salvar(self, conta: Conta):
        #Salva ou atualiza uma conta, se ela ja existir, vai ser sobrescrita
        self._contas[conta.id] = conta
    
    def buscar_por_id(self, conta_id:UUID) -> Conta:
        #Busca uma conta por ID
        conta = self._contas.get(conta_id)

        if not conta:
            raise ExcecaoDeDominio("Conta não encontrada")
        
        return conta
    
    def listar(self) -> list[Conta]:
        #retorna as contas cadastradas
        return list(self._contas.values())
    
    def existe(self, conta_id:UUID) -> bool:
        #Verifica se a conta existe
        return conta_id in self._contas
