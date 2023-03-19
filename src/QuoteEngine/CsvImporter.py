import csv
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class CsvImporter(IngestorInterface):
    """ Parse csv file """
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        
        quotes = []
        
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                quoteModel = QuoteModel(row['body'], row['author'])
                quotes.append(quoteModel)
        
        return quotes

print(CsvImporter.parse('src/_data/DogQuotes/DogQuotesCSV.csv'))

            
    