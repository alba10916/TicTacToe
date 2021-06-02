class Tablero:
    X = 1
    Y = -1
    POSIBILIDADES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.reset()

    def reset(self):
        self.jugadas = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

    def dibujo(self):
        print(f'----{self.jugadas}---')

    def jugadasLibres(self):
        while jugada not in self.POSIBILIDADES:
            if not first:
                print('lokoooooo')
            first = False
            jugada = input(f'El jugador {self.ficha} elige una posicion posible del {self.POSIBILIDADES}:')
            try:
                jugada = int(jugada)
            except ValueError:
                print("TAS GTO LOKO WROOONG")
        
        self.POSIBILIDADES.remove(jugada)
    def cuenta(self):
        pass
        
