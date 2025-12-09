import sys
from PyQt5 import QtWidgets

from interface import Ui_MainWindow
from robot import Robot, StateManager, Logger, Statistics


class Controller:
    # контроллер
    def __init__(self, ui):
        self.ui = ui
        self.robot = Robot()
        self.state = StateManager()
        self.logger = Logger()
        self.stats = Statistics()
        self.connect_buttons()

    def connect_buttons(self):
        # привязка всех QPushButton к пустым функциям
        for name in dir(self.ui):
            obj = getattr(self.ui, name)
            if isinstance(obj, QtWidgets.QPushButton):
                obj.clicked.connect(self.empty)

    def empty(self):
        pass


def main():
    # запуск Qt
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # создание контроллера
    controller = Controller(ui)

    # показ окна
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

