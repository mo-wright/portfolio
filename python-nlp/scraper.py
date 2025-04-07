import bs4
import requests
import os

url = "http://www.textfiles.com/100/"

def get_files():
    r = requests.get(url)

    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    for item in soup.find_all('tr'):
        link = item.find('a')
        href = url + link['href']
        download_links(href)
    print("Download complete")


# finding names
    for a_href in soup.find_all("a", href=True):
        print(a_href["href"])

def download_links(href):
    # obtain filename by splitting url and getting last string
    file_name = href.split('/')[-1]
    print(file_name)
    print("Downloading file: " + file_name)

    r = requests.get(href, stream = True)

    workingDir = os.getcwd()
    print("current working directory: " + workingDir)
    fileDeposit = os.path.join(workingDir, 'computer', file_name)
    print(fileDeposit)

 # download started
    with open(fileDeposit, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            # ebb what's the chunk stuff for?
            # It's to "chunk" the contents we're scraping into manageable 1 MB units (= 1024 x 1024 bytes)
            # literally, "megabyte-sized chunks"
            if chunk:
                f.write(chunk)
                print("Downloaded " + file_name)

    return

# ebb: Basically the line below initiates the whole program, sets it in motion.
# On the line if __name__ == "__main__": ,
# see: https://medium.com/@j.yanming/debugging-from-main-to-main-in-python-fe2a9784b36
if __name__ == "__main__":
    get_files = get_files()