"""
QuoteModal for quote data encapsulation.

Returns:
    {str}: quote that consists of body and author.
"""


class QuoteModel:
    """Encapsulate body and author."""

    def __init__(self, body, author):
        """Initialize parameters.

        Args:
            body (str): text.
            author (str): author name.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return string of body and author."""
        return f"{self.body} - {self.author}"
