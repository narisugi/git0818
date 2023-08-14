import csv

# CSVファイルのパス
csv_file_path = ''

# CSVファイルを読み込んでデータを表示する
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

from flask import Flask, render_template
import random
app = Flask(__name__)
@ app.route('/')
def gacha():
    items = ["アイテム1", "アイテム2", "アイテム3"]  # ガチャアイテムのリスト
    result = random.choice(items)  # ランダムにアイテムを選択
    return render_template('index.html', result=result)
if __name__ == '__main__':
    app.run()