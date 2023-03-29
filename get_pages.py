import argparse
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
    print("Failed to download music")
    exit()

music = response.content
# Do something with the downloaded music

print("Music downloaded successfully")
