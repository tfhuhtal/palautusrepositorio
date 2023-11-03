def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists

class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)
    
    def top(self, how_many, sorted_by=1):
        if sorted_by == 2:
            return sorted(self._players, key=sort_by_goals, reverse=True)[:how_many]
        elif sorted_by == 3:
            return sorted(self._players, key=sort_by_assists, reverse=True)[:how_many]
        else:
            return sorted(self._players, key=sort_by_points, reverse=True)[:how_many]
    