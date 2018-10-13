from peewee import *
import settings

_last_request_invoice = "select * from envio_fatura e where e.TipoSolicitacao = 0 and e.Situacao in (0,3) and e.TentativasGeracao < 3 limit 1"
_qtd_invoices = "select count(*) from envio_fatura e where e.TipoSolicitacao = 0 and e.Situacao in (0,3) and e.TentativasGeracao < 3"
_last_send_mails = "select * From netatende.envio_fatura e where e.TipoSolicitacao = 0 and e.DataEnvioEmail is not null order by e.DataEnvioEmail desc limit 10;"


def get_conn(**kwargs):
    try:
        mysql_db = MySQLDatabase(**kwargs)
        if mysql_db.connect():
            return mysql_db
    except Exception:
        raise


_conn = get_conn(**settings.NET_ATENDE_DATABASE)

INVOICE_HEADER = ('Codigo', 'Email', 'DataSolicitacao', 'DataCriacaoArquivo', 'DataEnvioEmail', 'Situacao', 'CidadeContrato', 'CodigoFatura', 'TipoFatura', 'TentativasGeracao', 'TentativasEnvio', 'DataVencimento', 'Valor', 'SituacaoFatura', 'CodigoContaFinanceira', 'CodigoInteracao', 'CodigoDatacenterInteracao', 'CodigoLogEnvio', 'CodigoLogGeracao', 'TipoSolicitacao')


def last_invoice():
    cursor_last_invoice = _conn.execute_sql(_last_request_invoice)
    last = list(cursor_last_invoice.fetchall())
    last.insert(0, INVOICE_HEADER)
    return last


def qtd_invoices():
    cursor_qtd_invoice = _conn.execute_sql(_qtd_invoices)
    total_invoices = list(cursor_qtd_invoice.fetchall())
    total_invoices.insert(0, ('Quantidade', ))
    return total_invoices


def last_send_mails():
    cursor_send_mails = _conn.execute_sql(_last_send_mails)
    send_emails = list(cursor_send_mails.fetchall())
    send_emails.insert(0, INVOICE_HEADER)
    return send_emails
