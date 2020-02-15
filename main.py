from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QFileDialog, QInputDialog, QMessageBox
import io
import sys
from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage, QCursor
import sys
import PyQt5
from pprint import pprint
import requests

address_ll = input()

map_params = {
    "l": "map",
    "ll": address_ll
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
print(response.url)
if not response:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(2)

Image.open(io.BytesIO(response.content)).show()
