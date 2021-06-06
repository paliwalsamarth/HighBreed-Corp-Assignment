import bs4
import requests


def get_keywords(url):
    # sending the request
    response = None
    try:
        response = requests.get(url)
    except:
        return None

    if response.status_code == 200:
        # parsing the response
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        desc = soup.find("meta", {"name": "description"})
        og_desc = soup.find("meta", {"property": "og:description"})
        keywords = soup.find("meta", {"name": "keywords"})

        desc = str(None) if not desc else str(desc["content"])
        og_desc = str(None) if not og_desc else str(og_desc["content"])
        keywords = str(None) if not keywords else str(keywords["content"])

        allKeywords = desc.lower() + " " + og_desc.lower() + " " + keywords.lower()

        bad_chars = [";", ":", "!", "*", "|", ".", ",", "-"]

        for i in bad_chars:
            allKeywords = allKeywords.replace(i, "")

        allKeywords.strip()
        allKeywords = set(allKeywords.split())

        allKeywords = allKeywords - set(["none", " "])
        # print(allKeywords)
        return list(allKeywords)
    else:
        return None
