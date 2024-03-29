## 説明

fixed_size は、複数の画像ファイルを均一の大きさのPDFに変換するためのツールです。主にテキストやプリントをスキャンしてPDFを作成し、書き込んで学習する場合や、書類をスキャンしてPDFを先生に提出する場合に利用します。

## 開発動機

スキャンしたPDFでは、ページごとのサイズが少し異なる場合があり、iPadなどで書き込んで作業する際や、先生に提出する際にどうしても見にくくなってしまいます。そこでこのツールを使えば均等の大きさのPDFが作成することができるため見やすいPDFになります。

## 特徴

- 複数の画像ファイルを一括してPDFに変換できる点。
- 均一の大きさのPDFを作成できる点。
- A4縦向きとA4横向きの出力を選択できる点。

## パッケージのインストール

このプログラムはPySide6とreportlabを使用して開発されています。
以下のようにコマンドラインに入力することで必要なパッケージをダウンロードすることができます。

pip install -r requirements.txt

## 使用方法

1. fixed_size を実行します。
2. "画像フォルダを選択" ボタンをクリックして、変換したい画像が含まれるフォルダを選択します。
3. "A4縦向きに出力" または "A4横向きに出力" ボタンをクリックして、PDFに変換します。
4. 変換が完了すると、作成されたPDFファイルがプレビューされます。
(テストプレイ用に"example"フォルダ(jpg画像複数枚)を用意しています。)

## 注意事項

- このツールは Python 3.x 環境で動作します。
- 変換されたPDFファイルは、同じディレクトリに "output.pdf" という名前で保存されます。
- サポートされている画像形式は、".png"、".jpg"、".jpeg"、".gif" です。

## ライセンス

このアプリケーションは GNU Lesser General Public License v3.0 のもとで公開されています。詳細は `LICENSE.txt` ファイルを参照してください。

このアプリケーションは PySide6 を利用しています。PySide6 は LGPL v3 ライセンスの下で公開されています。詳細は [こちら](https://www.qt.io/licensing/) を参照してください。