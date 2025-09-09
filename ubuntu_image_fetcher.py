import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        # Generate a unique name based on URL hash if no filename in path
        filename = f"image_{hashlib.md5(url.encode()).hexdigest()}.jpg"
    return filename

def is_duplicate(filepath, content):
    if not os.path.exists(filepath):
        return False
    # Compare hashes to check for duplicates
    with open(filepath, "rb") as f:
        existing = f.read()
        return hashlib.md5(existing).hexdigest() == hashlib.md5(content).hexdigest()

def is_image_content_type(headers):
    content_type = headers.get('Content-Type', '')
    return content_type.startswith('image/')

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URLs (comma separated for multiple)
    url_input = input("Please enter image URL(s) (comma-separated for multiple): ")
    urls = [u.strip() for u in url_input.split(",") if u.strip()]
    
    os.makedirs("Fetched_Images", exist_ok=True)
    downloaded = set()

    for url in urls:
        try:
            # Security: Only allow HTTP/S URLs
            if not url.lower().startswith(("http://", "https://")):
                print(f"✗ Skipping non-http(s) URL: {url}")
                continue

            # Fetch with a user-agent header
            headers = {'User-Agent': 'UbuntuImageFetcher/1.0'}
            response = requests.get(url, timeout=10, headers=headers, stream=True)
            response.raise_for_status()

            # Challenge: Check content-type
            if not is_image_content_type(response.headers):
                print(f"✗ Not an image (Content-Type: {response.headers.get('Content-Type')}): {url}")
                continue

            filename = get_filename_from_url(url)
            filepath = os.path.join("Fetched_Images", filename)

            # Challenge: Prevent duplicate by filename and content
            content = response.content
            if filename in downloaded or is_duplicate(filepath, content):
                print(f"⏩ Duplicate skipped: {filename}")
                continue

            with open(filepath, 'wb') as f:
                f.write(content)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

            downloaded.add(filename)

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()