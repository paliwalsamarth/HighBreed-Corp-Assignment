# importing the module
import bs4
import requests


def get_android_app_info(id):
    # URL
    URL = f"https://play.google.com/store/apps/details?id={id}"

    # sending the request
    response = requests.get(URL)

    # default context
    context = {
        "status": "fail",
        "message": "Invalid App ID",
    }

    if response.status_code == 200:
        # parsing the response
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # scraping details
        icon = soup.find("img", {"itemprop": "image"})["src"]

        name = soup.find("h1", {"itemprop": "name"}).find_all("span")[0].text

        dev = soup.find("a", {"class": "hrTbp R8zArc"})
        dev_name = dev.text
        dev_link = "https://play.google.com" + str(dev["href"])

        desc = soup.find("div", {"jsname": "sngebd"}).text
        desc = (desc[:200] + "...") if len(desc) > 200 else desc

        nOfDown = soup.findAll("span", {"class": "htlgb"})
        nOfDown = nOfDown[4].div.span.text
        nOfReview = soup.find("span", {"class": "AYi5wd TBRnV"}).span.text
        rating = soup.find("div", {"class": "BHMmbe"}).text

        context = {
            "status": "success",
            "message": "App Found !",
            "icon": icon,
            "name": name,
            "dev_name": dev_name,
            "dev_link": dev_link,
            "desc": desc,
            "nOfDown": nOfDown,
            "nOfReview": nOfReview,
            "rating": rating,
        }

    return context


def get_apple_app_info(id, name):
    # URL
    URL = f"https://apps.apple.com/in/app/{name}/{id}"
    # print("url = ", URL)

    # default context
    context = {
        "status": "fail",
        "message": "Invalid App ID or Name",
    }

    # sending the request
    response = requests.get(URL)
    # print(response)
    if response.status_code == 200:

        # parsing the response
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # scraping details
        icon = (soup.find("source", {"class": "we-artwork__source"})["srcset"]).split()[
            0
        ]

        name = soup.find(
            "h1", {"class": "product-header__title app-header__title"}
        ).text.split()
        name = " ".join(name[:-1])

        dev = soup.find(
            "h2", {"class": "product-header__identity app-header__identity"}
        ).a
        dev_name = dev.text.strip()
        dev_link = dev["href"]

        desc = soup.find("div", {"class": "section__description"}).div.div.text.strip()
        desc = (desc[:200] + "...") if len(desc) > 200 else desc

        # nOfDown = "Not in app store, don't show this in card"
        nOfReview = soup.find(
            "div", {"class": "we-customer-ratings__count small-hide medium-show"}
        ).text.split()[0]
        rating = soup.find(
            "span", {"class": "we-customer-ratings__averages__display"}
        ).text

        context = {
            "status": "success",
            "message": "App Found !",
            "icon": icon,
            "name": name,
            "dev_name": dev_name,
            "dev_link": dev_link,
            "desc": desc,
            # 'nOfDown': nOfDown,
            "nOfReview": nOfReview,
            "rating": rating,
        }
    return context
