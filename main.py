import io
import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QAbstractButton, QInputDialog
from Widget import Ui_Dialog


class MyMap(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_yes.setChecked(True)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.discharge)
        self.buttonGroup.buttonClicked.connect(self.change_map_sloi)
        self.buttonGroup_2.buttonClicked.connect(self.change_edit_line_2)

        self.search_bool = False
        self.k = 1
        self.address = None
        self.address_code = None

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
        if s == 'Up':
            map_params['z'] += 1 if map_params['z'] != 19 else 0
            self.k /= 2
        else:
            map_params['z'] -= 1 if map_params['z'] != 0 else 0
            self.k *= 2
        self.update_im()

    def change_centre_coords(self, s):
        coor = list(map(float, map_params['ll'].split(',')))
        if s == "Up":
            coor[1] += 0.011 * self.k
        elif s == "Down":
            coor[1] -= 0.011 * self.k
        elif s == "Left":
            coor[0] -= 0.011 * self.k
        elif s == "Right":
            coor[0] += 0.011 * self.k
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
            except Exception:
                self.lineEdit.setText('Адресс не действителен')
                return

            map_params['pt'] = pos + ',round'
            map_params['ll'] = pos
            self.search_bool = True
            self.update_im()
            self.address_postal(geo_object)

    def discharge(self):
        if self.search_bool:
            map_params['pt'] = None
        self.search_bool = False
        self.address = None
        self.address_code = None
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
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

    def address_postal(self, geo_object):
        try:
            self.address = geo_object['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
            postal_code = geo_object['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
            self.address_code = self.address + ' | ' + postal_code

            text = self.buttonGroup_2.checkedButton().text()
            if text == 'Отоброжать почтовый индекс':
                self.lineEdit_2.setText(self.address_code)
            elif text == 'Не отображать почтовый индекс':
                self.lineEdit_2.setText(self.address)

        except Exception:
            self.lineEdit_2.setText('Не удалось вывести адрес')
            self.address = None
            self.address_code = None
            return

    def change_edit_line_2(self):
        text = self.buttonGroup_2.checkedButton().text()
        if text == 'Отоброжать почтовый индекс' and self.address_code:
            self.lineEdit_2.setText(self.address_code)
        elif text == 'Не отображать почтовый индекс' and self.address:
            self.lineEdit_2.setText(self.address)


geocoder_params = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': None,
    'format': 'json'
}
map_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "l": 'map',
    "ll": '0,0',
    'size': '450,450',
    'z': 1,
    'pt': None}

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
map_api_server = "http://static-maps.yandex.ru/1.x/"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maps = MyMap()
    maps.show()
    sys.exit(app.exec_())
