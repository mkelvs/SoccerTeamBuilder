import csv

#Creating Lists
dragons = []
sharks = []
raptors = []
teams = [dragons, sharks, raptors]


#Reads the CSV file and returns it as a list.
def read_csv_file():
    with open("soccer_players.csv", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        players_list = list(csv_reader)
        return players_list

# Sort players according to their skills and returns the list of sorted players.
def sort_players(players):
    experienced_players = [] #List of players with soccer experience
    regular_players = [] # List of players without soccer experience
    for player in players:
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
        else:
            regular_players.append(player)
    return experienced_players, regular_players

#Distribute players to each teams equally.
def players_to_teams(experienced, regular, players_list, number_of_teams):
    team_size = len(players_list)/number_of_teams #calculates the number of players per team
    if len(dragons) < team_size and len(sharks) < team_size and len(raptors) < team_size:
        dragons.extend(experienced[:3])
        dragons.extend(regular[:3])
        sharks.extend(experienced[3:6])
        sharks.extend(regular[3:6])
        raptors.extend(experienced[6:])
        raptors.extend(regular[6:])
    for player in dragons:
        player.update({"team": "Dragons", "practice_time": "10:00 AM", "practice_location": "Gym C"})
    for player in sharks:
        player.update({"team": "Sharks", "practice_time": "8:00 AM", "practice_location": "Gym A"})
    for player in raptors:
        player.update({"team": "Raptors", "practice_time": "9:00 AM", "practice_location": "Gym B"})

    return dragons,sharks,raptors,all_players

#Creates a text file of the teams roster.
def create_text():
    with open("teams.txt", "w") as txt_file:
        players_list = read_csv_file()
        experienced, regular = sort_players(players_list)
        dragons, sharks, raptors, all_players = players_to_teams(experienced, regular, players_list, 3)
        txt_file.write("          " + "Dragons\n" + "Name | Experience | Guardian(s)\n" + "=" * 20 + "\n")
        for player in dragons:
            txt_file.write("{} | {} | {}".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))
            txt_file.write("\n")
        txt_file.write("\n")

        txt_file.write("          " + "Sharks\n" + "Name | Experience | Guardian(s)\n" + "=" * 20 + "\n")
        for player in sharks:
            txt_file.write("{} | {} | {}".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))
            txt_file.write("\n")
        txt_file.write("\n")

        txt_file.write("          " + "Raptors\n" + "Name | Experience | Guardian(s)\n" + "=" * 20 + "\n")
        for player in raptors:
            txt_file.write("{} | {} | {}".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))
            txt_file.write("\n")
        txt_file.write("\n")

#Create individual letter from the team's head coach.
def create_letter():
    for player in all_players:
        with open("{}.txt".format(player["Name"].lower().replace(" ", "_")), "w") as txt_file:
            txt_file.write("Dear {},\n\n".format(player["Guardian Name(s)"]))
            txt_file.write("We are very excited to welcome {}.\n".format(player["Name"]))
            txt_file.write("We are looking forward to see you on our first practice day held at {} in {}\n".format(player["practice_time"], player["practice_location"]))
            txt_file.write("See you there!\n\n")
            txt_file.write("Regards,\n{} Head Coach".format(player["team"]))


#Creating Variables:
players_list = read_csv_file()
experienced, regular = sort_players(players_list) #Assigning sorted players to variables
all_players = experienced + regular

players_to_teams(experienced,regular,players_list, 3) #Creating teams
create_text() #Create a text file for the team rosters
create_letter() #Create individual letters to players' guardians

