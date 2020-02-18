import io
import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QAbstractButton, QInputDialog
from Widget import Ui_Dialog


class MyMap(QDialog, Ui_Dialog):
    def __init__(self):
        while True:
            coor, boo = QInputDialog.getText(None, "Введите координаты", "Формат 37.575636,54.171069")
            if boo:
                try:
                    list(map(float, coor.split(',')))
                    map_params["ll"] = coor
                    break
                except Exception:
                    pass
            else:
                sys.exit()
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.discharge)
        self.buttonGroup.buttonClicked.connect(self.change_map_sloi)
        self.update_im()

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


map_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "l": 'map',
    "ll": None,
    'size': '650,450',
    'z': 15}

map_api_server = "http://static-maps.yandex.ru/1.x/"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maps = MyMap()
    maps.show()
    sys.exit(app.exec_())
