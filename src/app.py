"""Run flask server."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine.MemeGenerator import MemeGenerator as MemeEngine
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(list(imgs))
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    try:
        response = requests.get(image_url)
        tmp_path = random.getrandbits(64)
        tmp = f"./{tmp_path}.jpg"

        with open(tmp, 'wb') as img:
            img.write(response.content)

        path = meme.make_meme(tmp, body, author)

        os.remove(tmp)

        return render_template('meme.html', path=path)
    except Exception as error:
        print(error)
        return render_template('meme-error-page.html')


if __name__ == "__main__":
    app.run()
