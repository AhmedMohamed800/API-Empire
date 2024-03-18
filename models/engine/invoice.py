#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.invoice import Invoice


class PaymentEngine:
    """
    The PaymentEngine class handles the creation and\
        retrieval of invoices for users.
    """

    __storage = None

    def __init__(self):
        """
        Initializes a new instance of the PaymentEngine class.
        """
        self.__storage = DBStorage()

    def reload(self):
        """
        Reloads the storage.
        """
        self.__storage.reload()

    def create_invoice(self, session_id, payment_id, amount):
        """
        Creates a new invoice for the user with the specified session ID,\
            payment ID, and amount.

        Args:
            session_id (str): The session ID of the user.
            payment_id (str): The payment ID for the invoice.
            amount (float): The amount of the invoice.

        Returns:
            bool:\
                True if the invoice was created successfully, False otherwise.

        Raises:
            ValueError: If no user is found or no auth key is found.
        """
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
        """
        Retrieves all invoices for the user with the specified session ID.

        Args:
            session_id (str): The session ID of the user.

        Returns:
            list: A list of dictionaries representing the invoices.

        Raises:
            ValueError: If no session is found or no user is found.
        """
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
