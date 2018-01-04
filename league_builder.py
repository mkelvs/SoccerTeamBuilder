import csv

experienced_players = []
regular_players = []
dragons_team = []
sharks_team = []
raptors_team = []

with open("soccer_players.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for player in csv_reader:
        #Gathers all Experienced players together and all in list experienced_players
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
        else:
            # Gathers all Experienced players together and all in list regular_players
            regular_players.append(player)

    for players in experienced_players:
        # Each experienced player in list experienced_players is placed equally on each team
        if players not in dragons_team and len(dragons_team) < 3:
            dragons_team.append(players)
        elif players not in sharks_team and len(sharks_team) <3:
            sharks_team.append(players)
        elif players not in raptors_team and len(raptors_team) < 3:
            raptors_team.append(players)

    for players in regular_players:
        #Each regular players in list regular_players are placed on each team with a max of 6 people
        if players not in dragons_team and len(dragons_team) < 6:
            dragons_team.append(players)
        elif players not in sharks_team and len(sharks_team) <6:
            sharks_team.append(players)
        elif players not in raptors_team and len(raptors_team) < 6:
            raptors_team.append(players)





