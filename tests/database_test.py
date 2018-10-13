import settings
import database
from peewee import MySQLDatabase
from unittest import TestCase, main


class DatabaseTest(TestCase):

    def test_get_conn(self):
        self.assertIsInstance(
            database.get_conn(**settings.NET_ATENDE_DATABASE),
            MySQLDatabase
        )

    def test_last_invoice(self):
        last_invoice = database.last_invoice()
        self.assertIsInstance(last_invoice, list)

        for invoice in last_invoice:
            self.assertIsInstance(invoice, tuple)

    def test_last_send_mails(self):
        last_send_mails = database.last_send_mails()
        self.assertIsInstance(last_send_mails, list)

        for invoice in last_send_mails:
            self.assertIsInstance(invoice, tuple)

    def test_qtd_invoice_queued(self):
        qtd_invoice_queued = database.qtd_invoices()
        self.assertIsInstance(qtd_invoice_queued, list)
        self.assertIsInstance(qtd_invoice_queued[1][0], int)
        for qtd in qtd_invoice_queued:
            self.assertIsInstance(qtd, tuple)



if __name__ == '__main__':
    main()