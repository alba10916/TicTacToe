from mensajes import mensajes


class Jugador:

    def __init__(self, ficha, code):
        self.ficha = ficha
        self.code = code

    def elegimos(self, posibilidades):

        jugada = None
        while jugada not in posibilidades:
            first = True
            if not first:
                print('segunda partida')
            first = False
            jugada = input(mensajes["elegir"])
            try:
                jugada = int(jugada)
            except ValueError:
                print(mensajes["error"])

        return jugada
