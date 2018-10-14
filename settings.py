import os

NET_ATENDE_DATABASE = {
    'database': 'netatende',
    'user': '########',
    'password': '########',
    'host': '#######',
    'port': 3306
}

REPORT_BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')

if not os.path.isdir(REPORT_BASE_PATH):
    os.makedirs(REPORT_BASE_PATH)

# Caminho do relatório
INVOICE_REPORT_PATH = os.path.join(REPORT_BASE_PATH, 'NET Atende Invoices.xlsx')

DANGER_ALARM_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'songs', 'siren.mp3')
SUCCESS_ALARM_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'songs', 'bell.mp3')