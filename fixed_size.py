import os
from PySide6.QtWidgets import QWidget, QPushButton, QFileDialog, QMessageBox
from PySide6.QtGui import QDesktopServices, QIcon
from PySide6.QtCore import QUrl
from reportlab.lib.pagesizes import A4, landscape, portrait
from reportlab.pdfgen import canvas
from PIL import Image


class FileDialogApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Converter')
        self.setGeometry(100, 100, 300, 250)

        # ファイル選択ダイアログを表示するボタン
        self.btn_select_folder = QPushButton('画像フォルダを選択', self)
        self.btn_select_folder.setGeometry(50, 50, 200, 50)
        self.btn_select_folder.clicked.connect(self.showImgFolderDialog)

        # A4縦向きに出力ボタン
        self.btn_output_portrait = QPushButton('A4縦向きに出力', self)
        self.btn_output_portrait.setGeometry(50, 110, 200, 50)
        self.btn_output_portrait.clicked.connect(self.outputPortrait)

        # A4横向きに出力ボタン
        self.btn_output_landscape = QPushButton('A4横向きに出力', self)
        self.btn_output_landscape.setGeometry(50, 170, 200, 50)
        self.btn_output_landscape.clicked.connect(self.outputLandscape)

    def showImgFolderDialog(self):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)  # フォルダ選択モードに設定

        if folder_dialog.exec():
            self.img_folder = folder_dialog.selectedFiles()[0]  # 選択されたフォルダのパスを取得
            print("選択された画像フォルダのパス:", self.img_folder)

    def outputPortrait(self):
        if not hasattr(self, 'img_folder'):
            QMessageBox.warning(self, '警告', '画像フォルダを選択してください')
            return

        self.convertImagesToPdf(portrait(A4))

    def outputLandscape(self):
        if not hasattr(self, 'img_folder'):
            QMessageBox.warning(self, '警告', '画像フォルダを選択してください')
            return

        self.convertImagesToPdf(landscape(A4))

    def convertImagesToPdf(self, pagesize):
        output_pdf = self.getUniqueFilename('output.pdf')
        c = canvas.Canvas(output_pdf, pagesize=pagesize)

        for filename in os.listdir(self.img_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                img_path = os.path.join(self.img_folder, filename)
                img = Image.open(img_path)

                # 画像形式を確認して必要に応じて変換
                if img.format != 'RGB':
                    img = img.convert('RGB')

                img_width, img_height = img.size
                page_width, page_height = pagesize

                # 画像を収めるためのスケーリング
                scale = min(page_width / img_width, page_height / img_height)

                # 画像をページの中央に配置
                x = (page_width - img_width * scale) / 2
                y = (page_height - img_height * scale) / 2

                # 画像をキャンバスに描画
                c.drawImage(img_path, x, y, img_width * scale, img_height * scale)
                c.showPage()

        c.save()
        QMessageBox.information(self, '情報', 'PDFファイルが作成されました')

        # PDFファイルをプレビュー表示
        QDesktopServices.openUrl(QUrl.fromLocalFile(output_pdf))

    def getUniqueFilename(self, filename):
        if not os.path.exists(filename):
            return filename

        name, ext = os.path.splitext(filename)
        counter = 1
        while True:
            new_filename = f"{name}({counter}){ext}"
            if not os.path.exists(new_filename):
                return new_filename
            counter += 1