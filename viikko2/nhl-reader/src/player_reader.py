import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    def get_players(self):
        response = requests.get(self.url, timeout=10).json()
        players = [Player(p) for p in response]

        return players
