class Player:
    def __init__(self, player):
        self.name = player['name']
        self.nationality = player['nationality']
        self.assists = player['assists']
        self.goals = player['goals']
        self.team = player['team']
        self.games = player['games']
        self.id =  player['id'] if 'id' in player.keys() else None

    def __str__(self):
        points = self.goals + self.assists
        return f"{self.name:25}{self.team:20}{self.goals:2} + {self.assists:2} = {points:2}"

    def games_played(self):
        return self.games
