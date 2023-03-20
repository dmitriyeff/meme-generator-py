"""PDF file parser.
    
Returns:
    {list}: list of quotes
"""
import subprocess
import os
import random
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class PdfIngestor(IngestorInterface):
    """Initialize allowed file extensions."""
    
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """Parse pdf file."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        tmp = f'./{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(',')
                [body, author] = parsed[0].split(' - ')
                quoteModel = QuoteModel(body.strip('\"'), author)
                quotes.append(quoteModel)

        file_ref.close()
        os.remove(tmp)
        return quotes
