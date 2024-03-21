from game.player import Player
from game.team import Team
from game.game import Game

# Create players
player1 = Player("John Smith", 25, "6'5\"", "Guard", 190, 15, [80, 85, 90, 75, 80], 1000000)
player2 = Player("Doe Ray", 28, "6'8\"", "Forward", 220, 33, [78, 80, 75, 85, 77], 1200000)

# More players can be added similarly

# Create teams
team1 = Team("Hawks")
team2 = Team("Eagles")

team1.add_player(player1)
team2.add_player(player2)

# Simulate a game
game = Game(team1, team2)
Game.simulate_game(game)
print(Game.get_game_summary(game))