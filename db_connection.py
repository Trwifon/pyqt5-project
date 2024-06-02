import mysql.connector
import mysql.connector.locales.eng

dict_connection = {
    'host': '127.0.0.1',
    # 'host': '192.168.5.14',
    'port': '3306',
    'user': 'root',
    # 'user': 'Tsonka',
    'password': 'Proba123+',
    # 'password': 'Tsonka123+',
    'database': 'nadejda-94'
}
connection = mysql.connector.connect(**dict_connection)
cursor = connection.cursor()


def get_firm_list():
    connection.commit()
    cursor.execute("SELECT partner_name FROM partner")
    rows = cursor.fetchall()
    return rows


def get_firm_open_balance(name):
    query = "SELECT partner_balance FROM partner WHERE partner_name = %s"
    query_data = (name,)
    connection.commit()
    cursor.execute(query, query_data)
    balance = int(cursor.fetchone()[0])
    return balance

def get_day_report(warehouse, current_date):
    query = ("SELECT p.partner_name, r.order_type, r.ammount, r.note FROM records as r INNER"
            " JOIN partner as p ON r.partner_id = p.partner_id"
            " WHERE warehouse = %s and date = %s")
    query_data = (warehouse, current_date)
    connection.commit()
    cursor.execute(query, query_data)
    report = cursor.fetchall()
    return report

def get_day_cash(warehouse, current_date):
    query = ("SELECT SUM(ammount) FROM records WHERE warehouse = %s AND date = %s AND order_type = 'Каса'")
    query_data = (warehouse, current_date)
    connection.commit()
    cursor.execute(query, query_data)
    total_amount = cursor.fetchone()[0]
    return total_amount
