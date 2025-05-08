# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFontDialog, QFileDialog, QInputDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # === Style Buttons ===
        self.default_style = """
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                font-weight: bold;
                padding: 6px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #CCC;
            }
        """
        self.active_style = """
            QPushButton {
                background-color: #218838;
                color: white;
                font-weight: bold;
                padding: 6px;
                border-radius: 5px;
            }
        """

        # === Buttons ===
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(self.default_style)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(self.default_style)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 20, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(self.default_style)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 70, 571, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(self.default_style)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 400, 20))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuFitur = QtWidgets.QMenu(self.menubar)
        self.menuFitur.setObjectName("menuFitur")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionKeluar = QtWidgets.QAction(MainWindow)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionInput_Nama = QtWidgets.QAction(MainWindow)
        self.actionInput_Nama.setObjectName("actionInput_Nama")
        self.actionPilih_Font = QtWidgets.QAction(MainWindow)
        self.actionPilih_Font.setObjectName("actionPilih_Font")
        self.actionBuka_File = QtWidgets.QAction(MainWindow)
        self.actionBuka_File.setObjectName("actionBuka_File")

        self.menuFile.addAction(self.actionKeluar)
        self.menuFitur.addAction(self.actionInput_Nama)
        self.menuFitur.addAction(self.actionPilih_Font)
        self.menuFitur.addAction(self.actionBuka_File)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFitur.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # === Connect Buttons ===
        self.pushButton.clicked.connect(self.input_nama)
        self.pushButton_2.clicked.connect(self.pilih_font)
        self.pushButton_3.clicked.connect(self.buka_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Input Nama"))
        self.pushButton_2.setText(_translate("MainWindow", "Pilih Font"))
        self.pushButton_3.setText(_translate("MainWindow", "Buka File"))
        self.pushButton_4.setText(_translate("MainWindow", "Pilih Font"))
        self.label.setText(_translate("MainWindow", "Nama :"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFitur.setTitle(_translate("MainWindow", "Fitur"))
        self.actionKeluar.setText(_translate("MainWindow", "Keluar"))
        self.actionInput_Nama.setText(_translate("MainWindow", "Input Nama"))
        self.actionPilih_Font.setText(_translate("MainWindow", "Pilih Font"))
        self.actionBuka_File.setText(_translate("MainWindow", "Buka File"))

    # === Logic Functions ===
    def input_nama(self):
        self.pushButton.setStyleSheet(self.active_style)
        nama, ok = QInputDialog.getText(None, "Input Nama", "Masukkan nama Anda:")
        if ok and nama:
            self.label.setText(f"Nama : {nama}")
        self.pushButton.setStyleSheet(self.default_style)

    def pilih_font(self):
        self.pushButton_2.setStyleSheet(self.active_style)
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
        self.pushButton_2.setStyleSheet(self.default_style)

    def buka_file(self):
        self.pushButton_3.setStyleSheet(self.active_style)
        file_path, _ = QFileDialog.getOpenFileName(None, "Buka File", "", "All Files (*.*)")
        if file_path:
            self.label.setText(f"File: {file_path}")
        self.pushButton_3.setStyleSheet(self.default_style)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
