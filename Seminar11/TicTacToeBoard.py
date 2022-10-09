# Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:
# new_game() - для создания новой игры;
# get_field() - для получения поля (список списков);
# check_field() - для проверки, есть ли победитель, который возвращает X, если победил первый игрок, 0, если второй, D, если ничья и None, 
# если можно продолжать игру; • make_move(row, col) - который устанавливает значение текущего хода в ячейку поля с координатами row, col, 
# если это возможно, «переключает» ход игрока, а также возвращает сообщение «Победил игрок X» при победе крестиков, «Победил игрок 0» при победе ноликов, 
# «Ничья» в случае ничьей и «Продолжаем играть», если победитель после данного хода неопределён.
# Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята», если в клетке уже стоит крестик или нолик, 
# и «Игра уже завершена», если в текущей игре уже выявлен победитель или закончились ячейки для ходов.
# При создании объекта класса должна создаваться новая игра. Аргументы row и col метода make.move могут принимать значения от 1 до 3.

class TicTacToeBoard:

    def __init__(self):
            self.clear_place = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            self.p = self.clear_place
            self.end_info = 0
            self.list = ['X', '0']
            self.n = 1
    
    def new_game(self):
        self.clear_place = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.p = self.clear_place
        self.end_info = 0
        self.list = ['X', '0']
        self.n = 1
    
    def get_field(self):
        return self.p
    
    def check_field(self):
        if (self.p[0][0] == 'X' and
            self.p[0][1] == 'X' and
                self.p[0][2] == 'X') or \
                (self.p[1][0] == 'X' and
                self.p[1][1] == 'X' and
                self.p[1][2] == 'X') or \
                (self.p[2][0] == 'X' and
                self.p[2][1] == 'X' and
                self.p[2][2] == 'X') or \
                (self.p[0][0] == 'X' and
                self.p[1][1] == 'X' and
                self.p[2][2] == 'X') or \
                (self.p[0][2] == 'X' and
                self.p[1][1] == 'X' and
                self.p[2][0] == 'X') or \
                (self.p[0][0] == 'X' and
                self.p[1][0] == 'X' and
                self.p[2][0] == 'X') or \
                (self.p[0][1] == 'X' and
                self.p[1][1] == 'X' and
                self.p[2][1] == 'X') or \
                (self.p[0][2] == 'X' and
                self.p[1][2] == 'X' and
                self.p[2][2] == 'X'):
            return 'X'
        elif (self.p[0][0] == '0' and
            self.p[0][1] == '0' and
            self.p[0][2] == '0') or \
                (self.p[1][0] == '0' and
                self.p[1][1] == '0' and
                self.p[1][2] == '0') or \
                (self.p[2][0] == '0' and
                self.p[2][1] == '0' and
                self.p[2][2] == '0') or \
                (self.p[0][0] == '0' and
                self.p[1][1] == '0' and
                self.p[2][2] == '0') or \
                (self.p[0][2] == '0' and
                self.p[1][1] == '0' and
                self.p[2][0] == '0') or \
                (self.p[0][0] == '0' and
                self.p[1][0] == '0' and
                self.p[2][0] == '0') or \
                (self.p[0][1] == '0' and
                self.p[1][1] == '0' and
                self.p[2][1] == '0') or \
                (self.p[0][2] == '0' and
                self.p[1][2] == '0' and
                self.p[2][2] == '0'):
            return '0'
        elif '-' not in self.p[0] and \
                '-' not in self.p[1] and \
                '-' not in self.p[2]:
            return 'D'
        else:
            return 'None'
    
    def make_move(self, row, col):
        if self.p[row - 1][col - 1] == '-':
            self.n += 1
            self.p[row - 1][col - 1] = self.list[self.n % 2]
            if (self.p[0][0] == 'X' and
                self.p[0][1] == 'X' and
                self.p[0][2] == 'X') or \
                    (self.p[1][0] == 'X' and
                    self.p[1][1] == 'X' and
                    self.p[1][2] == 'X') or \
                    (self.p[2][0] == 'X' and
                    self.p[2][1] == 'X' and
                    self.p[2][2] == 'X') or \
                    (self.p[0][0] == 'X' and
                    self.p[1][1] == 'X' and
                    self.p[2][2] == 'X') or \
                    (self.p[0][2] == 'X' and
                    self.p[1][1] == 'X' and
                    self.p[2][0] == 'X') or \
                    (self.p[0][0] == 'X' and
                    self.p[1][0] == 'X' and
                    self.p[2][0] == 'X') or \
                    (self.p[0][1] == 'X' and
                    self.p[1][1] == 'X' and
                    self.p[2][1] == 'X') or \
                    (self.p[0][2] == 'X' and
                    self.p[1][2] == 'X' and
                    self.p[2][2] == 'X'):
                self.end_info = 'Игра уже завершена'
                return 'Победил игрок X'
            elif (self.p[0][0] == '0' and
                self.p[0][1] == '0' and
                self.p[0][2] == '0') or \
                    (self.p[1][0] == '0' and
                    self.p[1][1] == '0' and
                    self.p[1][2] == '0') or \
                    (self.p[2][0] == '0' and
                    self.p[2][1] == '0' and
                    self.p[2][2] == '0') or \
                    (self.p[0][0] == '0' and
                    self.p[1][1] == '0' and
                    self.p[2][2] == '0') or \
                    (self.p[0][2] == '0' and
                    self.p[1][1] == '0' and
                    self.p[2][0] == '0') or \
                    (self.p[0][0] == '0' and
                    self.p[1][0] == '0' and
                    self.p[2][0] == '0') or \
                    (self.p[0][1] == '0' and
                    self.p[1][1] == '0' and
                    self.p[2][1] == '0') or \
                    (self.p[0][2] == '0' and
                    self.p[1][2] == '0' and
                    self.p[2][2] == '0'):
                self.end_info = 'Игра уже завершена'
                return 'Победил игрок 0'
            elif '-' not in self.p[0] and \
                    '-' not in self.p[1] and \
                    '-' not in self.p[2]:
                self.end_info = 'Игра уже завершена'
                return 'Ничья'
            else:
                return 'Продолжаем играть'
        elif self.end_info != 0:
            return self.end_info
        else:
            return 'Клетка ' + str(row) + ', ' + str(col) + ' уже занята'

board = TicTacToeBoard()
print(*board.get_field(), sep = '\n')
print(board.make_move(1, 1))
print(*board.get_field(), sep = '\n')
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep = '\n')
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2)) 
print(*board.get_field(), sep = '\n')
