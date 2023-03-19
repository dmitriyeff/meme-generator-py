from typing import List
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    @abstractmethod
    def can_ingest(cls, path) -> bool:
        pass
    
    @abstractmethod
    def def_parse(cls, path: str) -> List[QuoteModel]:
        pass