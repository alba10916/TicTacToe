from mensajes import mensajes


class Tablero:
    posibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.reset()

    def reset(self):
        self.jugadas = mensajes["jugadas"]
        self.valorNumerico = mensajes["valorNumerico"]
        self.posibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def dibuja(self):
        print('-------------')
        print(f' {self.jugadas[6]} |  {self.jugadas[7]} | {self.jugadas[8]}\n')
        print(f' {self.jugadas[3]} |  {self.jugadas[4]} | {self.jugadas[5]}\n')
        print(f' {self.jugadas[0]} |  {self.jugadas[1]} | {self.jugadas[2]}')
        print('-------------')

    def jugadasLibres(self):
        return self.posibilidades

    def introducirJugada(self, jugador, jugada):

        self.jugadas[jugada-1] = jugador.ficha
        self.valorNumerico[jugada-1] = jugador.code
        self.posibilidades.remove(jugada)
        self.dibuja()

    def comprobarVictoria(self, jugador):
        diagonal1 = self.valorNumerico[0] + self.valorNumerico[4] + self.valorNumerico[8]
        diagonal2 = self.valorNumerico[2] + self.valorNumerico[4] + self.valorNumerico[6]
        columna1 = self.valorNumerico[0] + self.valorNumerico[3] + self.valorNumerico[6]
        columna2 = self.valorNumerico[1] + self.valorNumerico[4] + self.valorNumerico[7]
        columna3 = self.valorNumerico[2] + self.valorNumerico[5] + self.valorNumerico[8]
        fila1 = self.valorNumerico[0] + self.valorNumerico[1] + self.valorNumerico[2]
        fila2 = self.valorNumerico[3] + self.valorNumerico[4] + self.valorNumerico[5]
        fila3 = self.valorNumerico[6] + self.valorNumerico[7] + self.valorNumerico[8]
        msg = {"ficha": jugador.ficha}
        ganar = mensajes["ganar"].format(**msg)
        if diagonal1 == 3 or diagonal1 == (-3):
            print(ganar)
            exit()
        if diagonal2 == 3 or diagonal2 == (-3):
            print(ganar)
            exit()
        if columna1 == 3 or columna1 == (-3):
            print(ganar)
            exit()
        if columna2 == 3 or columna2 == (-3):
            print(ganar)
            exit()
        if columna3 == 3 or columna3 == (-3):
            print(ganar)
            exit()
        if fila1 == 3 or fila1 == (-3):
            print(ganar)
            exit()
        if fila2 == 3 or fila2 == (-3):
            print(ganar)
            exit()
        if fila3 == 3 or fila3 == (-3):
            print(ganar)
            exit()
