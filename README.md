# 座席管理アプリケーション
座席の状態（満席/空席）を確認できるWebアプリケーション。シチュエーションは食堂を想定している。あらかじめ、テーブル上にQRコードを張り付けておき、お盆がおかれQRコードが隠れると満席と判断する。


## 使用技術
- Ruby 3.4.1
- Rails 8.0.1
- Python 3.11.7


## 機能一覧

### create_qr.py
QRコードの生成をするプログラムで、作成したQRコードを印刷しテーブルに張り付けておく。

### reading_qr.py
PC内のWebカメラを利用してQRコードを読み取り、railsサーバーにPOSTリクエストを送信する。

### seat_management（railsプロジェクト）
以下２つの機能を有する
- 座席の状態を表示するページ。
- reading_qr.pyから受け取った情報をもとに座席状態を更新する。


## 今後の改善案
- ページのリアルタイム更新の追加。
- AWSへのデプロイ。
- QRコード読み取りにマイコンを使用する。
