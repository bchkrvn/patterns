from abc import ABC, abstractmethod


class BaseValidator(ABC):
    @property
    @abstractmethod
    def type_(self):
        pass

    @classmethod
    def validate(cls, data):
        if cls.type_ is None:
            raise NotImplemented()
        if not isinstance(data, cls.type_):
            raise TypeError()


class StringValidator(BaseValidator):
    type_ = str


class IntegerValidator(BaseValidator):
    type_ = int


class ListValidator(BaseValidator):
    type_ = list


class DictValidator(BaseValidator):
    type_ = dict
