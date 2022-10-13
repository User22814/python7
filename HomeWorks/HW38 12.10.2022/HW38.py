# прочитать изображение в память (подать путь к изображению - от пользователя) - чтение с диска
# выдать данных об изображении
# обработка изображения (подать все нужные параметры - от пользователя)
# выдать данных об итоговом изображении
# запись (сохранение результата) - перезапись/или сохранить как

import sys
import numpy as np
import time
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton, QSlider, \
    QComboBox
import cv2  # pip install opencv-python


class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя

        self.image_orig = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
        self.height_orig = np.size(self.image_orig, 0)
        self.width_orig = np.size(self.image_orig, 1)

        self.setWindowTitle(title)
        self.resize(width, height)

        self.image_data = None

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid(сетка)
        self.setLayout(self.layout)  # вкладываем QGridLayout -> MainWindow(QWidget)

        self.label_width = QLabel('Ширина: ')
        self.layout.addWidget(self.label_width, 1, 1)

        self.label_height = QLabel('Высота: ')
        self.layout.addWidget(self.label_height, 1, 2)

        self.line_edit_width = QLineEdit(f"{self.width_orig}")  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_width, 2, 1)  # вкладываем QLineEdit -> QGridLayout

        self.line_edit_height = QLineEdit(f"{self.height_orig}")  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_height, 2, 2)  # вкладываем QLineEdit -> QGridLayout

        self.check_box_wb = QCheckBox()  # экзампляр чек бокса
        self.check_box_wb.setChecked(False)
        self.layout.addWidget(self.check_box_wb, 3, 1)  # вкладываем QCheckBox -> QGridLayout

        self.label_check_wb = QLabel('сделать чёрно-белым: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check_wb, 3, 2)

        # self.slider_quality = QSlider(Qt.Horizontal)
        self.slider_quality = QSlider()
        self.slider_quality.setMinimum(1)
        self.slider_quality.setMaximum(100)
        self.slider_quality.setValue(95)

        self.layout.addWidget(self.slider_quality, 4, 5)

        self.label_slider_quality = QLabel('качество: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_slider_quality, 5, 5)

        self.label_1 = QLabel('')
        self.layout.addWidget(self.label_1, 6, 1)

        self.push_button_start = QPushButton('Start')  # экзампляр строки ввода текста
        self.push_button_start.clicked.connect(self.start)
        self.layout.addWidget(self.push_button_start, 7, 1)

        def delay(seconds: float):
            time.sleep(seconds)
            # тут код(поток исполнения)
            self.show()

        delay(0.5)
        # self.show()

    def start(self):
        print("start")

        white_black = bool(self.check_box_wb.isChecked())

        quality = int(self.slider_quality.value())
        width = int(self.line_edit_width.text())
        height = int(self.line_edit_height.text())

        image = self.image_orig

        # cv2.imshow('image', image)
        # cv2.waitKey(0)

        if white_black:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
            # image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]  # GRAY -> WHITE

        image = cv2.resize(image, (width, height))

        cv2.imwrite("image_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

        # cv2.imshow('image', image)
        # cv2.waitKey(0)


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'image analyse')  # создаём инстанс (экземпляр) класса
# пока класс не умрёт, эта часть кода не затронется
app.exec()  # очистка памяти

app1 = QApplication(sys.argv)
app1.exec()
