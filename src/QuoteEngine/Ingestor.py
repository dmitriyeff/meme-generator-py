from IngestorInterface import IngestorInterface
from TxtImporter import TxtImporter
from CsvImporter import CsvImporter
from PdfImporter import PdfImporter
from DocxImporter import DocxImporter

class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        """ Select appropriate helper function to parse provided file """
        extension = path.split('.')[-1]
        
        if extension == "txt":
            return TxtImporter.parse(path)
        elif extension == "csv":
            return CsvImporter.parse(path)
        elif extension == "pdf":
            return PdfImporter.parse(path)
        elif extension == "docx":
            return DocxImporter.parse(path)
        else:
            raise Exception('Unnkown file extension')