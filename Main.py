from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import init_form
from db_connection import get_firm_open_balance


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main_form.ui", self)
        init_form.set_form(self)
        self.comboBoxFirm.activated.connect(self.firm_selected)
        self.lineAmount.textEdited.connect(self.amount_refresh)


    def firm_selected(self):
        open_balance = get_firm_open_balance(self.comboBoxFirm.currentText())
        self.labelOpenBalance.setText(str(open_balance))
        self.labelCloseBalance.setText(str(open_balance))
        self.lineAmount.setText('888')
        return open_balance

    def amount_refresh(self):
        open_balance = self.firm_selected()
        if self.lineAmount.text().isdigit():
            amount = int(self.lineAmount.text())
            # close_balance = open_balance + amount
            close_balance = init_form.calculate_close_balance(self, open_balance, amount)
            self.labelCloseBalance.setText(str(close_balance))
        else:
            self.labelCloseBalance.setText(str(open_balance))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = Main()
    my_window.show()
    app.exec_()