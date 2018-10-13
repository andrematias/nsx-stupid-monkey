import settings
import report


def main():
    if report.make_invoices_report(settings.INVOICE_REPORT_PATH):
        return 'Relatório criado com sucesso em %s' % settings.INVOICE_REPORT_PATH
    else:
        return 'Falha ao criar o relatório'


if __name__ == '__main__':
    print(main())
