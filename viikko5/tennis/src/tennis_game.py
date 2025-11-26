class TennisGame:
    SCORES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }


    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        self.scores[player_name] += 1

    def get_score(self):
        if self.scores_even():
            if self.scores[self.player1_name] >= 3:
                return "Deuce"
            else:
                return self.SCORES[self.scores[self.player1_name]] + "-All"
        elif self.score_over_thirty():
            adv_player = self.advantage_of()

            if self.score_difference() >= 2:
                return f"Win for {adv_player}"
            else:
                return f"Advantage {adv_player}"
        else:
            return f"{self.SCORES[self.scores[self.player1_name]]}-{self.SCORES[self.scores[self.player2_name]]}"
    
    def scores_even(self):
        return self.score_difference() == 0

    def score_difference(self):
        return abs(self.scores[self.player1_name] - self.scores[self.player2_name])
    
    def advantage_of(self):
        if self.scores[self.player1_name] > self.scores[self.player2_name]:
            return self.player1_name
        return self.player2_name
    
    def score_over_thirty(self):
        if self.scores[self.player1_name] >= 4 or self.scores[self.player2_name] >= 4:
            return True
        return False
    