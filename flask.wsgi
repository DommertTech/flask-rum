import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/dev/python/wsgi/flask-rum/")
from main import app as application