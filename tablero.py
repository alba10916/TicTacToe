class tablero(self):
    def reset(self):
        pass

    def __init__(self):
        self.jugadas = {
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        }

    def dibujo(self):
        print(self.jugadas)
