import argparse
import re
import requests

parser = argparse.ArgumentParser(description='Download music from the Free Music Archive')
parser.add_argument('url', type=str, help='URL of the webpage to download music from')

args = parser.parse_args()

url = args.url

if not url.startswith('https://freemusicarchive.org/'):
    print("URL must start with 'https://freemusicarchive.org/'")
    exit()

response = requests.get(url)

if response.status_code != 200:
    print("Failed to download music listings")
    exit()

page = response.content

if not re.search(r'<div class="play-item[^\n]*', page.decode()):
    print("Error: this is not a music listing page")
    exit()
