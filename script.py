import os.path
import requests
from bs4 import BeautifulSoup as bs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = "https://www.rekhta.org/urdudictionary"

r = requests.get(url)
soup = bs(r.text, "html.parser")

word = soup.findAll("div", {"class": "wordContainer"})[0].text.strip("\n")
meaning = soup.findAll("div", {"class": "engMeaning"})[0].h3.text

with open(os.path.join(BASE_DIR, "rekhta-words.txt"), "a") as f:
	f.write(word + " = " + meaning + "\n")
