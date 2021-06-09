class Jugador:

    def __init__(self, ficha, code):
        self.ficha = ficha
        self.code = code

    def elegimos(self, posibilidades):

        # posibilidades = self.posibilidades
        jugada = None
        # jugada = int(input(f'El jugador {self.ficha} elige una posicion posible de { posibilidades }:'))        
        # print(f'El jugador{self.ficha} elige esta posicion{posibilidades}')
        while jugada not in posibilidades:
            first = True
            if not first:
                print('segunda partida')
            first = False
            jugada = input(f'El jugador {self.ficha} elige una posicion posible del {posibilidades}:')
            try:
                jugada = int(jugada)
            except ValueError:
                print("Error, elija un numero incluido en la lista")

        return jugada
