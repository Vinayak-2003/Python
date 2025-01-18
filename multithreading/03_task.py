import threading
import requests
import time


def download_file(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    
    
    
if __name__ == "__main__":
    urls = [
        "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fonlinetestcase.com%2Fwp-content%2Fuploads%2F2023%2F06%2F1-mb.xlsx&wdOrigin=BROWSELINK",
        "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fonlinetestcase.com%2Fwp-content%2Fuploads%2F2023%2F06%2F1-mb.xlsx&wdOrigin=BROWSELINK",
        "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fonlinetestcase.com%2Fwp-content%2Fuploads%2F2023%2F06%2F1-mb.xlsx&wdOrigin=BROWSELINK"
    ]
    filenames = ["file_1.xlsx", "file_3.xlsx", "file_2.xlsx"]
    
    threads = []
    
    start = time.time()
    for url, filename in zip(urls, filenames):
        time.sleep(2)
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()
        # download_file(url, filename)
    end = time.time()
    
    print("______________end-start", end-start)

print("All files are downloaded successfulle !!")