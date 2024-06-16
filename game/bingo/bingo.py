import Card as crd
import Play as ply
import Lottery as lty

from bingo_file_reader import read_bingo_data

import sys


def main() -> int:

    # 標準入力からファイルパスを取得する
    file_path = _let_input_filepath()

    # ファイルからビンゴゲームのデータを取得する
    bingo_data: list[list[str]] = read_bingo_data(file_path)

    # プレイデータを作成
    play_data = ply.PlayData(bingo_data[0])

    # カードデータを作成
    card_data = crd.CardData(play_data.card_size, bingo_data)

    # 抽選データを作成
    lottery_data = lty.LotteryData(bingo_data[-1])

    # ビンゴカードを表示する
    crd.display(bingo_data)

    # 抽選された数字の読み込み
    # drawn_numbers = list(
    #     map(int, bingo_data[index:index + play_data.lottery_times]))

    # 抽選された数字に基づいてビンゴカードの状態を更新
    for number in lottery_data.numbers:
        card_data.mark_number(int(number))

    # ビンゴの数を出力
    print(card_data.count_bingo())

    return 0


def _let_input_filepath() -> str:

    input = sys.stdin.read
    file_path = input().split()

    return file_path



if __name__ == "__main__":
    main()
