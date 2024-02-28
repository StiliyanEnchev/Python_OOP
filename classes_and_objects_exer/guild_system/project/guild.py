class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):

        if player_name in self.players:
            self.players.remove(player_name)
            player_name.guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        player_details = '\n'.join([player.player_info() for player in self.players])
        return (f"Guild: {self.name}\n"
                f"{''.join(player_details)}")



