class Recipiente:

    def __init__(self, tamanho: int, conteudo = 0 ):

        self.tamanho = tamanho if tamanho > 0 else 0 
        self.conteudo = conteudo
        self.limpo = True

    def esvaziar(self):
        self.tamanho = 0  

    def esta_vazio(self):
        
        if self.tamanho == 0:
            print("True")
        else:
            print("False")

    def lavar(self):
        self.tamanho = 0
        self.limpo = True

    def esta_limpo(self):
        if self.limpo:
            print("True")

        else:
            print("False")

    def estado(self):
        if self.limpo:
            # print("Limpo")
            return "Limpo"
        else:
            # print("Sujo")
            return "Sujo"

    def sujar(self):
        self.limpo = False

    def __repr__(self) -> str:
        return f"<Um recipiente {self.estado()} não especificado>"
