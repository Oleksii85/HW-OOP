class ChessFigure:

    def __init__(self, color, hor, vert):
        self.color = color
        self.hor = hor
        self.vert = vert
        self.position_h = 1
        self.position_v = 1

    @staticmethod
    def check_position(hor: int, vert: int) -> bool:
        return True if 1 <= hor <= 8 and 1 <= vert <= 8 else print('outside the field')

    def check_step(self, hor: int, vert: int) -> bool:
        raise NotImplementedError

    def change_color(self) -> str:
        return 'black' if self.color == 'white' else 'white'

    def get_move(self, hor: int, vert: int):
        return self.position_h - hor, self.position_v - vert


class Pawn(ChessFigure):

    def check_step(self, hor: int, vert: int) -> bool:
        if self.check_position(hor, vert):
            self.get_move(hor, vert)
            if self.color == 'white' and vert - self.position_v == 1 and hor == self.position_h:
                return True
            else:
                if self.color == 'black' and vert - self.position_v == -1 and hor == self.position_h:
                    return True
                else:
                    return False


class Knight(ChessFigure):

    def check_step(self, hor: int, vert: int) -> bool:
        if self.check_position(hor, vert):
            self.get_move(hor, vert)
            if (self.position_h - 1 == hor or self.position_h + 1 == hor) and\
                    (self.position_v - 2 == vert or self.position_v + 2 == vert):
                return True
            elif (self.position_h - 2 == hor or self.position_h + 2 == hor) and\
                    (self.position_v - 1 == vert or self.position_v + 1 == vert):
                return True
            else:
                return False


class Officer(ChessFigure):

    def check_step(self, hor: int, vert: int) -> bool:
        if self.check_position(hor, vert):
            self.get_move(hor, vert)
            if abs(self.position_v - hor) == abs(self.position_h - vert):
                return True
            else:
                return False


class Rook(ChessFigure):

    def check_step(self, hor: int, vert: int) -> bool:
        if self.check_position(hor, vert):
            self.get_move(hor, vert)
            return True if self.position_h == hor or self.position_v == vert else False


class Queen(ChessFigure):

    def check_step(self, hor: int, vert: int) -> bool:
        if self.check_position(hor, vert):
            self.get_move(hor, vert)
            return abs(self.position_v - hor) == abs(self.position_h - vert) or\
                self.position_h == hor or self.position_v == vert


class King(ChessFigure):

    def check_step(self, hor: int, vert: int) -> bool:
        if self.check_position(hor, vert):
            self.get_move(hor, vert)
            return abs(self.position_h - hor) <= 1 and abs(self.position_v - vert) <= 1


def get_move_figures(lst_figures: list, hor: int, vert: int) -> list:
    return [figure for figure in lst_figures if figure.check_step(hor, vert)]


pawn = Pawn('white', 2, 2)
knight = Knight('white', 3, 3)
officer = Officer('black', 2, 5)
rook = Rook('black', 1, 4)
queen = Queen('white', 5, 5)
king = King('black', 2, 7)
list_figures = [pawn, knight, officer, rook, queen, king]
print(pawn.change_color())
print(pawn.check_step(1, 1))
print(knight.check_step(3, 2))
print(officer.check_step(3, 3))
print(rook.check_step(1, 1))
print(queen.check_step(3, 6))
print(king.check_step(2, 2))
print(get_move_figures(list_figures, 6, 6))
