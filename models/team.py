from player import Player
import json
import os

class Team:
    def init(self, location, name, players = [], stats = None, strength = 0):
        self.location = location
        self.name = name
        self.players = players
        self.stats = stats if stats else {"wins": 0, "losses" : 0, "ties": 0}
        self.strength = strength

    def to_dict(self):
        return {
        "location": self.location,
        "name": self.name,
        "players": self.players,
        "stats": self.stats if self.stats else {"wins": 0, "losses": 0, "ties": 0},
        "strength": self.strength
        }
    
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.player:
            self.players.remove(player)

    def update_stats(self, win = False, lose = False, tie = False):
        if win:
            self.stats['wins'] += 1
        elif lose:
            self.stats['losses'] += 1
        elif tie:
            self.stats['ties'] += 1
            
    def display_info(self):
        print(f"Team: {self.location} + {self.name}")
        print("Roster:")
        for player in self.players:
            print(f"- {player.name}")
        print("Stats:")
        print(f"Wins: {self.stats['wins']}, Losses: {self.stats['losses']}, Ties: {self.stats['ties']}")

    def calculate_team_strength(self):
        # Example method that calculates team strength based on player skills
        for team in self.teams:
            team_strength = sum(player.get_skills() for player in team.players)
            print(f"Team {team.name} Strength: {team_strength}")
    

#Defines how to add and load players from the players.json file.
def load_teams(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file doesn't exist or is empty

def save_teams(filepath, teams):
    with open(filepath, 'w') as file:
        json.dump(teams, file, indent=4)

def add_player(filepath, new_team):
    teams = load_teams(filepath)
    teams.append(new_team)
    save_teams(filepath, teams)
    
    