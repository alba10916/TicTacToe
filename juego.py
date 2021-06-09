from tablero import Tablero
from jugador import Jugador


class Juego:
    DURACION = 9
    FICHA = ['X', 'O']

    def __init__(self):
        self.tablero = Tablero()
        self.reset()
        self.juega()

    def reset(self):
        self.jugador = [
            Jugador(self.FICHA[0], -1),
            Jugador(self.FICHA[1], 1)
         ]
        self.tablero.reset()
        self.turno = 0

    def juega(self):
        self.tablero.dibuja()
        while self.turno < self.DURACION:
            jugador = self.jugador[self.turno % 2]
            self.turno += 1
            jugada = jugador.elegimos(self.tablero.jugadasLibres())
            self.tablero.introducirJugada(jugador, jugada)
            self.tablero.comprobarVictoria(jugador)
        print('\n Habeis empatado, otra vez sera.....')    
