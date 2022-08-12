from PyQt5.QtWidgets import QApplication, QSizePolicy
from PyQt5.uic import loadUi
import sys


class Calculator:
    def __init__(self, design_file):
        self.design = design_file
        self.design.setFixedSize(400,200)
        self.design.inputWindow.setDisabled(True)
        self.design.inputWindow.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.design.inputWindow.setStyleSheet('* {background: #FFF; color: #000; font-size: 30px;}')
        self.btn_manager()

    def show(self):
        self.design.show()

    def btn_manager(self):
        self.design.btn0.clicked.connect(
            lambda: self.increment_display('0')
        )
        self.design.btn1.clicked.connect(
            lambda: self.increment_display('1')
        )
        self.design.btn2.clicked.connect(
            lambda: self.increment_display('2')
        )
        self.design.btn3.clicked.connect(
            lambda: self.increment_display('3')
        )
        self.design.btn4.clicked.connect(
            lambda: self.increment_display('4')
        )
        self.design.btn5.clicked.connect(
            lambda: self.increment_display('5')
        )
        self.design.btn6.clicked.connect(
            lambda: self.increment_display('6')
        )
        self.design.btn7.clicked.connect(
            lambda: self.increment_display('7')
        )
        self.design.btn8.clicked.connect(
            lambda: self.increment_display('8')
        )
        self.design.btn9.clicked.connect(
            lambda: self.increment_display('9')
        )
        self.design.btnDot.clicked.connect(
            lambda: self.increment_display('.')
        )

        self.design.btnSum.setStyleSheet('* {background: #55abcc; color: #000;}')
        self.design.btnSum.clicked.connect(
            lambda: self.increment_display('+')
        )

        self.design.btnSub.setStyleSheet('* {background: #55abcc; color: #000;}')
        self.design.btnSub.clicked.connect(
            lambda: self.increment_display('-')
        )

        self.design.btnMult.setStyleSheet('* {background: #55abcc; color: #000;}')
        self.design.btnMult.clicked.connect(
            lambda: self.increment_display('*')
        )

        self.design.btnDiv.setStyleSheet('* {background: #55abcc; color: #000;}')
        self.design.btnDiv.clicked.connect(
            lambda: self.increment_display('/')
        )

        self.design.btnClear.clicked.connect(
            lambda: self.design.inputWindow.setText('')
        )
        self.design.btnClear.setStyleSheet('* {background: #c87209; color: #000; font-weight: 900}')

        self.design.btnErase.clicked.connect(
            lambda: self.design.inputWindow.setText(self.design.inputWindow.text()[:-1])
        )
        self.design.btnErase.setStyleSheet('* {background: #c87209; color: #000; font-weight: 900}')

        self.design.btnEqual.clicked.connect(self.equal_btn)
        self.design.btnEqual.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.design.btnEqual.setStyleSheet('* {background: #65d55d; color: #000; font-weight: 900}')

    def increment_display(self, character):
        self.design.inputWindow.setText(self.design.inputWindow.text() + character)

    def equal_btn(self):
        try:
            self.design.inputWindow.setText(
                str(eval(self.design.inputWindow.text()))
            )
        except Exception as e:
            self.design.inputWindow.setText('Invalid math.')


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    calculator = Calculator(loadUi('design.ui'))
    calculator.show()
    qApp.exec_()
