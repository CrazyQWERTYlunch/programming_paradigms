class Player:
    def __init__(self, name, symbol='X'):
        self.name = name
        self.symbol = symbol

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        self.__symbol = value


class Board:
    EMPTY_CELL = " "

    def __init__(self, size=3):
        self.size = size
        self.cells = []
        for _ in range(size):
            self.cells.append([self.EMPTY_CELL] * size)

    def __str__(self):

        result = " " * 5
        for i in range(self.size):
            result += f"{i + 1:^4}"
        line = "\n" + " " * 4 + "-" * (self.size * 4 + 1)
        result += line
        for i in range(self.size):
            row = f"{i + 1:^4}" + "|"
            for j in range(self.size):
                row += f"{str(self.cells[i][j]) :^3}" + "|"
            result += "\n" + row + line
        return result

    def set_cell(self, x, y, value):
        if self.cells[x - 1][y - 1] == self.EMPTY_CELL:
            self.cells[x - 1][y - 1] = value
        else:
            print('Ячейка уже занята символом, выбери другую')
            self.set_cell(int(input()), int(input()), value)


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = 0 if self.players[0].symbol == "X" else 1

    def turn_user(self):
        print("Ходит " + self.players[self.turn].name)

    def winner(self):
        print("Игра закончена! " + self.players[self.turn].name + " выиграл!")

    def check_win(self):
        # Проверяем горизонтали

        if self.board.cells[0][0] == self.board.cells[0][1] == self.board.cells[0][2] != self.board.EMPTY_CELL:
            return True
        if self.board.cells[1][0] == self.board.cells[1][1] == self.board.cells[1][2] != self.board.EMPTY_CELL:
            return True
        if self.board.cells[2][0] == self.board.cells[2][1] == self.board.cells[2][2] != self.board.EMPTY_CELL:
            return True
        # Проверяем вертикали
        if self.board.cells[0][0] == self.board.cells[1][0] == self.board.cells[2][0] != self.board.EMPTY_CELL:
            return True
        if self.board.cells[0][1] == self.board.cells[1][1] == self.board.cells[2][1] != self.board.EMPTY_CELL:
            return True
        if self.board.cells[0][2] == self.board.cells[1][2] == self.board.cells[2][2] != self.board.EMPTY_CELL:
            return True
        # Проверяем диагонали
        if self.board.cells[0][0] == self.board.cells[1][1] == self.board.cells[2][2] != self.board.EMPTY_CELL or \
                self.board.cells[0][2] == self.board.cells[1][1] == self.board.cells[2][0] != self.board.EMPTY_CELL:
            return True

        return False

    def check_move(self):
        pass

    def play(self):
        for i in range(9):  # максимальное количество ходов
            self.turn_user()
            print(self.board)
            self.board.set_cell(int(input()), int(input()), self.players[self.turn].symbol)
            if self.check_win():
                break
            if self.turn:
                self.turn -= 1
            else:
                self.turn += 1

        else:
            print("Ничья")
            return None  # Преждевременное завершение

        self.winner()



pr1 = Player('Nikita', 'X')

pr2 = Player('Leonid', 'O')

g1 = Game(pr1, pr2)

g1.play()

while input('Реванш?\nВыход:q').lower() != 'q':
    pr1.symbol, pr2.symbol = pr2.symbol, pr1.symbol
    g1 = Game(pr1, pr2)
    g1.play()
