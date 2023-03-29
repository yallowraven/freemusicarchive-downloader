# Free Music Archive Downloader

This is a command-line tool for downloading music from the Free Music Archive (https://freemusicarchive.org). The script allows you to download songs, extract metadata, and prune songs with missing metadata.

## Features

- Download songs from a specified FMA URL
- Option to log each downloaded song
- Extract metadata from downloaded songs
- Prune songs with missing metadata

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries: ```pip install -r requirements.txt```

## Usage

```bash
python ./main.py <url> <output_dir> [--silent] [--meta] [--prune-no-meta]

<url>: URL of the webpage to download music from
<output_dir>: Output directory for downloaded songs
--silent: Do not log each downloaded song
--meta: Extract metadata from downloaded songs
--prune-no-meta: Prune songs with missing metadata
```

## Example

To download all songs from the "Blues" collection on the Free Music Archive and extract metadata for each song without pruning:
```
python download.py https://freemusicarchive.org/genre/Blues <output_dir> --meta
```