from typing import Tuple, List
import random
from copy import copy
from itertools import cycle


class StepError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Ui:

    @staticmethod
    def start_game():
        print("Классическая игра крестики нолики")

    @staticmethod
    def end_game():
        pass

    @staticmethod
    def hello_user(user: 'User'):
        print(f'{user} с символом {user.symbol} зарегистрирован')

    @staticmethod
    def ask_user():
        while True:
            name = input('Ваше имя в игре? \n>>>')
            if not name:
                print('необходимо ввести имя')
                continue
            return name

    @staticmethod
    def game_mode():
        ask_str = "Выберите режим игры:\n" \
                  "1 - против компьютера\n 2 - против Игрока"
        while True:
            try:
                answer = int(input(ask_str + '\n>>>'))
                if not 2 >= answer > 0:
                    raise ValueError
                return answer
            except ValueError:
                print("Неверный ввод, вводите только указанные числа")

    @staticmethod
    def step(user):
        print(f'{"#" * 5} Ход {user} {"#" * 5}')
        while True:
            coords_str = input('Введите координаты хода через пробел')
            try:
                coords = tuple(int(itm) - 1 for itm in coords_str.split(' '))
                if not coords or len(coords) != 2 or not all(map(lambda x: x in range(3), coords)):
                    raise ValueError
            except ValueError:
                print('Ошибка ввода')
                continue
            return coords

    @staticmethod
    def print_board(bord):
        print(bord)

    @staticmethod
    def user_win(user, statistic):
        print(f'Победил {user} на {statistic} ходу')

    @staticmethod
    def standoff():
        print("Игра завершилась в ничью")


class Game:

    def __init__(self):
        self.__board = Board()
        self.__users: List[User] = []
        self.game_step = 0

    def start_game(self):
        Ui.start_game()
        self.create_users()
        self.__game_cycle()

    def __game_cycle(self):
        for user in cycle(self.__users):
            if self.game_step > 9:
                Ui.standoff()
                break
            self.game_step += 1
            Ui.print_board(self.__board)
            user.step(self.__board)
            game_result = self.__board.check()
            if game_result[0]:
                Ui.user_win(game_result[1], self.game_step)
                break

    def create_users(self):
        game_mode = Ui.game_mode()
        if game_mode == 1:
            users = (User.create_user('X'), User.create_bot('O'))
        else:
            users = (User.create_user('X'), User.create_user('O'))
        self.__users.extend(users)


class Board:

    def __init__(self):
        self.__board = [[0, 0, 0] for _ in range(3)]
        self.__variants = [(n, m) for n in range(3) for m in range(3)]

    def set_step(self, user: 'User', coord: Tuple[int]):
        self[coord[0]][coord[1]] = user
        self.__variants.remove(coord)

    @property
    def free_coord(self):
        return copy(self.__variants)

    def check(self):
        for lines in zip(self, zip(*self)):
            for line in lines:
                if self.check_line(line):
                    return True, line[0]
        if self.check_line([self[n][n] for n in range(0, 3)]):
            return True, self[0][0]
        elif self.check_line(
                [self[n][m] for n, m in zip(range(0, 3), range(2, -1, -1))]):
            return True, self[0][-1]
        return False, None

    def check_line(self, line):
        return isinstance(line[0], User) and line.count(line[0]) == len(line)

    def set_step(self, user, step):
        if step not in self.free_coord:
            raise StepError('Ячейка занята')
        self.__variants.remove(step)
        self.__board[step[0]][step[1]] = user

    def __getitem__(self, item):
        return self.__board[item]

    def __str__(self):
        result = '#\n'.join(
            [f"{line_idx}#" + '|'.join([str(itm.symbol) if isinstance(itm, User) else '_' for itm in line])
             for line_idx, line in enumerate(self.__board, 1)]) + "#"
        return f"{'##1#2#3#'}\n" + result + f"\n{'##1#2#3#'}\n"


class User:
    __bot_names = (
        'Wally',
        'R2D2',
        'C3PO',
        'Fedor',
        'HAL 9000',
    )

    def __init__(self, name, symbol, is_bot=True):
        self.name = name
        self.symbol = symbol
        self.is_bot = is_bot

    def __str__(self):
        return f'{"Бот" if self.is_bot else "Игрок"} {self.name}'

    @classmethod
    def create_user(cls, symbol: str):
        user = cls(Ui.ask_user(), symbol, False)
        Ui.hello_user(user)
        return user

    @classmethod
    def create_bot(cls, symbol: str):
        user = cls(random.choice(cls.__bot_names), symbol)
        Ui.hello_user(user)
        return user

    def step(self, bord):
        if self.is_bot:
            step = self.__auto_step(bord)
            bord.set_step(self, step)
        else:
            while True:
                try:
                    step = Ui.step(self)
                    bord.set_step(self, step)
                except StepError:
                    continue
                return 1

    @staticmethod
    def __auto_step(bord: Board):
        return random.choice(bord.free_coord)


if __name__ == '__main__':
    game = Game()
    game.start_game()
