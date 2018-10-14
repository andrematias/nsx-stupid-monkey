import time
from sys import stdout

import settings
import report
import rules
import database
import webbrowser
import schedule


def alert():
    print("Analisando os dados de envio de faturas NET Atende...")
    try:
        invoices_queued = database.qtd_invoices()[1::][0][0]
        rules.max_invoices_queued(invoices_queued)

        last_invoice = database.last_invoice()[1::]
        rules.time_diff(last_invoice)

        last_invoices = database.last_send_mails()[1::]
        rules.diff_request_and_send_mail(last_invoices)

        print('Até agora tudo certo, Ua a a!!! :D')
        webbrowser.open(settings.SUCCESS_ALARM_PATH)

    except rules.MaxInvoiceQueuedException as max_queue:
        print(max_queue)
        webbrowser.open(settings.DANGER_ALARM_PATH)

    except rules.SendMailTimeException as latence:
        print(latence)
        webbrowser.open(settings.DANGER_ALARM_PATH)


def job():
    alert()
    report.main()


if __name__ == '__main__':
    schedule.every(90).minutes.do(job)
    print('Macaco esperando...')

    while True:
        schedule.run_pending()
        time.sleep(1)
