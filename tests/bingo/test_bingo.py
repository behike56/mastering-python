import unittest
from game.bingo.bingo import BingoCard


class TestBingoCard(unittest.TestCase):
    def setUp(self):
        self.card_data = [
            [13, 3, 9],
            [8, 0, 2],
            [16, 17, 15]
        ]
        self.bingo_card = BingoCard(3, self.card_data)

    def test_initial_state(self):
        # 初期状態ではどのマスも開いていない
        self.assertFalse(any(any(row) for row in self.bingo_card.opened))
        # 中央のマスが開いていないことを確認する
        self.assertFalse(self.bingo_card.opened[1][1])

    def test_mark_number(self):
        self.bingo_card.mark_number(3)
        self.assertTrue(self.bingo_card.opened[0][1])
        self.assertFalse(self.bingo_card.opened[0][0])

    def test_count_bingo_no_bingo(self):
        self.bingo_card.mark_number(3)
        self.bingo_card.mark_number(9)
        self.assertEqual(self.bingo_card.count_bingo(), 0)

    def test_count_bingo_with_bingo(self):
        numbers = [13, 3, 9, 8, 2, 16, 17, 15]
        for number in numbers:
            self.bingo_card.mark_number(number)
        self.assertEqual(self.bingo_card.count_bingo(), 3)


if __name__ == '__main__':
    unittest.main()
