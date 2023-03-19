from typing import List
from abc import ABC, abstractmethod
from QuoteModel import QuoteModel

class IngestorInterface(ABC):
	@abstractmethod
	def def_parse(cls, path: str) -> List[QuoteModel]:
		pass
    
	@classmethod
	def can_ingest(cls, path) -> bool:
		""" Return boolean wether file could be parsed or not """
		extension = path.split('.')[-1]
		
		return extension in cls.allowed_extensions