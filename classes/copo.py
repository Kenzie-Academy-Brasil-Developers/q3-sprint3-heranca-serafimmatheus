from .recipiente import Recipiente

class Copo(Recipiente):
    bebida = "água"

    def __init__(self, tamanho: int, conteudo=0):
        super().__init__(tamanho, conteudo)

    def encher(self, bebida="água"):
        if self.limpo:
            self.limpo = False
            self.conteudo = self.tamanho
            self.bebida = bebida
        else:
            print("Não se pode encher um copo sujo")

    def beber(self, quantidade: float):
        if quantidade < 0:
            print("Quantidade deve ser positiva")
        elif quantidade > self.tamanho:
            print("Não há bebida suficiente no copo")

        else:
            self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __repr__(self):
        if self.conteudo <= 0:
            return f"<um copo vazio de {self.tamanho}ml >"

        return f"<um copo de tamanho {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}>"