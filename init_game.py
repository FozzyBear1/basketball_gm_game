import json
import os
from models.player import Player
from models.team import Team
from models.league import League

def load_players_from_json(filepath):
    with open(filepath, 'r') as file:
        players_data = json.load(file)
    return [Player(name=p['name'], position=p['position'], skills=p['skills'], salary=p['salary']) for p in players_data]

def initialize_game():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    players_file_path = os.path.join(dir_path, 'data', 'players.json')
    
    # Load players
    all_players = load_players_from_json(players_file_path)
    
    # For simplicity, this example assumes you divide the players between two teams
    half_size = len(all_players) // 2
    team1_players = all_players[:half_size]
    team2_players = all_players[half_size:]

    # Create teams and assign players
    team1 = Team(location="Location A", name="Team A")
    team2 = Team(location="Location B", name="Team B")
    for player in team1_players:
        team1.add_player(player)
    for player in team2_players:
        team2.add_player(player)

    # Initialize the league with these teams
    league = League(name="Super League", teams=[team1, team2])

    # Here, you could simulate matches, update standings, etc.

if __name__ == "__main__":
    initialize_game()
                     
