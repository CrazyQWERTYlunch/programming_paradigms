class Player:
    __total_wins = 0

    def __init__(self, name, symbol='X'):
        self.name = name
        self.symbol = symbol

    def touch(self):
        return self.__symbol

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        self.__symbol = value

    def get_total_wins(self):
        return self.__total_wins

    def wins(self):
        self.__total_wins += 1


class Board:
    EMPTY_CELL = " "

    def __init__(self, size=3):
        self.size = size
        self.count = size * size
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
        if self.cells[x - 1][y - 1] == " ":
            self.cells[x - 1][y - 1] = value
            self.count -= 1
        else:
            print('Ячейка уже занята символом, выбери другую')
            self.set_cell(int(input()),int(input()), value)

class Game():

    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0

    def turn_user(self):
        print("Ходит " + self.players[self.turn].name)

    def winner(self):
        print("Игра закончена! " + self.players[self.turn - 1].name + "выиграл")

    def check_win(self):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтали
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикали
            (0, 4, 8), (2, 4, 6)  # Диагонали
        ]
        for combo in win_combinations:
            # Если все три ячейки в одной из победных комбинаций содержат один и тот же символ и не пусты, то есть победитель
            if self.board.cells[combo[0]] == self.board.cells[combo[1]] == self.board.cells[combo[2]] != " ":
                return True
        return False

    def check_move(self):
        return not self.board.count

    def game_over(self):
        return self.check_win() or self.check_move()

    def play(self):
        while self.game_over():
            self.turn_user()
            print(self.board)
            self.board.set_cell(int(input()), int(input()), self.players[self.turn].symbol)
            self.board.count -= 1
            if self.turn:
                self.turn -= 1
            else:
                self.turn += 1
        self.winner()


pr1 = Player('Name1', 'X')

pr2 = Player('Name2', 'O')


b1 = Board()

g1 = Game(b1,pr1,pr2)
g1.play()

