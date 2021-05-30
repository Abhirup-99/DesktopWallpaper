from bs4 import BeautifulSoup as soup
import shutil
import requests
import time
import os
from random import randint

download_direct = os.path.join(os.path.dirname(__file__), "images")


def scrape(term=""):
    try:
        # checks if folder is already there
        if not os.path.exists(download_direct):
            os.makedirs(download_direct)
        else:
            shutil.rmtree(download_direct)
            os.makedirs(download_direct)

        # assumes there are 10 pages for a search result
        page = randint(1, 10)
        if term != "":
            url = "https://www.wallpaperflare.com/search?wallpaper={}&page={}".format(
                term, page
            )
        else:
            url = "https://www.wallpaperflare.com/index.php?c=main&m=portal_loadmore&page={}".format(
                page
            )

        page_soup = soup(requests.get(url).content, "html5lib")

        imgs = page_soup.findAll("li", {"itemprop": "associatedMedia"})

        # gets a random image from the page
        img_random_number = randint(1, len(imgs) - 1)
        img_page = (
            imgs[img_random_number].find("a", {"itemprop": "url"})["href"]
            + "/download/"
        )
        img_url = get_url(img_page)
        download_file(img_url)
        return "success"
    except Exception:
        return "error"


def get_url(img_page):
    page_soup = soup(requests.get(img_page).content, "html.parser")
    return page_soup.find("img", {"id": "show_img"})["src"]


def download_file(url):
    local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        with open(os.path.join(download_direct, local_filename), "wb") as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename
