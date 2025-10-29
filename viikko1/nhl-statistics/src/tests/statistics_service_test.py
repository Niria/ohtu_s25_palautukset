import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_valid_player(self):
        self.assertEqual(self.stats.search("Lemieux").name, "Lemieux")

    def test_search_invalid_name_returns_nothing(self):
        self.assertIsNone(self.stats.search("Null"))

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")

        self.assertEqual(len(team_players), 3)

        for p in team_players:
            self.assertIn(p.name, ["Semenko", "Kurri", "Gretzky"])

    
    def test_top_returns_top_3_players(self):
        # The top method currently returns n+1 top players, so n=2
        top_players = self.stats.top(2)
        names = [p.name for p in top_players]

        self.assertEqual(len(top_players), 3)
        self.assertListEqual(names, ["Gretzky", "Lemieux", "Yzerman"])
