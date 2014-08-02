# Dommert's Flask-Rum [Version 0.1.1]
# __init__.py
from flask import Flask
from main import app
import rum_config

app = Flask(__name__)
