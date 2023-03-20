from typing import List
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Return boolean wether file could be parsed or not """
        extension = cls.get_file_extension(path)

        return extension in cls.allowed_extensions

    @classmethod
    def get_file_extension(cls, path) -> str:
        """ Return file extension name """
        return path.split('.')[-1]
