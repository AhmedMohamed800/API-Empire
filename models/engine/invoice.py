#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.invoice import Invoice


class Payment:
    """ AUTH class """
    __storage = None

    def __init__(self):
        """ init """
        self.__storage = DBStorage()

    def reload(self):
        """ reload """
        self.__storage.reload()

    def create_invoice(self, session_id, payment_id, amount):
        """ create invoice """
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        if not user.auth:
            raise ValueError("no auth key found")
        num = float(amount) / 0.01
        user.auth.max_req += num
        self.__storage.new(Invoice(user_id=user.id, amount=amount,
                                   payment_id=payment_id, request=num))
        self.__storage.save()
        return True
    
    def get_invoice(self, session_id):
        """ get all invoices """
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        invoices = self.__storage.all(Invoice, user_id=user.id)
        data = []
        for invoice in invoices:
            data.append(invoice.to_dict())
        return data
