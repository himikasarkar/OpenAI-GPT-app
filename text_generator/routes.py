from text_generator import generator
from flask import Blueprint, render_template, request, redirect
from .generator import ai

generator = Blueprint('generator',__name__)

@generator.route('/')
def index():
    return render_template('index.html')

@generator.route('/analyze', methods=['POST'])
def analyze():
    title = request.form['title']
    text = ai.generate_text(title)

    return render_template('index.html', text=text)