from mock import patch
import unittest
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

        class OutputCollector(object):
            def __init__(self, *args, **kwargs):
                self.output_collector = []

            def __call__(self, output):
                self.output_collector.append(output)

        self.output_collector = OutputCollector()

    def tearDown(self):
        pass

    @patch('game.Game.get_input', return_value='9')
    def test_quit_game(self, mock_input):
        with patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEquals(
            self.output_collector.output_collector,
            [],
        )

    def test_game_selection(self):
        self.assertEquals(
            self.game.game_inputs(),
            'Select Game\n'
            '0: Guess Number Game\n'
            '1: Tateti\n'
            '9: to quit\n'
        )

    def test_play_guess_number_game(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '0'
                if 'Give me a number from 0 to 100' in console_output:
                    return '50'

        with \
            patch('game.Game.get_input', side_effect=ControlInputValues()), \
            patch('game.Game.output', side_effect=self.output_collector), \
            patch('guess_number_game.guess_number_game.randint', return_value=50):
            self.game.play()

        self.assertEquals(
            self.output_collector.output_collector,
            ['[]', 'you win'],
        )

    def test_play_tateti(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '1'
                if '' in console_output:
                    game_turns = (
                        '0 0',
                        '1 0',
                        '0 1',
                        '1 1',
                        '0 2',
                    )
                    play = game_turns[self.play_count]
                    self.play_count += 1
                    return play

        with \
            patch('game.Game.get_input', side_effect=ControlInputValues()), \
            patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEquals(
            self.output_collector.output_collector,
            [
                '[[0, 0, 0], [0, 0, 0], [0, 0, 0]]',
                '',
                '[[\'X\', 0, 0], [0, 0, 0], [0, 0, 0]]',
                '',
                '[[\'X\', 0, 0], [\'O\', 0, 0], [0, 0, 0]]',
                '',
                '[[\'X\', \'X\', 0], [\'O\', 0, 0], [0, 0, 0]]',
                '',
                '[[\'X\', \'X\', 0], [\'O\', \'O\', 0], [0, 0, 0]]',
                'X wins',
            ],
        )


if __name__ == "__main__":
    unittest.main()