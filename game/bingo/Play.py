class PlayData:
    def __init__(self, first_row: list[str]):
        self.card_size = int(first_row[0])
        self.lottery_times = int(first_row[1])
