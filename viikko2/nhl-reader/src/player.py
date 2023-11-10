import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nat = dict['nationality']
        self.goal = dict['goals']
        self.assist = dict['assists']
    
    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goal:2} + {self.assist:2} = {self.goal + self.assist:2}"
    
class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
    
    def get_players(self):
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)
        return self.players
    
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
    
    def top_scorers_by_nationality(self, nat):
        sorted_players = sorted(self.players, key=lambda player: player.goal + player.assist, reverse=True)
        filtered_players = list(filter(lambda player: player.nat == nat, sorted_players))

        return filtered_players

    