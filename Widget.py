# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(685, 569)
        Dialog.setMinimumSize(QtCore.QSize(684, 569))
        Dialog.setMaximumSize(QtCore.QSize(2000, 2000))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(650, 450))
        self.label.setMaximumSize(QtCore.QSize(650, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("123.bmp"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(250, 35))
        self.widget.setMaximumSize(QtCore.QSize(250, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_map = QtWidgets.QRadioButton(self.widget)
        self.radioButton_map.setMinimumSize(QtCore.QSize(73, 17))
        self.radioButton_map.setMaximumSize(QtCore.QSize(73, 17))
        self.radioButton_map.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_map.setChecked(True)
        self.radioButton_map.setObjectName("radioButton_map")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_map)
        self.horizontalLayout.addWidget(self.radioButton_map)
        self.radioButton_sat = QtWidgets.QRadioButton(self.widget)
        self.radioButton_sat.setMinimumSize(QtCore.QSize(74, 17))
        self.radioButton_sat.setMaximumSize(QtCore.QSize(74, 17))
        self.radioButton_sat.setChecked(False)
        self.radioButton_sat.setObjectName("radioButton_sat")
        self.buttonGroup.addButton(self.radioButton_sat)
        self.horizontalLayout.addWidget(self.radioButton_sat)
        self.radioButton_sat_skl = QtWidgets.QRadioButton(self.widget)
        self.radioButton_sat_skl.setMinimumSize(QtCore.QSize(73, 17))
        self.radioButton_sat_skl.setMaximumSize(QtCore.QSize(73, 17))
        self.radioButton_sat_skl.setObjectName("radioButton_sat_skl")
        self.buttonGroup.addButton(self.radioButton_sat_skl)
        self.horizontalLayout.addWidget(self.radioButton_sat_skl)
        self.verticalLayout.addWidget(self.widget)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton_map.setText(_translate("Dialog", "Схема"))
        self.radioButton_sat.setText(_translate("Dialog", "Спутник"))
        self.radioButton_sat_skl.setText(_translate("Dialog", "Гибрид"))
        self.pushButton.setText(_translate("Dialog", "Искать"))
        self.pushButton_2.setText(_translate("Dialog", "Сброс поискового результата"))
