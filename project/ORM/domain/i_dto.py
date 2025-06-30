from abc import abstractmethod
from typing import Dict, Any

class IDTO():
    @abstractmethod
    def put_into_dto(self):
        pass

    @staticmethod
    @abstractmethod
    def create_from_dto(_dict: Dict[str, Any]) -> object:
        pass
