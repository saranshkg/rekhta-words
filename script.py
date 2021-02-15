import os.path
import requests
from bs4 import BeautifulSoup as bs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = "https://rekhtadictionary.com/"

r = requests.get(url)
soup = bs(r.text, "html.parser")

#print(soup)

#Get daily word and its corresponding meaning

daily_word = soup.findAll("div", {"class": "rdDailywordBlok"})[0].find('span').contents[0]
daily_word_meaning = soup.findAll("div", {"class": "rdDailymeaningBlock"})[0].find('h3').contents[0]
# print(daily_word)
# print(daily_word_meaning)

with open(os.path.join(BASE_DIR, "rekhta-words.txt"), "a") as f:
	f.write(daily_word + " = " + daily_word_meaning + "\n")


# Loop over trending words and get their corresponding meanings

trending_word_cards = soup.findAll("div", {"class": "rdtrndWrd"})

# print(len(trending_word_cards))

for i in range(0, len(trending_word_cards)):
	trending_word = soup.findAll("div", {"class": "rdtrndWrd"})[i].find('h3').contents[0]
	trending_word_meaning = soup.findAll("p", {"class": "rdSimilarmeaning"})[i].contents[0]

	# print(trending_word)
	# print(trending_word_meaning)

	with open(os.path.join(BASE_DIR, "rekhta-words.txt"), "a") as f:
		f.write(trending_word + " = " + trending_word_meaning + "\n")