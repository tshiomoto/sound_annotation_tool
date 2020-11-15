import sys
from PyQt5 import QtWidgets
from main_window import Ui_MainWindow


class SoundAnnotationTool(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(SoundAnnotationTool, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SoundAnnotationTool()
    window.show()
    sys.exit(app.exec_())