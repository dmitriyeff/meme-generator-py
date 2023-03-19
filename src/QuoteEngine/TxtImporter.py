from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel


class TxtImporter(IngestorInterface):
    """ Parse txt file """
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        
        quotes = []
        
        with open(path,'r', encoding='utf-8-sig') as txt:
            for row in txt:
                [body, author] = row.strip().split('-')
                
                quote_model = QuoteModel(body, author)
                quotes.append(str(quote_model))
        
        return quotes     
    