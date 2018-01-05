import csv

#Reads the csv file and convert it to a list
def csv_to_list():
    with open("soccer_players.csv", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_list = list(csv_reader)
        return csv_list



#Sort players based on their experience
def sort_players(players):
    experienced_players = []
    regular_players = []
    for player in players:
        #Gathers all Experienced players together and all in list experienced_players
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
        else:
            # Gathers all Experienced players together and all in list regular_players
            regular_players.append(player)
    return experienced_players, regular_players


all_items = csv_to_list()
experienced_players, regular_players = sort_players(all_items)

print("Experienced Players: {}".format(experienced_players))


"""
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

"""
