import csv


def read_bingo_data(file_path: str) -> list[list[str]]:
    """ファイルからビンゴデータを取得する。
    ビンゴデータは３種類ある：
      プレイデータ
      カードデータ
      抽選データ

    Args:
        file_path (str): ファイルパス

    Returns:
        list[list[str]]: ビンゴデータ、1行がlist[str]
    """

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        bingo_data = [row for row in reader]

    return bingo_data
