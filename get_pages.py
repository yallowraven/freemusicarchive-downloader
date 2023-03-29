import argparse
import requests

parser = argparse.ArgumentParser(description='Fetch the HTML contents of a webpage')
parser.add_argument('url', type=str, help='URL of the webpage to fetch')

args = parser.parse_args()

url = args.url
response = requests.get(url)

if response.status_code != 200:
    print("Failed to retrieve HTML content")

content = response.content