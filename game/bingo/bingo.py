import Card as crd
import Play as ply
import Lottery as lty

from bingo_file_reader import read_bingo_data

import sys


def _let_input_filepath() -> str:

    input = sys.stdin.read
    file_path = input().split()

    return file_path


def _display_bingo_card(bingo_card: list[list[str]]) -> int:

    print("Bingo Card:")

    for row in bingo_card:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

    return 0


def _create_bingo_card_data(
        play_data: ply.PlayData,
        card_data: crd.CardData) -> list:

    # ビンゴカードの読み込み
    bingo_card_data = []
    for i in range(card_size):
        row = list(map(int, bingo_data[index:index + card_size]))
        bingo_card_data.append(row)
        index += card_size


def main() -> int:

    # 標準入力からファイルパスを取得する
    file_path = _let_input_filepath()

    # ファイルからビンゴゲームのデータを取得する
    bingo_data = read_bingo_data(file_path)

    # プレイデータを作成
    play_data = ply.PlayData(bingo_data[0])

    # カードデータを作成
    card_data = bc.CardData(play_data.card_size, bingo_card_data)

    # 抽選データを作成
    lottery_data = lty.LotteryData()

    # ビンゴカードを表示する
    _display_bingo_card(bingo_data)

    # 抽選された数字の読み込み
    drawn_numbers = list(map(int, bingo_data[index:index + lottery_times]))

    # 抽選された数字に基づいてビンゴカードの状態を更新
    for number in drawn_numbers:
        bingo_card.mark_number(number)

    # ビンゴの数を出力
    print(bingo_card.count_bingo())


if __name__ == "__main__":
    main()
