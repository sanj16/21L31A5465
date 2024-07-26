import requests
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

third_party_api_urls = {
    'e': "http://20.244.56.144/test/even"
}

def fetch_numbers(url):
    try:
        logging.debug(f"Fetching numbers from URL: {url}")
        response = requests.get(url, timeout=0.5)
        response.raise_for_status()
        data = response.json()
        logging.debug(f"Response JSON: {data}")
        numbers = data.get('numbers', [])
        logging.debug(f"Extracted numbers: {numbers}")
        return numbers
    except (requests.RequestException, ValueError) as e:
        logging.error(f"Error fetching numbers: {e}")
        return []

if __name__ == '__main__':
    url = third_party_api_urls['e']
    numbers = fetch_numbers(url)
    print(f"Fetched numbers: {numbers}")
