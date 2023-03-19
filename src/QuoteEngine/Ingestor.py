from IngestorInterface import IngestorInterface
import Ingestors

class Ingestor(IngestorInterface):    
    ingestors = {
        'txt': Ingestors.TxtIngestor,
        'csv': Ingestors.CsvIngestor,
        'pdf': Ingestors.PdfIngestor,
        'docx': Ingestors.DocxIngestor,
    }
    
    
    @classmethod
    def parse(cls, path):
        """ Select appropriate ingestor class to parse provided file """
        file_extension = cls.get_file_extension(path)
        
        try:
            ingestor = cls.ingestors.get(file_extension)
            
            if not ingestor:
                raise Exception(f"File extension with name: `{file_extension}`, is not supported")
            
            return cls.ingestors.get(file_extension).parse(path)
        except Exception as error:
            print(error)
        
print(Ingestor.parse('src/_data/DogQuotes/DogQuotesPDF.pd'))