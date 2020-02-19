import io
import sys
from pprint import pprint

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QAbstractButton, QInputDialog
from Widget import Ui_Dialog


class MyMap(QDialog, Ui_Dialog):
    def __init__(self):
        while True:
            coor, boo = '37.575636,54.171069', True  # QInputDialog.getText(None, "Введите координаты", "Формат 37.575636,54.171069")
            if boo:
                try:
                    coor = list(map(float, coor.split(',')))
                    if len(coor) != 2 or not (-180 <= coor[0] <= 180) or not (-85 <= coor[1] <= 85):
                        raise IndexError
                    map_params["ll"] = ','.join(list(map(str, coor)))
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

        self.search_bool = False
        self.k = 1

        self.update_im()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.change_mashtab('Up')

        if event.key() == Qt.Key_PageDown:
            self.change_mashtab('Down')

        if event.key() == Qt.Key_Up:
            self.change_centre_coords('Up')

        if event.key() == Qt.Key_Down:
            self.change_centre_coords('Down')

        if event.key() == Qt.Key_Left:
            self.change_centre_coords('Left')

        if event.key() == Qt.Key_Right:
            self.change_centre_coords('Right')

    def change_mashtab(self, s):
        coor = list(map(float, map_params['spn'].split(',')))
        if s == 'Up':
            coor[0] *= 2
        else:
            coor[1] /= 2
        map_params['spn'] = ','.join(list(map(str, coor)))
        self.update_im()

    def change_centre_coords(self, s):
        coor = list(map(float, map_params['ll'].split(',')))
        if s == "Up":
            coor[1] += float(map_params['spn'].split(',')[1]) * 2
        elif s == "Down":
            coor[1] -= float(map_params['spn'].split(',')[1]) * 2
        elif s == "Left":
            coor[0] -= float(map_params['spn'].split(',')[0]) * 2
        elif s == "Right":
            coor[0] += float(map_params['spn'].split(',')[0]) * 2
        if -180 <= coor[0] <= 180 and -85 <= coor[1] <= 85:
            map_params['ll'] = ','.join(list(map(str, coor)))
            self.update_im()

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
        geocoder_params['geocode'] = self.lineEdit.text()
        response = requests.get(geocoder_api_server, params=geocoder_params)
        if not response:
            self.lineEdit.setText('Адресс не действителен')
        else:
            try:
                json = response.json()
                geo_object = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                pos = ','.join(geo_object['Point']['pos'].split())
                envelope = json["response"]["GeoObjectCollection"][
                    "featureMember"][0]["GeoObject"]['boundedBy']['Envelope']
                low = envelope['lowerCorner'].split()
                upp = envelope['upperCorner'].split()

                print(low, upp)
            except Exception:
                self.lineEdit.setText('Адресс не действителен')
                return
            map_params['pt'] = pos + ',round'
            map_params['ll'] = pos
            map_params['spn'] = f"{abs(float(upp[0]) - float(low[0])) / 2},{abs(float(upp[1]) - float(low[1])) / 2}"
            self.search_bool = True
            self.update_im()

    def discharge(self):
        if self.search_bool:
            map_params['pt'] = None
        self.search_bool = False
        self.lineEdit.setText('')
        self.update_im()

    def update_im(self):
        response = requests.get(map_api_server, params=map_params)
        if not response:
            print(response.url)
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        p = QPixmap()
        buf = (io.BytesIO(response.content)).getbuffer()
        p.loadFromData(buf)
        self.label.setPixmap(p)


geocoder_params = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': None,
    'format': 'json'
}
map_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "l": 'map',
    "ll": None,
    'size': '450,450',
    'spn': None,
    'pt': None}

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
map_api_server = "http://static-maps.yandex.ru/1.x/"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maps = MyMap()
    maps.show()
    sys.exit(app.exec_())
