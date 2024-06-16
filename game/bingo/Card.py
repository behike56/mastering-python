import Play as ply


class CardData:
    def __init__(self, size, card):
        assert size % 2 == 1, "N must be an odd number."  # Nが奇数であることを確認
        self.size: int = size
        self.card: list[list[str]] = card
        self.opened: list[list[bool]] = [[False] * size for _ in range(size)]
        # 中央のマスを開けない

    def _create_bingo_card_data(
            self,
            play_data: ply.PlayData) -> list[list[str]]:

        # ビンゴカードの読み込み
        bingo_card_data: list[list[str]] = []

        for i in range(self.size):
            row = list(map(int, self.card[index:index + self.size]))
            bingo_card_data.append(row)
            index += self.size

        return bingo_card_data

    def mark_number(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if self.card[i][j] == number:
                    self.opened[i][j] = True

    def count_bingo(self):
        bingo_count = 0

        # 行のチェック
        for i in range(self.size):
            if all(self.opened[i][j] for j in range(self.size)):
                bingo_count += 1

        # 列のチェック
        for j in range(self.size):
            if all(self.opened[i][j] for i in range(self.size)):
                bingo_count += 1

        # 斜めのチェック
        if all(self.opened[i][i] for i in range(self.size)):
            bingo_count += 1

        if all(self.opened[i][self.size - 1 - i] for i in range(self.size)):
            bingo_count += 1

        return bingo_count

    def display(bingo_card: list[list[str]]) -> int:

        print("Bingo Card:")

        for row in bingo_card:
            print(" | ".join(row))
            print("-" * (len(row) * 4 - 1))

        return 0
