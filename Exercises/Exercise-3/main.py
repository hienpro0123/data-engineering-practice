import requests
import gzip
from io import BytesIO
import sys

def main():
    try:
        # 1. Tải file gz đầu tiên
        base_url = "https://data.commoncrawl.org"
        wet_paths_url = f"{base_url}/crawl-data/CC-MAIN-2022-05/wet.paths.gz"
        
        print(f"Đang tải file: {wet_paths_url}")
        response = requests.get(wet_paths_url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        
        # 2. Giải nén và đọc file
        with gzip.GzipFile(fileobj=BytesIO(response.content)) as gz_file:
            first_line = gz_file.readline().decode('utf-8').strip()
            if not first_line:
                print("File rỗng hoặc không có dữ liệu")
                sys.exit(1)
            
            # 3. Tải file thứ hai
            second_file_url = f"{base_url}/{first_line}"
            print(f"Đang tải file: {second_file_url}")
            
            # Stream file để tiết kiệm bộ nhớ
            with requests.get(second_file_url, stream=True) as r:
                r.raise_for_status()
                with gzip.GzipFile(fileobj=BytesIO(r.content)) as gz_file2:
                    for line in gz_file2:
                        print(line.decode('utf-8').strip())
                        
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
