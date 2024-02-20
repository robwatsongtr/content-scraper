from Scraper import Scraper

if __name__ == "__main__":

    url = "https://techcrunch.com/2022/05/12/sample-series-a-pitch-deck-dutch/"
    scraper = Scraper(url)
    data = scraper.scrape_page()

    # print(data)

    with open("output.html", "w") as file:
        file.write(data)

    print("Data has been saved to output.html file.")

    