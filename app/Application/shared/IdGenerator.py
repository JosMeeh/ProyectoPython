from abc import ABC, abstractmethod


class IUUIDGenerator(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def generate(self) -> str:
        pass