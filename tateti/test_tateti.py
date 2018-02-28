import unittest
from tateti import Tateti


class TestTateti(unittest.TestCase):

    def setUp(self):
        self.tateti = Tateti()

    def test_initial_playing(self):
        self.assertTrue(self.tateti.playing)

    def test_piezas_play_0(self):
        self.tateti.play(0, 1)
        self.assertEquals(
            self.tateti.board,
            "[[0, 'X', 0], [0, 0, 0], [0, 0, 0]]",
        )

    def test_piezas_play_1(self):
        self.tateti.play(2, 1)
        self.assertEquals(
            self.tateti.board,
            "[[0, 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )
        self.tateti.play(0, 0)
        self.assertEquals(
            self.tateti.board,
            "[['O', 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )

    def test_play_negative_exception(self):
        with self.assertRaises(Exception) as e:
            self.tateti.play(-1, 1)
            self.assertEqual(e.exception.message, "Movement not allowed.",)

    def test_play_negative_exception_2(self):
        with self.assertRaises(Exception) as e:
            self.tateti.play(-1, -1)
            self.assertEqual(e.exception.message, "Movement not allowed.",)

    def test_play_negative_exception_3(self):
        with self.assertRaises(Exception) as e:
            self.tateti.play(1, -1)
            self.assertEqual(e.exception.message, "Movement not allowed.",)

    def test_play_caracter_invalid(self):
        with self.assertRaises(Exception) as e:
            self.tateti.play('a', 'b')
            self.assertEqual(e.exception.message, "Movement not allowed.",)

    def test_next_O(self):
        self.assertEqual(self.tateti.next(), "Plays O")

    def test_next_X(self):
        self.tateti.play(1, 1)
        self.assertEqual(self.tateti.next(), "Plays X")

    def test_repeat_movement(self):
        self.tateti.play(2, 1)
        self.assertEquals(
            self.tateti.board,
            "[[0, 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )
        with self.assertRaises(Exception) as e:
            self.tateti.play(2, 1)
            self.assertEqual(e.exception.message, "Movement not allowed.",)


if __name__ == "__main__":
    unittest.main()
