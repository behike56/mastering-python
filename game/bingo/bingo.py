import BingoCard as bc

# def


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    N = int(data[index])
    index += 1
    K = int(data[index])
    index += 1

    # ビンゴカードの読み込み
    bingo_card_data = []
    for i in range(N):
        row = list(map(int, data[index:index + N]))
        bingo_card_data.append(row)
        index += N

    # 抽選された数字の読み込み
    drawn_numbers = list(map(int, data[index:index + K]))

    # ビンゴカードを作成
    bingo_card = bc.BingoCard(N, bingo_card_data)

    # 抽選された数字に基づいてビンゴカードの状態を更新
    for number in drawn_numbers:
        bingo_card.mark_number(number)

    # ビンゴの数を出力
    print(bingo_card.count_bingo())


if __name__ == "__main__":
    main()
