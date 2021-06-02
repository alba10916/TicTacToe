class Jugador:
    

    def __init__(self, ficha):
        self.ficha = ficha

    def elegir(self):
        jugada = None
        first = True

        jugada = input(f'El jugador {self.ficha} elige una posicion posible del {self.POSIBILIDADES}:')
        

        


        # self.POSIBILIDADES.remove(self.POSIBILIDADES.index(jugada))


        #while jugada not in self.POSIBILIDADES:
        #    jugada = input(f'El jugador {self.ficha} debe elegir una posicion valida: ')

        
        print(f'El jugador{self.ficha} elige esta posicion{jugadasLibres}')
