
"""
FILENAME:               app.py
AUTHOR:                 Medi Assumani
DESCRIPTION:            Entry point of the Stswie Griffin Tweet Generator that containts
                        the flask server and connected with needed internal modules.
"""

from flask import Flask
import sys
sys.path.insert(0,'./scripts')
from file_opener import read_file
from histogram_generator import generate_histogram
from sentence import generate_sentence

app = Flask(__name__)

# Route : Index
@app.route('/')
def index():
    file_path = 'stewi_griffin_scripts.txt'
    text = read_file(file_path)
    histogram = generate_histogram(text)

    return generate_sentence(histogram, 15)
