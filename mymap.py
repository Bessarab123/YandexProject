from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QFileDialog, QInputDialog, QMessageBox
from Widget import Ui_Dialog


class My_Map(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def change_mashtab(self):
        pass

    def change_centre_coords(self):
        pass

    def change_map_sloi(self):
        pass


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    map = My_Map()
    map.show()
    sys.exit(app.exec_())
