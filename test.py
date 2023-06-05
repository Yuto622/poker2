import unittest

import poker

class TestPokerMethods(unittest.TestCase):

    def test_which_win(self):
        result = poker.which_win(1, 2)
        self.assertEqual(result, "プレイヤー2の勝ちです")

if __name__ == '__main__':
    unittest.main()
