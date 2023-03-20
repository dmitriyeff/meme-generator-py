"""DOCX file parser.

Returns:
    {list}: list of quotes
"""
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    """Initialize allowed extensions."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """Parse docx file."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []

        f = open(path, 'rb')
        document = Document()
        f.close()

        for para in document.paragraphs:
            if para.text != "":
                quote = para.text.split(',')
                [body, author] = quote[0].split('-')

                quoteModel = QuoteModel(
                    body.strip().strip('\"').encode('utf-8'),
                    author.strip().encode('utf-8')
                )

                quotes.append(quoteModel)
        return quotes
