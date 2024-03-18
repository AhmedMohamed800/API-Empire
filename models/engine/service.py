#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.api import API


class ServiceEngine:
    """A class representing the service engine.

    This class provides methods to interact with services and APIs.

    Attributes:
        __storage (DBStorage):\
            An instance of the DBStorage class for data storage.

    """

    def __init__(self):
        """Initialize the ServiceEngine class."""
        self.__storage = DBStorage()

    def reload(self):
        """Reload the data storage."""
        self.__storage.reload()

    def get_all(self):
        """Get all services.

        Returns:
            dict: A dictionary containing the list of services and categories.

        """
        data = {}
        data['service'] = [api.to_dict() for api in self.__storage.all(API)]
        data['categorys'] = list(set([api.category
                                      for api in self.__storage.all(API)]))
        return data

    def get_weather(self):
        """Get the weather.

        Returns:
            str: The weather condition.

        """
        return "sunny"

    def get(self, service_id):
        """Get a service by ID.

        Args:
            service_id (int): The ID of the service.

        Returns:
            list: A list of answers and service information.

        Raises:
            ValueError: If the service_id is not provided or is not an integer.
            ValueError: If the service_id does not exist.

        """
        if service_id is None:
            raise ValueError("service_id is required")
        try:
            service_id = int(service_id)
        except ValueError:
            raise ValueError("service_id must be an integer")
        if not self.__storage.get("API", id=service_id):
            raise ValueError("service_id does not exist")
        service = self.__storage.get("API", id=service_id).to_dict()
        answers = [answer.to_dict() for answer in
                   self.__storage.get("Endpoint", api_id=service['id'])]
        for i in range(len(answers)):
            answers[i]['method'] = answers[i]['method'].value
        answers.append({"title": service['title'],
                        "description": service['description']})
        return answers
