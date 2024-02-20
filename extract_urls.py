from Scraper import Scraper

if __name__ == "__main__":

    file_path = 'url_links.txt'
    urls_list = Scraper.extract_urls_from_text_file(file_path)

    with open("urls-list.py", "w") as file:
        for item in urls_list:
            file.write("'" + str(item) + "'" + "," + '\n')

    print("done")
    