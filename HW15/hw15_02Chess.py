class ChessPiece:

    def __init__(self, color):
        self.color = color
        self.position_h = 1
        self.position_v = 1

    def check_position(self, hor: int, vert: int) -> bool:
        return 1 <= hor <= 8 and 1 <= vert <= 8

    def check_step(self, hor: int, vert: int) -> bool:
        raise NotImplementedError

    def change_color(self) -> str:
        return 'black' if self.color == 'white' else 'white'

    def get_move(self, hor: int, vert: int):
        return hor - self.position_h, vert - self.position_v


class Pawn(ChessPiece):

    def check_step(self, hor: int, vert: int) -> bool:
        delta_x, delta_y = self.get_move(hor, vert)
        if not self.color == 'white' and delta_x == 1 and hor == self.position_h or\
                self.color == 'black' and delta_x == -1 and hor == self.position_h:
            return False
        else:
            return self.check_position(hor, vert)


class Knight(ChessPiece):

    def check_step(self, hor: int, vert: int) -> bool:
        delta_x, delta_y = self.get_move(hor, vert)
        valid_moves = [(2, 1), (1, 2)]
        if not (delta_x, delta_y) in valid_moves:
            return False
        else:
            return self.check_position(hor, vert)


class Bishop(ChessPiece):

    def check_step(self, hor: int, vert: int) -> bool:
        delta_x, delta_y = self.get_move(hor, vert)
        if not abs(delta_x) == abs(delta_y):
            return False
        else:
            return self.check_position(hor, vert)


class Rook(ChessPiece):

    def check_step(self, hor: int, vert: int) -> bool:
        if not self.position_h == hor or self.position_v == vert:
            return False
        else:
            return self.check_position(hor, vert)


class Queen(ChessPiece):

    def check_step(self, hor: int, vert: int) -> bool:
        delta_x, delta_y = self.get_move(hor, vert)
        if not abs(delta_x) == abs(delta_y) or self.position_h == hor or self.position_v == vert:
            return False
        else:
            return self.check_position(hor, vert)


class King(ChessPiece):

    def check_step(self, hor: int, vert: int) -> bool:
        delta_x, delta_y = self.get_move(hor, vert)
        if not abs(delta_x) <= 1 and abs(delta_y) <= 1:
            return False
        else:
            return self.check_position(hor, vert)


def get_move_figures(lst_figures: list, hor: int, vert: int) -> list:
    return [figure for figure in lst_figures if figure.check_step(hor, vert)]


pawn = Pawn('white')
knight = Knight('white')
officer = Bishop('black')
rook = Rook('black')
queen = Queen('white')
king = King('black')
list_figures = [pawn, knight, officer, rook, queen, king]
print(pawn.change_color())
print(pawn.check_step(1, 1))
print(knight.check_step(3, 2))
print(officer.check_step(3, 3))
print(rook.check_step(1, 1))
print(queen.check_step(3, 6))
print(king.check_step(2, 2))
print(get_move_figures(list_figures, 6, 6))
