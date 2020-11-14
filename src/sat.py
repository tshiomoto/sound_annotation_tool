import sys
from PyQt5 import QtWidgets
from main_window import Ui_MainWindow


class SoundAnnotationTool(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(SoundAnnotationTool, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.saveButton.clicked.connect(self.save_project)
        self.ui.actionsave.triggered.connect(self.save_project)
        self.ui.actionload.triggered.connect(self.load_project)

    def save_project(self): #イベント処理の関数
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fname, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                         "save project",
                                                         "",
                                                         "Sound Annotation Tool file(*.sat)",
                                                         options=options)
        if fname:
            print(fname)

    def load_project(self): #イベント処理の関数
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         "load project",
                                                         "",
                                                         "Sound Annotation Tool file(*.sat)",
                                                         options=options)
        if fname:
            print(fname)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SoundAnnotationTool()
    window.show()
    sys.exit(app.exec_())