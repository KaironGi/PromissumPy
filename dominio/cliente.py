import uuid

class Cliente:

    def __init__(self, nome):

        self.id = uuid.uuid4()

        self.nome = nome