import os
from Scraper import Scraper
from urls_list import urls_list
from urls_list2 import urls_list2

if __name__ == "__main__":
    subdir_name = "scraped_urls"

    if not os.path.exists(subdir_name):
        os.makedirs(subdir_name)
    
    for url in urls_list:
        scraper = Scraper(url)
        data = scraper.scrape_page()

        description = url.split('/')[-2]
        file_name = f"{description}.html"
        file_path = os.path.join(subdir_name, file_name)

        with open(file_path, "w") as file:
            file.write(data)

        print(f"{file_name} has been saved." )
    