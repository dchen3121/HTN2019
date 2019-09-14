from typing import List, TypeVar, Type, Dict, Union
from abc import ABCMeta, abstractmethod
from common.database import Database

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):

    def __init__(self, username: str, data: Dict):
        self.username = username
        self.data = data

    def add_to_firebase(self):
        Database.insert(self.username, self.data)

    def save_to_firebase(self):
        Database.update(self.username, self.data)

    def remove_from_firebase(self):
        Database.remove(self.username, self.data)

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    def register_model(self, user):
        Database.new_user(user)
