import io
import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QAbstractButton
from Widget import Ui_Dialog


class MyMap(QDialog, Ui_Dialog):
    def __init__(self, bts):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.discharge)

        p = QPixmap()
        buf = bts.getbuffer()
        p.loadFromData(buf)
        self.label.setPixmap(p)

        self.buttonGroup.buttonClicked.connect(self.change_map_sloi)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.change_mashtab('Up')

        if event.key() == Qt.Key_PageDown:
            self.change_mashtab('Down')

        if event.key() == Qt.Key_Up:
            self.change_centre_coords()

        if event.key() == Qt.Key_Down:
            self.change_centre_coords()

        if event.key() == Qt.Key_Left:
            self.change_centre_coords()

        if event.key() == Qt.Key_Right:
            self.change_centre_coords()

    def change_mashtab(self, s):
        if s == 'Up':
            map_params['z'] += 1 if map_params['z'] != 19 else 0
        else:
            map_params['z'] -= 1 if map_params['z'] != 0 else 0
        self.update_im()

    def change_centre_coords(self):
        pass

    def change_map_sloi(self):
        text = self.buttonGroup.checkedButton().text()
        if text == 'Гибрид':
            map_params['l'] = 'sat,skl'
        elif text == 'Схема':
            map_params['l'] = 'map'
        elif text == 'Спутник':
            map_params['l'] = 'sat'
        self.update_im()

    def search(self):
        values = self.lineEdit.text()

    def discharge(self):
        pass

    def update_im(self):
        response = requests.get(map_api_server, params=map_params)
        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(2)
        p = QPixmap()
        buf = (io.BytesIO(response.content)).getbuffer()
        p.loadFromData(buf)
        self.label.setPixmap(p)


address_ll = list(map(float, input('формат вводных данных: 37.575636,54.171069\n').split(',')))
size = '650,450'
map_params = {
    "l": 'map',
    "ll": ','.join(map(str, address_ll)),
    'size': size,
    'z': 15}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
if not response:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maps = MyMap(io.BytesIO(response.content))
    maps.show()
    sys.exit(app.exec_())
