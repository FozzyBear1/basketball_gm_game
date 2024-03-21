from player import Player
from team import Team
import random

class Game:

    def __init__(self, away_team, home_team,):
        self.away_team = away_team
        self.home_team = home_team
        self.score_away = 0
        self.score_home = 0
        self.winner = None
        self.loser = None

    def simulate_game(self):
        strength_away = Team.get_team_overall(self.away_team)
        strength_home = Team.get_team_overall(self.home_team) + 2

        self.score_away= int(strength_away * random.uniform(0.9, 1.1))
        self.score_home = int(strength_home * random.uniform(0.9, 1.1))

        if self.score_away == self.score_home:
            self.score_home += 1

        if self.score_away > self.score_home:
            self.winner = self.team1
        else:
            self.winner = self.home_team

    def get_game_summary(self):
        if self.winner is None:
            return "Game is tied or hasn't been played yet."
        else:
            summary = f"Winner: {self.winner.get_name()}\n"
            summary += f"Score: {self.team1.get_name()} {self.score_team1} - {self.score_team2} {self.team2.get_name()}\n"
            # Add more detailed stats if necessary
            return summary