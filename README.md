# Ubuntu Image Fetcher

Ubuntu-Inspired Python Project: Mindfully Collecting Images from the Web

## Description

This tool is inspired by the Ubuntu philosophy: _"I am because we are."_ It allows you to fetch images from the web and organize them, showing respect for the global online community by handling errors gracefully and avoiding duplicates.

- **Community:** Connects to the wider web to collect shared images.
- **Respect:** Handles errors and respects the network and file system.
- **Sharing:** Organizes images for easy access and sharing.
- **Practicality:** A useful script for organizing images from URLs.

## Features

- Download a single image from a URL and save it to the `Fetched_Images` directory.
- Graceful error handling for network and file issues.
- Avoids duplicate downloads.
- Handles multiple URLs (challenge).
- Basic security checks before downloading files (challenge).
- Checks important HTTP headers (challenge).

## Requirements

- Python 3.x
- `requests` library

Install requirements (if needed):
```bash
pip install requests
```

## Usage

Run the script:

```bash
python ubuntu_image_fetcher.py
```

Follow the prompts to enter one or more image URLs.

## Example Output

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URLs (comma-separated): https://example.com/image1.jpg, https://example.com/image2.png
✓ Successfully fetched: image1.jpg
✓ Image saved to Fetched_Images/image1.jpg
✓ Successfully fetched: image2.png
✓ Image saved to Fetched_Images/image2.png

Connection strengthened. Community enriched.
```

## Ubuntu Principles

- **Community:** Connects to the web.
- **Respect:** Handles errors, avoids duplicates, checks headers.
- **Sharing:** Images organized for easy sharing.
- **Practicality:** Real-world usefulness.

## Challenge Features

See code comments for additional challenge solutions.

---

_A person is a person through other persons._ — Ubuntu philosophy