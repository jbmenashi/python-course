class Game:
   def __init__(self, home, away, score):
      self.home = home
      self.away = away
      self.score = score

   def matchup(self):
      return f"{self.away} vs {self.home}"


   def player(self, player):
      return f"{self.score} was the score and the MVP was {player}"


