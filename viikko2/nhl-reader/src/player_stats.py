class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [p for p in self.players if p.nationality == nationality]
        return sorted(filtered_players, key=lambda x: x.goals+x.assists, reverse = True)

    def top_goals_by_nationality(self, nationality):
        filtered_players = [p for p in self.players if p.nationality == nationality]
        return sorted(filtered_players, key=lambda x: x.goals, reverse = True)
