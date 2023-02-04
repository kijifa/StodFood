from scrape.scrape import wget_download_page


def perfect_canteen():
    url = "https://menu.perfectcanteen.cz/pdf/28/cz/price/a3"
    file_name = "perfect_canteen.pdf"

    file = wget_download_page(url, file_name)
    print(file)


