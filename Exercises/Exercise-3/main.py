import gzip
import logging
import requests
from urllib.parse import urlparse

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_gz_file_in_memory(bucket, key):
    """Tải file .gz từ HTTP và trả về nội dung giải nén trong memory."""
    try:
        url = f"https://data.commoncrawl.org/{key}"
        logger.info(f"Tải file từ URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        decompressed = gzip.decompress(response.content).decode('utf-8')
        return decompressed
    except Exception as e:
        logger.error(f"Lỗi khi tải hoặc giải nén file: {e}")
        raise

def get_first_uri(file_content):
    """Lấy URI từ dòng đầu tiên của file."""
    try:
        lines = file_content.splitlines()
        if not lines:
            raise ValueError("File rỗng")
        return lines[0].strip()
    except Exception as e:
        logger.error(f"Lỗi khi lấy URI: {e}")
        raise

def download_and_stream_file(uri):
    """Tải file .gz từ URI qua HTTP, giải nén và in từng dòng."""
    try:
        url = f"https://data.commoncrawl.org/{uri}"
        logger.info(f"Tải file từ URI: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Giải nén file gzip khi đọc stream
        with gzip.GzipFile(fileobj=response.raw) as gz_file:
            for line in gz_file:
                print(line.decode('utf-8').strip())

    except Exception as e:
        logger.error(f"Lỗi khi tải hoặc in file từ URI: {e}")
        raise


def main():
    try:
        # Bước 1 & 2: Tải và giải nén file wet.paths.gz trong memory
        bucket = 'commoncrawl'
        key = 'crawl-data/CC-MAIN-2025-13/wet.paths.gz'
        file_content = download_gz_file_in_memory(bucket, key)

        # Bước 3: Lấy URI từ dòng đầu tiên
        first_uri = get_first_uri(file_content)

        # Bước 4 & 5: Tải file từ URI và in từng dòng
        download_and_stream_file(first_uri)
    except Exception as e:
        logger.error(f"Lỗi trong main: {e}")
        raise

if __name__ == "__main__":
    main()
