from PySide6 import QtWidgets, QtCore


class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:

        self.setWindowTitle("Вход в приложение")
        size = QtCore.QSize(300, 150)
        self.setFixedSize(size)

        labelLogin = QtWidgets.QLabel()
        labelLogin.setMinimumWidth(45)
        labelLogin.setText("Логин")

        labelPassword = QtWidgets.QLabel()
        labelPassword.setMinimumWidth(45)
        labelPassword.setText("Пароль")

        self.lineEditLogin = QtWidgets.QLineEdit()

        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.pushButtonRegistration = QtWidgets.QPushButton()
        self.pushButtonRegistration.setText("Регистрация")

        self.pushButtonOk = QtWidgets.QPushButton()
        self.pushButtonOk.setText("Ок")

        self.pushButtonCancel = QtWidgets.QPushButton()
        self.pushButtonCancel.setText("Отмена")

        # layouts
        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(labelPassword)
        layoutPassword.addWidget(self.lineEditPassword)

        layoutRegistration = QtWidgets.QHBoxLayout()
        layoutRegistration.addSpacerItem(
            QtWidgets.QSpacerItem(
                20, 20, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        layoutRegistration.addWidget(self.pushButtonRegistration)

        layoutHandle = QtWidgets.QHBoxLayout()
        layoutHandle.addSpacerItem(
            QtWidgets.QSpacerItem(
                20, 20, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        layoutHandle.addWidget(self.pushButtonOk)
        layoutHandle.addWidget(self.pushButtonCancel)

        layoutMain =QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addLayout(layoutRegistration)
        layoutMain.addLayout(layoutHandle)



        self.setLayout(layoutMain)




if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = LoginWindow()
    win.show()

    app.exec()
