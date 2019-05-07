Daw Myu
-------
Python script that extracts text from a set of images and writes them into text file (organized by page). <br />
Intended as a tool to assist in the translation of text in images.


Getting Started
---------------
When executing this script, users must provide three arguments in this order

1| The path to the directory that holds the relevant images <br />
2| The name of the resultant text file <br />
3| The Google API key (Google account required, sign up here -- https://cloud.google.com/vision/docs/ocr)

Example: <br />
    python main.py [Folder path] [Text file name] [Google API key]

Prerequisites
-------------
Windows users might want to add Python to their PATH


Built With
----------
Google Optical Character Recognition API (https://cloud.google.com/vision/docs/ocr) <br />
Requests: HTTP for Humans (https://2.python-requests.org/en/master/)


License
-------
This project is licensed under the MIT License
