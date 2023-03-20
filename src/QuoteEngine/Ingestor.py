from .IngestorInterface import IngestorInterface
from QuoteEngine.Ingestors import TxtIngestor, CsvIngestor, PdfIngestor, DocxIngestor

class Ingestor(IngestorInterface):    
    ingestors = {
        'txt': TxtIngestor,
        'csv': CsvIngestor,
        'pdf': PdfIngestor,
        'docx': DocxIngestor,
    }
    
    
    @classmethod
    def parse(cls, path):
        """ Select appropriate ingestor class to parse provided file """
        file_extension = cls.get_file_extension(path)
        
        try:
            ingestor = cls.ingestors.get(file_extension)
            
            if not ingestor:
                """ Raise an exception if file extension parser is not provided """
                raise Exception(f"File extension with name: `{file_extension}`, is not supported")
            
            return cls.ingestors.get(file_extension).parse(path)
        except Exception as error:
            print(error)