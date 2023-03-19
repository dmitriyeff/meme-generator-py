import pdftotext
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class PdfImporter(IngestorInterface):
    """ Parse pdf file """
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path):
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

print(PdfImporter.parse('src/_data/DogQuotes/DogQuotesPDF.pdf'))

            
    