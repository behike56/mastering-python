class CardData:
    def __init__(self, n, card):
        assert n % 2 == 1, "N must be an odd number."  # Nが奇数であることを確認
        self.n = n
        self.card = card
        self.opened = [[False] * n for _ in range(n)]
        # 中央のマスを開けない

    def mark_number(self, number):
        for i in range(self.n):
            for j in range(self.n):
                if self.card[i][j] == number:
                    self.opened[i][j] = True

    def count_bingo(self):
        bingo_count = 0

        # 行のチェック
        for i in range(self.n):
            if all(self.opened[i][j] for j in range(self.n)):
                bingo_count += 1

        # 列のチェック
        for j in range(self.n):
            if all(self.opened[i][j] for i in range(self.n)):
                bingo_count += 1

        # 斜めのチェック
        if all(self.opened[i][i] for i in range(self.n)):
            bingo_count += 1

        if all(self.opened[i][self.n - 1 - i] for i in range(self.n)):
            bingo_count += 1

        return bingo_count
