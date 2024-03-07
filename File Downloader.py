import requests
from tqdm import tqdm
from urllib.parse import urlparse
import os
def file_extension(url):
  return os.path.splitext(urlparse(url).path)[1]
url=input("Enter the url and press enter : ")
r=requests.get(url, stream=True)
total_size= int(r.headers.get('content-length', 0))
block_size = 1024
progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
with open('downloaded_file'+file_extension(url),'wb') as f:
  for data in r.iter_content(block_size):
    progress_bar.update(len(data))
    f.write(data)
progress_bar.close()
print("Download Completed!!")
if total_size!= 0 and progress_bar.n != total_size:
  print("ERROR, something went wrong")