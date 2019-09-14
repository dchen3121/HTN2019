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


    def register_model(self, email: str, password: str):
        Database.new_user(email, password)

    # @classmethod
    # def get_by_email(cls: Type[T], email: str) -> T:
    #     return cls(Database.find(email).key(), Database.find(email).val())

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        things_from_db = Database.find(cls.username, {})
        return [cls(**thing) for thing in things_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T:
        return cls(**Database.find_one(cls.username.split, {attribute: value}))
