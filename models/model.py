from typing import List, TypeVar, Type, Dict, Union
from abc import ABCMeta, abstractmethod
from common.database import Database

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):

    username: str
    data: Dict

    def __init__(self, *args, **kwargs):
        pass

    def add_to_firebase(self):
        Database.insert(self.username, self.data)

    def save_to_firebase(self):
        Database.update(self.username, self.data)

    def remove_from_firebase(self):
        Database.remove(self.username, self.data)

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def register_model(email: str, password: str):
        Database.new_user(email, password)

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:
        return cls.find_one_by("_id", _id)

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        things_from_db = Database.find(cls.username, {})
        return [cls(**thing) for thing in things_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T:
        return cls(**Database.find_one(cls.username, {attribute: value}))

    @classmethod
    def find_many_by(cls, attribute: str, value: str) -> List[T]:
        return [cls(**elem) for elem in Database.find(cls.username, {attribute: value})]

    @classmethod
    def find_many_by_dict(cls, query: Dict) -> List[T]:
        return [cls(**elem) for elem in Database.find(cls.username, query)]

    @classmethod
    def find_sorted_ascending(cls, query: Dict, key: str):
        return [cls(**elem) for elem in Database.find_all_sorted_by(cls.username, query, key, True)]

    @classmethod
    def find_sorted_descending(cls, query: Dict, key: str):
        return [cls(**elem) for elem in Database.find_all_sorted_by(cls.username, query, key, False)]
