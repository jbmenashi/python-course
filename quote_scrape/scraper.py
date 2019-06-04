import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url = "http://quotes.toscrape.com/"
url = "/page/1"

while url:
   res = requests.get(f"{base_url}{url}")
   print("Now Scraping new Page")
   soup = BeautifulSoup(res.text, "html.parser")
   quotes = soup.find_all(class_="quote")
   for quote in quotes:
      all_quotes.append({
         "text":quote.find(class_="text").get_text(),
         "author":quote.find(class_="author").get_text(),
         "bio-link":quote.find("a")["href"]
      })
   next_btn = soup.find(class_="next")
   url = next_btn.find("a")["href"] if next_btn else None

quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote ")
print(quote["text"])
print(quote["author"])
guess = ""

while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
   guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses} ")
   if guess.lower() == quote["author"].lower():
      print("You Got It!")
      break
   remaining_guesses -= 1
   if remaining_guesses == 3:
      res = requests.get(f"{base_url}{quote['bio-link']}")
      soup = BeautifulSoup(res.text, 'html.parser')
      birthdate = soup.find(class_="author-born-date").get_text()
      birthplace = soup.find(class_="author-born-location").get_text()
      print(f"Here's a hint: The author was born in {birthplace} on {birthdate}")
   elif remaining_guesses == 2:
      print(f"Another hint: Their first name starts with {quote['author'][0]}")
   elif remaining_guesses == 1:
      print(f"One more hint: Their last name starts with {quote['author'].split()[1][0]}")
   else:
      print(f"Out of Guesses! It was {quote['author']}")

print("You Got It!")