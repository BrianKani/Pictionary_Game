"""defines the state of the playing board"""

class Board():
    ROWS, COLUMNS = 720

    def __init__(self):
        self.data = self._create_empty_board()

    def _create_empty_board(self):
        return [[(255,255,255) for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
    
    def update(self, x,y,color):
        self.data[x][y]=color

    def clear(self):
        self.data = self._create_empty_board()

    def fill(self,x,y):
        pass

    def get_board(self):
        return self.data





        


