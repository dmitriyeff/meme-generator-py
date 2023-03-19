from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
from docx import Document

class DocxImporter(IngestorInterface):
    """ Parse docx file """
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        
        quotes = []
        
        document = Document(path)

        for para in document.paragraphs:
            if para.text != "":
                quote = para.text.split(',')
                [body, author] = quote[0].split('-')
                
                quoteModel = QuoteModel(body.strip().strip('\"'), author.strip())
                
                quotes.append(quoteModel)
        
        return quotes

print(DocxImporter.parse('src/_data/DogQuotes/DogQuotesDOCX.docx'))          
    