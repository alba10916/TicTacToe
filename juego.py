from tablero import Tablero
from jugador import Jugador


class Juego:
    DURACION = 9
    FICHA = ['X', 'Y']

    def __init__(self):
        self.tablero = Tablero()
        self.reset()
        self.juega()

    def reset(self):
        self.jugador = [
            Jugador(self.FICHA[0]),
            Jugador(self.FICHA[1])
        ]
        self.tablero.reset()
        self.turno = 0

    def juega(self):
        self.tablero.dibujo()
        while self.turno < self.DURACION:
            

            jugada = jugador.elegir(jugadasLibres)
            self.turno += 1
            # self.tablero.dibuja()
