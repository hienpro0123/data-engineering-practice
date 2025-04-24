import boto3
import gzip
import shutil
import wget
import os


# Bucket: commoncrawl
# Key: crawl-data/CC-MAIN-2022-05/wet.paths.gz
# Concatenate the following URL with the file URL: https://data.commoncrawl.org/

def main():
    # S3 Bucket variables
    bucket_name = 'commoncrawl'
    key = 'crawl-data/CC-MAIN-2020-16/wet.paths.gz'
    s3 = boto3.resource('s3')

    # Creating directories
    if not os.path.exists('gzip_files'):
        os.makedirs('gzip_files')
        print('Directory "gzip_files" created')

    if not os.path.exists('path_files'):
        os.makedirs('path_files')
        print('Directory "path_files" created')

    if not os.path.exists('data_files'):
        os.makedirs('data_files')
        print('Directory "data_files" created')

    s3.Bucket(bucket_name).download_file(key, 'gzip_files/wet.paths.gz')

    with gzip.open('gzip_files/wet.paths.gz', 'rb') as gzip_obj:
        with open('path_files/wet.paths.txt', 'wb') as content:
            shutil.copyfileobj(gzip_obj, content)

    with open('path_files/wet.paths.txt', 'r') as data_file:
        url = f'https://data.commoncrawl.org/{list(data_file)[0]}'
        file_name = url[url.rfind('/') + 1:]
        wget.download(url, 'gzip_files/')

    with gzip.open('gzip_files/' + file_name.replace('\n', ''), 'rb') as f_gzip_file:
        with open('data_files/' + file_name.replace('.gz', '').replace('\n', ''), 'wb') as unzip_file:
            shutil.copyfileobj(f_gzip_file, unzip_file)

    pass


if __name__ == '__main__':
    main()
