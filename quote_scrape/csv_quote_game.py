import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com/"

def read_quotes(filename):
   with open(filename, "r") as file:
      csv_reader = DictReader(file)
      return list(csv_reader)

def start_game(quotes):
   quote = choice(quotes)
   remaining_guesses = 4
   print("Here's a quote ")
   print(quote["text"])
   print(quote["author"])
   guess = ""

   while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
      guess = input(
          f"Who said this quote? Guesses remaining: {remaining_guesses} ")
      if guess.lower() == quote["author"].lower():
         print("You Got It!")
         break
      remaining_guesses -= 1
      if remaining_guesses == 3:
         res = requests.get(f"{BASE_URL}{quote['bio-link']}")
         soup = BeautifulSoup(res.text, 'html.parser')
         birthdate = soup.find(class_="author-born-date").get_text()
         birthplace = soup.find(class_="author-born-location").get_text()
         print(
             f"Here's a hint: The author was born in {birthplace} on {birthdate}")
      elif remaining_guesses == 2:
         print(
             f"Another hint: Their first name starts with {quote['author'][0]}")
      elif remaining_guesses == 1:
         print(
             f"One more hint: Their last name starts with {quote['author'].split()[1][0]}")
      else:
         print(f"Out of Guesses! It was {quote['author']}")

   again = ''
   while again not in ('y', 'yes', 'n', 'no'):
      again = input("Would you like to play again? (Y/N)?")
   if again.lower() in ('yes', 'y'):
      print("Okay, let's do it!")
      return start_game(quotes)
   else:
      print("Okay goodbye")

quotes = read_quotes("quotes.csv")
start_game(quotes)
