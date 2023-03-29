import argparse
from download_songs import download_songs
from extract_urls import extract_urls
from get_pages import get_pages

from url_validation import UrlValidationResult, get_error_message, validate_url

parser = argparse.ArgumentParser(description='Download music from the Free Music Archive')
parser.add_argument('url', type=str, help='URL of the webpage to download music from')
parser.add_argument('output_dir', type=str, help='Output directory for downloaded songs')

args = parser.parse_args()
url = args.url
output_dir = args.output_dir

url_validation_result = validate_url(url)
if url_validation_result != UrlValidationResult.VALID:
    print(get_error_message(url_validation_result))
    exit()

print("Fetching pages...")
pages = get_pages(url)

print("Extracting URLs...")
urls = extract_urls(pages)

print("Downloading songs...")
download_songs(urls, output_dir)

print("Done!")
