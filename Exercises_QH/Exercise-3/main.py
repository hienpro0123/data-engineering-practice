import boto3
import gzip
import io

def download_s3_file(bucket, key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    return response['Body'].read()

def stream_s3_file(bucket, key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    return response['Body'].iter_lines()

def main():
    bucket = 'commoncrawl'
    key = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'

    # 1. Tải file .gz vào bộ nhớ
    gz_data = download_s3_file(bucket, key)

    # 2. Giải nén trong bộ nhớ và đọc dòng đầu tiên
    with gzip.GzipFile(fileobj=io.BytesIO(gz_data)) as gz:
        first_path = gz.readline().decode('utf-8').strip()

    print(f"First path: {first_path}")

    # 3. Tải và in từng dòng từ file trong path đầu tiên
    lines = stream_s3_file(bucket, first_path)
    for line in lines:
        print(line.decode('utf-8'))

if __name__ == "__main__":
    print("🚀 Starting the script...")
    main()
