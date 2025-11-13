# python-csv-tool

CSV ファイルを読み込み、`price` と `quantity` から `total` 列を計算して追加するサンプルスクリプトです。

## 使い方

1. `python-csv-tool` ディレクトリ直下に `input.csv` を配置します。
   例:

   ```csv
   item,price,quantity
   apple,120,3
   orange,80,2

以下コマンドを実行します。

python main.py


output.csv が生成され、total 列が追加されます。

item,price,quantity,total
apple,120,3,360.00
orange,80,2,160.00

想定シーン

売上集計など、業務でよくある CSV 加工処理のイメージ

Python を用いた簡単なバッチ処理・自動化スクリプトのサンプル


---
