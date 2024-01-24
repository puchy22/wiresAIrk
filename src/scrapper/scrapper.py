import requests
from bs4 import BeautifulSoup
import os

wireshark_samples = 'https://wiki.wireshark.org/SampleCaptures'

response = requests.get(wireshark_samples)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

# Filter links that contain a "href" with a ".cap", ".pcap" or "pcappng" extension

capture_downloads = []

for link in links:
    try:
        href = link['href']

        if href.endswith('.cap') or href.endswith('.pcap') or href.endswith('.pcapng'):
            capture_downloads.append('https://wiki.wireshark.org' + href)
    except:
        pass

# Create data folder if it doesn't exist in the root of the project

if not os.path.exists(os.path.join(os.getcwd(), 'data')):
    os.makedirs(os.path.join(os.getcwd(), 'data'))

# Download samples in data folder in the root of the project

for download in capture_downloads:
    response = requests.get(download)
    filename = download.split('/')[-1]
    print('Downloading ' + filename)
    with open(os.path.join(os.getcwd(), 'data', filename), 'wb') as f:
        f.write(response.content)

