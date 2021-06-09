class Tablero:
    X = 1
    O = -1
    posibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.reset()

    def reset(self):
        self.jugadas = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]
        self.posibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def dibuja(self):
        print('-------------')
        print(f' {self.jugadas[0]} |  {self.jugadas[1]} | {self.jugadas[2]}\n')
        print(f' {self.jugadas[3]} |  {self.jugadas[4]} | {self.jugadas[5]}\n')
        print(f' {self.jugadas[6]} |  {self.jugadas[7]} | {self.jugadas[8]}')
        print('-------------')

    def jugadasLibres(self):
        return self.posibilidades

    def introducirJugada(self, jugador, jugada):

        self.jugadas[jugada-1] = jugador.ficha

        print(jugada)
        print(type(jugada))
        print(self.jugadas)

        self.posibilidades.remove(jugada)
        self.dibuja()
