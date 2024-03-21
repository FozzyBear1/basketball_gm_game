from player import Player

class Team:
    def __init__(self, location, name, roster, team_salary, team_overall):
        self.location = location
        self.name = name
        self.roster = set(roster) if roster is not None else set()
        self.team_salary = team_salary
        self.team_overall = team_overall

    def get_location(self):
        return self.location 

    def get_name(self):
        return self.name 

    def get_roster(self):
        return self.roster 
    
    def get_team_salary(self):
        return self.team_salary

    def set_location(self, location):
        self.location = location

    def set_name(self, name):
        self.name = name

    def add_player(self, player):
        if isinstance(player, Player):
            self.roster.add(player)
        else:
            print("The player has not been added to the roster.")

    def remove_player(self, player):
        try:
            self.roster.remove(player)
        except KeyError:
            print("The player is not in the roster")

    def calculate_team_salary(self):
        salary = 0
        for player in self.roster:
            salary += Player.get_salary(player)

        return salary
    
    def get_team_overall(self):
        return self.team_overall
    
    def calculate_team_overall(self):
        counter = 0
        overall = 0

        for player in self.roster:
            counter = counter + 1
            overall += Player.calculate_overall(player)

        overall = overall / counter
        return overall