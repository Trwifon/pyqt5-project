from datetime import datetime
from PyQt5.QtWidgets import QTableWidgetItem
from db_connection import get_firm_list, get_day_report, get_day_cash


def give_firm_list():
    rows = get_firm_list()
    firm_list = [str(i[0]) for i in rows]
    firm_list.sort()
    return firm_list


def set_form(my_form):
    current_date = datetime.now().date()
    my_form.labelDate.setText(str(current_date))

    firm_list = give_firm_list()
    my_form.comboBoxFirm.addItems(firm_list)

    warehouse = 'Поръчки PVC' #да не е хардкорнато
    report = get_day_report(warehouse, current_date)
    day_cash = get_day_cash(warehouse, current_date)

    my_form.tableWidget.setItem(1, 1, QTableWidgetItem('Наличност каса:'))
    my_form.tableWidget.setItem(1, 2, QTableWidgetItem(str(day_cash)))

    row_index = 3
    for current_tuple in report:
        col_index = 0
        for value in current_tuple:
            my_form.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))
            col_index += 1
        row_index += 1

def calculate_close_balance(my_form, open_balance, amount):
    close_balance = 0
    if my_form.radioCash.isChecked() or my_form.radioBank.isChecked():
        close_balance = open_balance + amount
    else:
        close_balance = open_balance - amount
    return close_balance



