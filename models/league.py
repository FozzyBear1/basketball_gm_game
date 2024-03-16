from match import Match
from team import Team
import json

class League:
    def __init__(self, name, teams=None):
        self.name = name
        self.teams = teams if teams is not None else []
    
    def add_team(self, team):
        """Add a team to the league."""
        self.teams.append(team)
    
    def remove_team(self, team_name):
        """Remove a team from the league by name."""
        self.teams = [team for team in self.teams if team.name != team_name]
    
    def get_team_stats(self, team_name):
        """Get stats for a specific team by name."""
        for team in self.teams:
            if team.name == team_name:
                return team.stats
        return None
    
    def update_team_stats(self, team_name, win=False, lose=False, tie=False):
        """Update the stats for a specific team."""
        for team in self.teams:
            if team.name == team_name:
                team.update_stats(win=win, lose=lose, tie=tie)
                break
    
    def display_league_info(self):
        """Display basic info about the league and its teams."""
        print(f"League: {self.name}")
        for team in self.teams:
            team.display_info()
    
    def to_dict(self):
        """Convert league data to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "teams": [team.to_dict() for team in self.teams]
        }

# Additional functions related to handling league data in JSON files
def load_league(filepath):
    with open(filepath, 'r') as file:
        league_data = json.load(file)
        league = League(league_data['name'])
        for team_data in league_data['teams']:
            team = Team(team_data['location'], team_data['name'], team_data['players'], team_data['stats'])
            league.add_team(team)
    return league

def save_league(filepath, league):
    with open(filepath, 'w') as file:
        json.dump(league.to_dict(), file, indent=4)