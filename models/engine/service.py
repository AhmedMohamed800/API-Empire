#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.api import API
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4 as uu


class Service:
    """service class"""
    def __init__(self):
        """ init """
        self.__storage = DBStorage()
    
    def reload(self):
        """ reload """
        self.__storage.reload()
    
    def get_all(self):
        """get all services"""
        data = {}
        data['service'] = [api.to_dict() for api in self.__storage.all(API)]
        data['categorys'] = list(set([api.category for api in self.__storage.all(API)]))
        return data

    def get_weather(self):
        """ get weather """
        return "sunny"
    
    def get(self, service_id):
        """get service by id"""
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
