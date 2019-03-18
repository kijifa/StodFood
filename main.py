import pycurl
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import pytesseract


page_folder = './Pages/'
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\'


def main():

    #puzzlesalad()
    chemicka()

    return


def chemicka():

    url = 'http://www.mojejidelnakb.cz/cs/jidelni-listek/jidelni-listek-tento-tyden.html'

    week = download_page(url,'chemicka.html')

    soup = BeautifulSoup(week,'html.parser')
    menu_url = soup.find('div',{'class':'odsazeni'}).find('img')
    img_src = menu_url.get('src')
    menu_link = 'http://www.mojejidelnakb.cz'+img_src

    img_week_menu = download_file(menu_link,'chemicka.png')

    print(menu_url)
    print(img_src)
    print(menu_link)

    print(pytesseract.image_to_string(Image.open(page_folder+'chemicka.png'),lang='ces'))

    return


def puzzlesalad():

    url = 'https://puzzlesalads.cz/dashboard/provozovna/?idp=4'

    page = download_page(url,'puzzle.html')

    #print(page)

    soup = BeautifulSoup(page,'html.parser')
    daily = soup.find('div',{'class': 'about-1 m-t-20'}).getText()
    daily = daily.strip()

    print(daily)

    f = open('Menu.txt','w+')
    f.write(daily)
    f.close()

    return


def remove_ws(variable):




    return output


def download_page(url: str,name):
    buffer = BytesIO()

    c = get_curl(url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    httpcode = buffer.getvalue()
    httpcode = (httpcode.decode('windows-1250', 'ignore'))
    #httpcode = httpcode.decode('utf-8', 'ignore')

    f = open(page_folder+name, 'w')
    f.write(httpcode)
    f.close()

    return httpcode


def download_file(url: str,name):

    c = get_curl(url)
    with open(page_folder+name,'wb') as file:
        c.setopt(c.WRITEFUNCTION,file.write)
        c.perform()
    c.close()

    return


def get_curl(url: str):
    """
    Funkce vrací Curl connector nastavený pro použití v KB
    :argument url: URL stahovaného souboru
    :return: Curl objekt
    """
    c = pycurl.Curl()
    # c.setopt(pycurl.VERBOSE, True)
    c.setopt(pycurl.PROXY, "vsproxy.kb.cz")
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    c.setopt(pycurl.PROXYPORT, 8080)
    c.setopt(pycurl.FOLLOWLOCATION, 1)  # Povolit přesměrování URL
    c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
    c.setopt(pycurl.PROXYAUTH, pycurl.HTTPAUTH_NTLM)
    c.setopt(pycurl.PROXYUSERNAME, '')
    c.setopt(pycurl.PROXYPASSWORD, '')
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.COOKIEFILE, 'cookie.txt')
    c.setopt(pycurl.COOKIEJAR, 'cookie.txt')
    return c


if __name__ == "__main__":
    # execute only if run as a script
    main()
