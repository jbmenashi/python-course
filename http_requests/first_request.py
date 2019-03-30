import requests
import random

def api_request():
   msg = input("What kind of joke do you want? ")
   url = 'http://icanhazdadjoke.com/search'
   response = requests.get(url, headers={ "Accept" : "application/json" }, params={ "term": msg })
   results = response.json()['results']
   if results:
      print(random.choice(results)['joke'])
   else:
      print("No jokes for that search term!")

api_request()