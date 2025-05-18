from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self):
        super().__init__()


    @classmethod
    @abstractmethod
    def product(cls, *args, **kwargs):
        pass

