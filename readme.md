## MEME-GENERATOR
Multimedia application to dynamically generate memes, including an image with an overlaid quote.

## How to generate an image with the quote
1. `git clone https://github.com/dmitriyeff/meme-generator-py.git`
2. `cd src`
3. `python3 meme.py`

## How to generate custom images with the quotes
If you want to generate your own images, you can use command line:

`python3 meme.py [--path PATH] [--body BODY] [--author AUTHOR]`

Example: `python3 meme.py --path "_data/photos/dog/xander_1.jpg" --body "Finish" --author "Denis"`

## How to run flask server
1. `cd src`
2. `python3 ./app.py `

