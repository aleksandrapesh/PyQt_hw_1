from PySide6 import QtWidgets, QtCore

from hw_1.ui.c_login_form import Ui_Form


class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = LoginWindow()
    win.show()

    app.exec()
