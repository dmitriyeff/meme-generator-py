## MEME-GENERATOR
Multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Prepare local env
1. `pip3 install -r requirements.txt` in the root dir
2. make sure you have xpdf on your machine:
	For Mac, we suggest that you use Homebrew:
	If you don't already have it, install use the command provided here to install Homebrew: https://brew.sh/. After installing, read the last few lines that it outputs in your CLI—it may provide additional commands that you can run to add Homebrew to PATH.
	Once Homebrew is installed, simply run `brew install xpdf` in the terminal.
	For Windows, you'll need to:
	Download the Windows command-line tools from the xpdf website.
	Unzip the files in a location of your choice.
	Get the full file path to the folder named bin32 (if you have a 32-bit machine) or bin64 (if you have a 64-bit machine).
	Add this path to the Path environment variable. This will allow you to use the xpdf command from the command line. If you've never done this before, check out this Stack Overflow post on how to add a folder to the Path environment variable.
	For Linux, you can use Homebrew (as shown above for Mac) or apt-get to install (simply enter sudo apt-get install -y xpdf in your command line interface).


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
3. open the host on which app is running: http://127.0.0.1:5000

