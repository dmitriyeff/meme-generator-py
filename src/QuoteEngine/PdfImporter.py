import pdftotext
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class PdfImporter(IngestorInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path):
        """ Parse pdf file """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        
        quotes = []
        with open(path, "rb") as f:
            pdf = pdftotext.PDF(f)
            strings = "\n\n".join(pdf).strip().split('\n')
            
            for string in strings:
                [body, author] = string.split(' - ')
                quoteModel = QuoteModel(body.strip('\"'), author)
                quotes.append(quoteModel)

        return quotes

            
    