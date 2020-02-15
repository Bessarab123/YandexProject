from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QFileDialog, QInputDialog, QMessageBox
from Widget import Ui_Dialog


class My_Map(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.discharge)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.change_mashtab()

        if event.key() == Qt.Key_PageDown:
            self.change_mashtab()

        if event.key() == Qt.Key_Up:
            self.change_centre_coords()

        if event.key() == Qt.Key_Down:
            self.change_centre_coords()

        if event.key() == Qt.Key_Left:
            self.change_centre_coords()

        if event.key() == Qt.Key_Right:
            self.change_centre_coords()

    def change_mashtab(self):
        pass

    def change_centre_coords(self):
        pass

    def change_map_sloi(self):
        pass

    def search(self):
        values = self.lineEdit.text()

    def discharge(self):
        pass


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    map = My_Map()
    map.show()
    sys.exit(app.exec_())
