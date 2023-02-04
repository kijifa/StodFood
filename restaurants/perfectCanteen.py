from scrape.scrape import wget_download_page
from scrape.scrape import convert_pdf
from scrape.scrape import save_txt

def perfect_canteen():
    url = "https://menu.perfectcanteen.cz/pdf/28/cz/price/a3"
    file_name = "perfect_canteen.pdf"

    canteen_file = wget_download_page(url, file_name)
    print(canteen_file)
    text = convert_pdf(canteen_file)
    print(text)
    save_txt("perfect_canteen.txt", text)




