import unittest
from ReversiGame import ReversiGame


class TestReversi(unittest.TestCase):

    def setUp(self):
        self.game = ReversiGame()

    def test_initial_status(self):
        self.assertTrue(self.game.playing)
        self.assertEquals(self.game.tablero[3][3], 'B')
        self.assertEquals(self.game.tablero[3][4], 'W')
        self.assertEquals(self.game.tablero[4][3], 'W')
        self.assertEquals(self.game.tablero[4][4], 'B')

    def test_initial_next_turn_whites(self):
        self.assertEquals(
            self.game.next_turn(),
            'Turn of the whiteones',
        )

    def test_wrong_movement_empty(self):
        self.assertEquals(self.game.play(1, 1), 'No hay posibilidades')

    @unittest.SkipTest
    def test_no_posibilities(self):
        self.assertEquals(self.game.play(7, 7), 'No hay posibilidades')

    def test_wrong_movement_occupied(self):
        self.assertEquals(self.game.play(3, 4), 'Movimiento no permitido')

    def test_get_directions(self):
        result = [
            [(3, 4, 'W')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(3, 5))

    def test_get_directions_black(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'W', 'B', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.game.playingBlack = False
        result = [
            [(3, 5, 'B')], [(3, 4, 'B')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(2, 5))
        result = [
            [(3, 3, 'B')], [(3, 4, 'B')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(2, 3))

    def test_find_possibilities_limits_min(self):
        self.assertEquals([], self.game.find_possibility_pieces(0, 0))

    def test_find_possibilities_limits_max(self):
        self.assertEquals([], self.game.find_possibility_pieces(7, 7))

    def test_get_all_directions_white(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', ' ', 'W', 'B', ' ', 'B', 'W', ' '],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.game.playingBlack = False
        result = [
            [(3, 3, 'B')], [(3, 5, 'B')],
            [(2, 4, 'B')], [(4, 4, 'B')],
            [(2, 5, 'B')], [(2, 3, 'B')],
            [(4, 3, 'B')], [(4, 5, 'B')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(3, 4))

    def test_get_all_directions_black(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        result = [
            [(3, 3, 'W')], [(3, 5, 'W')],
            [(2, 4, 'W')], [(4, 4, 'W')],
            [(2, 5, 'W')], [(2, 3, 'W')],
            [(4, 3, 'W')], [(4, 5, 'W')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(3, 4))

    def test_reverse_posibles(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        posibles = self.game.find_possibility_pieces(3, 4)

        self.game.reverse_posibles(posibles)
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', ' ', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.assertEquals(result, self.game.tablero)

    def test_play_valid(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.game.play(3, 4)
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.assertEquals(result, self.game.tablero)
        self.assertEquals(
            self.game.next_turn(),
            'Turn of the whiteones',
        )

    def test_graphic_board(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        result = (
            '  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '0 |   |   |   |   |   |   |   |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '1 |   |   | B | B | B | B | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '2 |   |   | B | W | W | W | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '3 |   |   | B | W |   | W | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '4 |   |   | B | W | W | W | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '5 |   |   | B | B | B | B | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '6 |   |   |   |   |   |   |   |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '7 |   |   |   |   |   |   |   |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
        )

        self.assertEquals(result, self.game.board)


if __name__ == "__main__":
    unittest.main()
