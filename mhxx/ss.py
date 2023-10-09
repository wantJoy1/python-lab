import requests
from bs4 import BeautifulSoup

# const
sharpness: dict[str, float] = {
    "blue": 1.20,
    "white": 1.32,
    "purple": 1.39
}

critical_eye: dict[int, int] = {
    1: 10,
    2: 20,
    3: 30
}

weakness_exploit = 50

def response():
    url = "http://wiki.mhxg.org/data/2702.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
    return soup

# res = response().find_all('')
print(response())
