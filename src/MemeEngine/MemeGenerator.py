"""
Raises: unexpected error.

Returns:
{str}: path to saved image.
"""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeGenerator:
    """Image - quote generator class."""

    def __init__(self, output_dir):
        """Init output directory.

        Args:
            output_dir (str): path to output directory.
        """
        self.out_path = output_dir

    def make_meme(
        self,
        img_path: str,
        body: str,
        author: str,
        width=500
    ) -> str:
        """Create a Postcard With a Text Greeting.

        Arguments:
            img_path {str} -- the file location for the input image.
            body {str} -- quote
            author {str} -- author of the quote
            width {int} -- maximum width
        Returns:
            str -- the file path to the output image.
        """
        try:
            with Image.open(img_path) as img:
                im = img.getdata()
                width, height = im.size
                pixels = width * height

                if (pixels > 500):
                    """Resize an image."""
                    size = width, height
                    img = img.resize(size)

                draw = ImageDraw.Draw(img)
                font = ImageFont.load_default()
                draw.text(
                    (random.randint(0, width),
                     random.randint(0, height)),
                    f"{body} - {author}",
                    font=font,
                    fill='white'
                )

                image_name = random.getrandbits(64)
                img.save(f"{self.out_path}/{image_name}.jpg")

                return f"{self.out_path}/{image_name}.jpg"
        except Exception as error:
            raise Exception(error)
