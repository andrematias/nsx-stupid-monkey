import datetime

from database import INVOICE_HEADER

MAX_INVOICE_QUEUED = 1500
MAX_TIME_INTERVAL = datetime.timedelta(hours=3, minutes=0, seconds=0)


class SendMailTimeException(Exception):
    """
    Se a diferença de datas entre o campo DataSolicitacao e a data de agora for superior a 3h
    """


class MaxInvoiceQueuedException(Exception):
    """
    Se a cada execução da query o valor retornado estiver superior á  1500 itens.
    """


def _invoice_dict(invoices, header=INVOICE_HEADER):
    for invoice in invoices:
        yield dict(zip(header, invoice))


def time_diff(invoices):
    for invoice in _invoice_dict(invoices):
        diff = datetime.datetime.now() - invoice.get('DataSolicitacao')
        if diff > MAX_TIME_INTERVAL:
            raise SendMailTimeException('Data da Solicitacao Maior do que 3 horas, realizar o acionamento')


def diff_request_and_send_mail(invoices):
    for invoice in _invoice_dict(invoices):
        diff = invoice.get('DataEnvioEmail') - invoice.get('DataSolicitacao')
        if diff > MAX_TIME_INTERVAL:
            raise SendMailTimeException('DataEnvioEmail e a DataSolicitacao for superior a 3 horas, realizar o acionamento')


def max_invoices_queued(qtd):
    if qtd > MAX_INVOICE_QUEUED:
        raise MaxInvoiceQueuedException('Quantidade de faturas enfileiradas é maior do que %s' % MAX_INVOICE_QUEUED)




