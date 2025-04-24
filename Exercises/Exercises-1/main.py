import os
import requests
import zipfile
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# Danh sách các URL cần tải xuống
URLS = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]

def create_downloads_dir():
    """Tạo thư mục downloads nếu chưa tồn tại"""
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        print("✅ Đã tạo thư mục downloads")

def download_file(url):
    """Tải xuống một file từ URL nếu chưa có"""
    try:
        filename = os.path.basename(urlparse(url).path)
        filepath = os.path.join('downloads', filename)

        if os.path.exists(filepath):
            print(f"⚠️ {filename} đã tồn tại, bỏ qua...")
            return filepath

        print(f"⬇️ Đang tải xuống {filename}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"✅ Đã tải xong {filename}")
        return filepath
    except Exception as e:
        print(f"❌ Lỗi khi tải {url}: {str(e)}")
        return None

def extract_zip(filepath):
    """Giải nén file zip và xóa sau khi giải nén"""
    if not filepath or not filepath.endswith('.zip'):
        return

    try:
        print(f"📦 Đang giải nén {filepath}...")
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall('downloads')
        os.remove(filepath)
        print(f"🗑️ Đã xóa file zip {filepath}")
    except Exception as e:
        print(f"❌ Lỗi khi giải nén {filepath}: {str(e)}")

def download_and_extract(url):
    """Tải và giải nén một file"""
    filepath = download_file(url)
    extract_zip(filepath)

def main():
    create_downloads_dir()
    print("🚀 Bắt đầu tải xuống song song")
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_and_extract, URLS)

if __name__ == "__main__":
    main()
