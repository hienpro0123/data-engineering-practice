import requests
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def download_file(url, folder='downloads_url'):
    # Create downloads folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    try:
        # Get the file name from the URL
        file_name = url.split('/')[-1]
        file_path = os.path.join(folder, file_name)
        
        # Download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Save the file
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        
        print(f"Successfully downloaded {file_name}")
        return True
    
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")
        return False

def main():
    # Download each file in the list
    for uri in download_uris:
        download_file(uri)
    
    print("Download process completed.")

if __name__ == "__main__":
    main()