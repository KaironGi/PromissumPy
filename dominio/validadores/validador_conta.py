from dominio.excecoes import ExcecaoDeDominio
from dominio.enums import StatusConta


class ValidadorConta:

    @staticmethod
    def verificar_conta_ativa(conta):
        
        #Verifica se a conta está ativa antes da operação
    
        if conta.status != StatusConta.ATIVO:
            raise ExcecaoDeDominio("Conta não está ativa")