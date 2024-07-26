from flask import Flask, jsonify
from collections import deque
import requests
import time
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

WINDOW_SIZE = 10

# Third-party API URLs
third_party_api_urls = {
    'p': "http://20.244.56.144/test/primes",
    'f': "http://20.244.56.144/test/fibo",
    'e': "http://20.244.56.144/test/even",
    'r': "http://20.244.56.144/test/rand"
}

# Bearer token for authorization
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIxOTc0MzM1LCJpYXQiOjE3MjE5NzQwMzUsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImQ0ZjM3M2RjLTljY2UtNDBlMC04MTkxLWM3NmI1MDk1ODI2NyIsInN1YiI6InNhbmphbmEubWFuZGFyYXB1QGdtYWlsLmNvbSJ9LCJjb21wYW55TmFtZSI6IlZpZ25hbiBJbnN0aXR1dGUgIiwiY2xpZW50SUQiOiJkNGYzNzNkYy05Y2NlLTQwZTAtODE5MS1jNzZiNTA5NTgyNjciLCJjbGllbnRTZWNyZXQiOiJvVkJGZGRCZFh4YUl0a2FJIiwib3duZXJOYW1lIjoiU2FuamFuYSBNYW5kYXJhcHUiLCJvd25lckVtYWlsIjoic2FuamFuYS5tYW5kYXJhcHVAZ21haWwuY29tIiwicm9sbE5vIjoiMjFMMzFBNTQ2NSJ9.gVW-aRKjiKqt61bKK0w42NU84fXgKU9nBabhHDvm4d8"

# Initialize a deque with a fixed window size
number_window = deque(maxlen=WINDOW_SIZE)

def fetch_numbers(url):
    try:
        headers = {
            'Authorization': f'Bearer {BEARER_TOKEN}'
        }
        logging.debug(f"Fetching numbers from URL: {url}")
        response = requests.get(url, headers=headers, timeout=0.5)
        response.raise_for_status()
        data = response.json()
        logging.debug(f"Response JSON: {data}")
        numbers = data.get('numbers', [])
        logging.debug(f"Extracted numbers: {numbers}")
        return numbers
    except (requests.RequestException, ValueError) as e:
        logging.error(f"Error fetching numbers: {e}")
        return []

def calculate_average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

@app.route('/numbers/<numberid>', methods=['GET'])
def get_numbers(numberid):
    if numberid not in third_party_api_urls:
        return jsonify({"error": "Invalid number ID"}), 400

    start_time = time.time()
    prev_state = list(number_window)

    url = third_party_api_urls[numberid]
    numbers = fetch_numbers(url)
    if not numbers:
        logging.debug("No numbers received or extracted.")
    for number in numbers:
        if number not in number_window:
            number_window.append(number)

    curr_state = list(number_window)
    avg = calculate_average(curr_state)

    if time.time() - start_time > 0.5:
        return jsonify({"error": "Request timed out"}), 500

    response = {
        "windowPrevState": prev_state,
        "windowCurrState": curr_state,
        "numbers": numbers,
        "avg": avg
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=9876, debug=True)
