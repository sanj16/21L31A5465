from flask import Flask, jsonify, request
import requests
from collections import deque
import time

app = Flask(__name__)

WINDOW_SIZE = 10
third_party_api_url = "http://third-party-server.com/api/numbers/{type}"