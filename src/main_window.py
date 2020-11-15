# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from backend import SATSystem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 893)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(510, 810, 91, 23))
        self.saveButton.setObjectName("saveButton")

        self.writeButton = QtWidgets.QToolButton(self.centralwidget)
        self.writeButton.setGeometry(QtCore.QRect(610, 810, 101, 21))
        self.writeButton.setObjectName("writeButton")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 701, 771))
        self.widget.setObjectName("widget")

        self.all_layout_view = QtWidgets.QVBoxLayout(self.widget)
        self.all_layout_view.setContentsMargins(0, 0, 0, 0)
        self.all_layout_view.setObjectName("all_layout_view")
        
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setObjectName("tableView")
        self.all_layout_view.addWidget(self.tableView)
        
        self.window_size_pane = QtWidgets.QHBoxLayout()
        self.window_size_pane.setContentsMargins(150, -1, -1, -1)
        self.window_size_pane.setSpacing(150)
        self.window_size_pane.setObjectName("window_size_pane")
        
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.window_size_pane.addWidget(self.label_3)
        
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.window_size_pane.addWidget(self.horizontalSlider_2)
        
        self.all_layout_view.addLayout(self.window_size_pane)
        
        self.view_pane = QtWidgets.QVBoxLayout()
        self.view_pane.setObjectName("view_pane")
        
        self.all_wave_pane = QtWidgets.QHBoxLayout()
        self.all_wave_pane.setContentsMargins(-1, -1, 5, -1)
        self.all_wave_pane.setSpacing(10)
        self.all_wave_pane.setObjectName("all_wave_pane")
        
        self.all_view_label = QtWidgets.QLabel(self.widget)
        self.all_view_label.setObjectName("all_view_label")
        self.all_wave_pane.addWidget(self.all_view_label)

        self.all_wave_view = QtWidgets.QGraphicsView(self.widget)
        self.all_wave_view.setObjectName("all_wave_view")
        self.all_wave_pane.addWidget(self.all_wave_view)
        self.view_pane.addLayout(self.all_wave_pane)
        
        self.window_area_slider = QtWidgets.QSlider(self.widget)
        self.window_area_slider.setOrientation(QtCore.Qt.Horizontal)
        self.window_area_slider.setObjectName("window_area_slider")
        self.view_pane.addWidget(self.window_area_slider)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.target_wave_label = QtWidgets.QLabel(self.widget)
        self.target_wave_label.setObjectName("target_wave_label")
        self.horizontalLayout_2.addWidget(self.target_wave_label)
        
        self.target_wave_view = QtWidgets.QGraphicsView(self.widget)
        self.target_wave_view.setEnabled(True)
        self.target_wave_view.setObjectName("target_wave_view")
        self.horizontalLayout_2.addWidget(self.target_wave_view)
        self.view_pane.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_label = QtWidgets.QLabel(self.widget)
        self.label_label.setObjectName("label_label")
        self.horizontalLayout_3.addWidget(self.label_label)
        
        self.label_view = QtWidgets.QGraphicsView(self.widget)
        self.label_view.setObjectName("label_view")
        self.horizontalLayout_3.addWidget(self.label_view)
        self.view_pane.addLayout(self.horizontalLayout_3)
        
        self.all_layout_view.addLayout(self.view_pane)
        self.all_layout_view.setStretch(0, 10)
        self.all_layout_view.setStretch(1, 1)
        self.all_layout_view.setStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew_project = QtWidgets.QAction(MainWindow)
        self.actionnew_project.setObjectName("actionnew_project")
        
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        
        self.actionload = QtWidgets.QAction(MainWindow)
        self.actionload.setObjectName("actionload")
        
        self.actionexport_text_file = QtWidgets.QAction(MainWindow)
        self.actionexport_text_file.setObjectName("actionexport_text_file")
        
        self.actionplay_all_area = QtWidgets.QAction(MainWindow)
        self.actionplay_all_area.setObjectName("actionplay_all_area")
        
        self.actionplay_target_area = QtWidgets.QAction(MainWindow)
        self.actionplay_target_area.setObjectName("actionplay_target_area")
        
        self.actionannotate = QtWidgets.QAction(MainWindow)
        self.actionannotate.setObjectName("actionannotate")
        
        self.menu.addAction(self.actionnew_project)
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionload)
        self.menu.addSeparator()
        self.menu.addAction(self.actionexport_text_file)
        
        self.menu_2.addAction(self.actionplay_all_area)
        self.menu_2.addAction(self.actionplay_target_area)
        
        self.menu_3.addAction(self.actionannotate)
        
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.saveButton.clicked.connect(self.save_project)
        self.actionsave.triggered.connect(self.save_project)
        self.actionload.triggered.connect(self.load_project)
        self.actionnew_project.triggered.connect(self.new_project)

    def save_project(self): #イベント処理の関数
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fname, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "save project",
            "",
            "Sound Annotation Tool file(*.sat)",
            options=options
        )
        if fname:
            print(fname)

    def load_project(self): #イベント処理の関数
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "load project",
            "",
            "Sound Annotation Tool file(*.sat)",
            options=options
        )
        if fname:
            print(fname)

    def new_project(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "load sound file",
            "",
            "WAVE file format sound file(*.wav)",
            options=options
        )
        if fname:
            print(fname) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.writeButton.setText(_translate("MainWindow", "ラベルの書き出し"))
        self.label_3.setText(_translate("MainWindow", "対象波形の幅の大きさ："))
        self.all_view_label.setText(_translate("MainWindow", "波形全体："))
        self.target_wave_label.setText(_translate("MainWindow", "対象波形："))
        self.label_label.setText(_translate("MainWindow", "　　 ラベル："))
        self.menu.setTitle(_translate("MainWindow", "ファイル"))
        self.menu_2.setTitle(_translate("MainWindow", "音声"))
        self.menu_3.setTitle(_translate("MainWindow", "アノテーション"))
        self.actionnew_project.setText(_translate("MainWindow", "new project"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionload.setText(_translate("MainWindow", "load"))
        self.actionexport_text_file.setText(_translate("MainWindow", "export text file"))
        self.actionplay_all_area.setText(_translate("MainWindow", "play all area"))
        self.actionplay_target_area.setText(_translate("MainWindow", "play target area"))
        self.actionannotate.setText(_translate("MainWindow", "annotate"))

