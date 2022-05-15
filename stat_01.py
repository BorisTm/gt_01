import requests
from bs4 import BeautifulSoup

URL = "https://djinni.co/jobs/keyword-"
KEY_WORDS = ("qa-automation", "python", "golang", "javascript", "java", "qa")

try:
    for key in KEY_WORDS:
        page = requests.get(URL + key)
        soup = BeautifulSoup(page.content, "html.parser")
        print(key + ":", soup.select_one("span[class*=text-muted]").text)


except BaseException as err:
    print(f"Unexpected error: {err}, {type(err)}")
