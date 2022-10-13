import random
import sys
import time
import aiohttp
import asyncio
import json
import psycopg2

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget
)

index = 0


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.label_main = QLabel("Данные от сервера: ")
        layout.addWidget(self.label_main, 1, 1)

        self.label_answer = QLabel("Приложение запущено")
        layout.addWidget(self.label_answer, 1, 2)

        self.label_id = QLabel("id: int")
        layout.addWidget(self.label_id, 2, 1)
        self.lineedit_id = QLineEdit("")
        layout.addWidget(self.lineedit_id, 3, 1)

        self.label_title = QLabel("title: str")
        layout.addWidget(self.label_title, 2, 2)
        self.lineedit_title = QLineEdit("")
        layout.addWidget(self.lineedit_title, 3, 2)

        self.label_author = QLabel("author: str")
        layout.addWidget(self.label_author, 2, 3)
        self.lineedit_author = QLineEdit("")
        layout.addWidget(self.lineedit_author, 3, 3)

        self.label_price = QLabel("price: float")
        layout.addWidget(self.label_price, 2, 4)
        self.lineedit_price = QLineEdit("")
        layout.addWidget(self.lineedit_price, 3, 4)

        self.label_page_counts = QLabel("page counts: int")
        layout.addWidget(self.label_page_counts, 2, 5)
        self.lineedit_page_counts = QLineEdit("")
        layout.addWidget(self.lineedit_page_counts, 3, 5)

        pushbutton1 = QPushButton("Go!")
        layout.addWidget(pushbutton1, 4, 2)
        pushbutton1.clicked.connect(self.create_data)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle("CRUD PYQT6")
        self.setGeometry(500, 250, 500, 250)
        self.show()

    def create_data(self):
        global index
        # CREATE (INSERT)
        conn = psycopg2.connect("dbname=db_new_hw35 user=postgres password=qwerty228")
        cur = conn.cursor()

        id = int(self.lineedit_id.text())
        title = str(self.lineedit_title.text())
        author = str(self.lineedit_author.text())
        price = float(self.lineedit_price.text())
        page_counts = int(self.lineedit_page_counts.text())

        query_string = f"""
        INSERT INTO public.books (id, title, author, price, page_counts)
        VALUES ({id}, '{title}', '{author}', {price}, {page_counts})
        """

        cur.execute(query_string)
        conn.commit()  # применение данных после изменений

        index += 1

        self.label_answer.setText(f"Сообщение №{index} записано на сервер!")

        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()
