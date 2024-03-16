import random
from team import Team

class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.result = None  # 'home' for home team win, 'away' for away team win, 'draw' for draw

    def simulate_match(self):
        # Example of a simple match simulation based on team strength
        home_advantage = 1.05  # Assuming home team has a slight advantage
        home_strength = self.home_team.strength * home_advantage
        away_strength = self.away_team.strength

        # Calculate match outcome probabilities
        draw_probability = 0.2  # Assuming 20% chance of a draw regardless of team strength
        home_win_probability = (home_strength / (home_strength + away_strength)) * (1 - draw_probability)
        away_win_probability = (away_strength / (home_strength + away_strength)) * (1 - draw_probability)

        # Determine match outcome
        outcome = random.choices(['home', 'away', 'draw'],
                                 weights=[home_win_probability, away_win_probability, draw_probability],
                                 k=1)[0]

        self.result = outcome

    def get_result(self):
        return self.result