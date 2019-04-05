class Baseball:
   def __init__(self, home, away, total):
      self.home = home
      self.away = away
      self.total = total

   def matchup(self):
      return f"{self.away} vs {self.home}"

   def short_matchup(self):
      return self.away.slice[:3]

   def player(self, player):
      return f"{self.total} has been delivered by {player}"