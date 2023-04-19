import random


players = []
number_of_players = int(input("How many players are there?"))
print(len(players))
for i in range(1, number_of_players+1):
    players.append(i)
print("Welcome to Team or Player Allocator!\n")


while True:
    random.shuffle(players)
    resp = input("Is it a team or individual sport?\
                 \n Type team or ind here: ")
    
    if resp == "team":
        team1 = players[:len(players)//2]
    # print(team1)

        print("Team 1 captain: ", random.choice(team1))
        print("Team 1:")
        for player in team1:
            print(player)

        team2 = players[len(players)//2:]
        print("\nTeam 2 captain: ", random.choice(team2))
        print("Team 2:")
        for player in team2:
            print(player)

        response = input("Pick the team again? Type y for 'yes' or n for 'no': ")
        if response == "n":
            break
        

    else:
        for i in range (0, players[0], 2):
            print(players[i], " vs ", players[i+1])
            start = random.randrange(i, i+2)
            print(players[start], " starts\n")
    break

# The program is to be split in two parts            print(5+5)
