import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        players = [Player(p) for p in requests.get(self.url).json()]
        
        return players
