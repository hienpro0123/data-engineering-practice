import requests
import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    snap_shot = requests.get(url)
    raw_html = snap_shot.text
    soup = BeautifulSoup(raw_html, 'html.parser')

    rows = soup.find_all('tr')  # <-- mỗi hàng gồm 3 cột
    data = []

    for row in rows:
        tds = row.find_all('td')
        if len(tds) >= 3:
            href = tds[0].text.strip()
            time_ = tds[1].text.strip()
            size = tds[2].text.strip()
            data.append({
                "Name": href,
                "Last modified": time_,
                "Size": size
            })

    #luu vao file csv
    df = pd.DataFrame(data)
    df.to_csv('data.csv')


if __name__ == "__main__":
    main()
