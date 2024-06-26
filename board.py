class Board:
    def __init__(self, board):
        self.board =  board
        self.symbol = None

        self.dic = {
            'derecha': self.derecha,
            'izquierda': self.izquierda,
            'abajo': self.abajo,
            'arriba': self.arriba,
        }
        self.corner = [[0, 0], [0, 4], [4, 0], [4, 4]]
        self.left = [[1, 0], [2, 0], [3, 0]]
        self.right = [[1, 4], [2, 4], [3, 4]]
        self.up = [[0, 1], [0, 2], [0, 3]]
        self.down = [[4, 1], [4, 2], [4, 3]]
        self.corners_m = [self.dic['arriba'], self.dic['abajo']]
        self.left_m = [self.dic['derecha'], self.dic['arriba'], self.dic['abajo']]
        self.right_m = [self.dic['izquierda'], self.dic['arriba'], self.dic['abajo']]
        self.up_m = [self.dic['abajo'], self.dic['derecha'], self.dic['izquierda']]
        self.down_m = [self.dic['arriba'], self.dic['derecha'], self.dic['izquierda']]

    
    def print_b(self):
        for row in self.board:
            print(" ".join(map(str, row)))

    def move(self, x, y, symbol):
        if self.check_move(x, y):
            self.symbol = symbol
            
            moves_dict = {
                tuple(pos): funcs for pos, funcs in zip(
                    [self.corner, self.left, self.right, self.up, self.down],
                    [self.corners_m, self.left_m, self.right_m, self.up_m, self.down_m]
                )
            }
            
            for positions, functions in moves_dict.items():
                if [x, y] in positions:
                    index = positions.index([x, y])
                    functions[index](x, y, symbol)
                    break

                

    def derecha(self, x, y, symbol):
        for i in range(y, len(self.board[x]) - 1):
            self.board[x][i] = self.board[x][i + 1]
        self.board[x][len(self.board) - 1] = symbol

    def izquierda(self, x, y, symbol):
        for i in range(y, 0, -1):
            self.board[x][i] = self.board[x][i - 1]
        self.board[x][0] = symbol

    def abajo(self, x, y, symbol):
        for i in range(x, len(self.board) - 1):
            self.board[i][y] = self.board[i + 1][y]
        self.board[len(self.board) - 1
                   ][y] = symbol

    
    def arriba(self, x, y, symbol):
        for i in range(x, 0, -1):
            self.board[i][y] = self.board[i - 1][y]
        self.board[0][y] = symbol
    
    def check_move(self, x, y):
        return self.board[x][y] == 0 or self.board[x][y] == self.symbol
    
    def check_win(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                symbol = self.board[x][y]
                if symbol != 0:
                    # Verificar horizontalmente
                    if y + 4 < len(self.board[x]):
                        if all(self.board[x][y+i] == symbol for i in range(5)):
                            return True
                    # Verificar verticalmente
                    if x + 4 < len(self.board):
                        if all(self.board[x+i][y] == symbol for i in range(5)):
                            return True
                    # Verificar diagonalmente \
                    if x + 4 < len(self.board) and y + 4 < len(self.board[x]):
                        if all(self.board[x+i][y+i] == symbol for i in range(5)):
                            return True
                    # Verificar diagonalmente /
                    if x + 4 < len(self.board) and y - 4 >= 0:
                        if all(self.board[x+i][y-i] == symbol for i in range(5)):
                            return True
        return False
