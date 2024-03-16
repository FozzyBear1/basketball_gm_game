import json
import os

class Player:
    def __init__(self, name, position, skills, salary):

        self.name = name
        self.position = position
        self.skills = int(skills)
        self.salary = float(salary)

    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position
    
    def get_skills(self):
        return self.skills
    
    def get_salary(self):
        return self.salary
    
    
    def to_dict(self):
        return {
        "name": self.name,
        "position": self.position,
        "skills": self.skills,
        "salary": self.salary 
        }
        
    def display_info(self):

        print(f"Player: {self.name}, Position: {self.position}, Salary: {self.salary}")
        print(f"Skills: {self.skills}")

#Defines how to add and load players from the players.json file.
def load_players(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file doesn't exist or is empty

def save_players(filepath, players):
    with open(filepath, 'w') as file:
        json.dump(players, file, indent=4)

def add_player(filepath, new_player):
    players = load_players(filepath)
    players.append(new_player)
    save_players(filepath, players)

def main():

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    players_file_path = os.path.join(dir_path, 'data', 'players.json')

    # Prompt the user for player details
    print("Add a New Player to the Database")
    name = input("Enter player's name: ")
    position = input("Enter player's position: ")
    try:
        skills = int(input("Enter player's skills (0-100): "))
        salary = float(input("Enter player's salary: "))
    except ValueError:
        print("Invalid input for skills or salary. Please enter numeric values.")
        return

    # Create a dictionary for the new player
    new_player = Player(name, position, skills, salary)

    # Add the new player to players.json
    add_player(players_file_path, new_player.to_dict())
    print(f"Player {name} added successfully!")

if __name__ == "__main__":
    main()
    
