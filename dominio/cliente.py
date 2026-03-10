import uuid


class Cliente:

    def __init__(self, nome):

        # Identificador único do cliente no sistema
        self.id = uuid.uuid4()

        # Nome do cliente
        self.nome = nome