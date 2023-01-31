#!/usr/bin/env python3
"""Task 0. Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

@app.route('/')
def home():
    render_template("0-index.html")
#babel = Babel(app)
