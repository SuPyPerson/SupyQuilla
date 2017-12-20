"""
O tesouro Inca de Mamaquilla
"""
from random import shuffle
CIRCLE = 9310

class Baralho :
    """
    Cartas do Jogo
    """


    def __init__(self, jogo):
        self.jogo = jogo
        self.baralho = [carta for carta in range(1, 31)]
        shuffle(self.baralho)
        for carta in self.baralho:
            if self.jogo.decide ():
                print("terminou")
                break
            self.jogo.apresenta_carta(carta)



class Jogo :
    """
    O jogo do Tesouro Inca
    """
    def __init__(self):
        self.mapa = {c: chr(CIRCLE+c) for c in range(1,16) }
        self.baralho = Baralho(self)
    def apresenta_carta(self, carta):
        carta = self.mapa[carta] if carta in self.mapa else carta
        print(carta,end=" ")
    def decide(self):


        decidiu =     input("(s)sai ou (f)fica")
        return decidiu == "s"

if __name__ == "__main__":
    Jogo()