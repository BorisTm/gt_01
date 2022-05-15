import requests
from bs4 import BeautifulSoup


def get_dj_stats():
    url = "https://djinni.co/jobs/keyword-"
    key_words = ("qa-automation", "python", "golang", "javascript", "java", "qa")
    res_dict = {}
    try:
        for key in key_words:
            page = requests.get(url + key)
            soup = BeautifulSoup(page.content, "html.parser")
            value = soup.select_one("span[class*=text-muted]").text
            res_dict[key] = value
    except BaseException as err:
        print(f"Unexpected error: {err}, {type(err)}")
    return res_dict


result = get_dj_stats()
print(result)
