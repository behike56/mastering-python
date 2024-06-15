import BingoCard as bc
import csv
import sys


def read_bingo_card(file_path) -> list[list[str]]:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        bingo_card = [row for row in reader]
    return bingo_card


def display_bingo_card(bingo_card):
    print("Bingo Card:")
    for row in bingo_card:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))


def main():

    input = sys.stdin.read
    file_path = input().split()

    bingo_data = read_bingo_card(file_path)

    display_bingo_card(bingo_data)

    index = 0
    N = int(bingo_data[index])
    index += 1
    K = int(bingo_data[index])
    index += 1

    # ビンゴカードの読み込み
    bingo_card_data = []
    for i in range(N):
        row = list(map(int, bingo_data[index:index + N]))
        bingo_card_data.append(row)
        index += N

    # 抽選された数字の読み込み
    drawn_numbers = list(map(int, bingo_data[index:index + K]))

    # ビンゴカードを作成
    bingo_card = bc.BingoCard(N, bingo_card_data)

    # 抽選された数字に基づいてビンゴカードの状態を更新
    for number in drawn_numbers:
        bingo_card.mark_number(number)

    # ビンゴの数を出力
    print(bingo_card.count_bingo())


if __name__ == "__main__":
    main()
