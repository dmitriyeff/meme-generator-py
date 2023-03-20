from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """ Parse txt file """
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception(f"Cannot ingest exception")
        
        quotes = []
        
        with open(path,'r', encoding='utf-8-sig') as txt:
            for row in txt:
                [body, author] = row.strip().split('-')
                
                quote_model = QuoteModel(body, author)
                quotes.append(quote_model)
        
        return quotes     
    