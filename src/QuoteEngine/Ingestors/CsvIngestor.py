"""CSV file parser.
    
Returns:
    {list}: list of quotes.
"""
import csv
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CsvIngestor(IngestorInterface):
    """initialize allowed extensions."""
    
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        """Parse csv file."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                quoteModel = QuoteModel(row['body'], row['author'])
                quotes.append(quoteModel)

        return quotes
