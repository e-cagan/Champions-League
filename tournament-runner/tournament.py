import random

TEAMS = ["Real Madrid", "FC Barcelona", "Bayern Münich", "Manchester City", "Paris Saint-Germain", "Juventus", "Liverpool", "Chelsea", "Atletico Madrid", "Borussia Dortmund", "Inter Milan", "Ajax", "Manchester United", "Shakhtar Donetsk", "Benfica", "Zenit Saint Petersburg", "Villarreal", "AC Milan", "Lille", "RB Leipzig", "Sevilla", "FC Porto", "Sporting CP", "Barcelona", "Galatasaray", "RB Salzburg", "Club Brugge", "Dynamo Kyiv", "Malmo FF", "Sheriff Tiraspol", "Young Boys", "Fenerbahçe"]

# THIS PROGRAM IS A SIMPLE SIMILATION FOR UEFA CHAMPIONS LEAGUE

# We must generate groups of the tournament randomly
# Then we must simulate the group stage (2 teams will continue the tournament)
# Then we must simulate quarter finals
# Then we must simulate semi finals 
# Then we must simulate final and display the winner

def generate_groups():
    random.shuffle(TEAMS)
    groups = {}
    for i in range(8):
        group_teams = TEAMS[i*4: (i+1)*4]
        groups[chr(ord('A') + i)] = group_teams
    return groups

def simulate_groups():
    groups = generate_groups()
    qualified_teams = []
    for group, team in groups.items():
        winners = random.sample(team, 2)
        qualified_teams.extend(winners)
        print(f"Group: {group}, Winners: {winners}")
    return qualified_teams

def simulate_quarter_finals(remaining_teams):
    qualified_teams = []
    for _ in range(4):
        matching_teams = random.sample(remaining_teams, 2)
        winner = random.choice(matching_teams)
        qualified_teams.append(winner)
        remaining_teams.remove(winner)
    print(f"The qualified teams are {qualified_teams} after quarter finals")
    return qualified_teams

def simulate_semi_finals(remaining_teams):
    qualified_teams = []
    for _ in range(2):
        matching_teams = random.sample(remaining_teams, 2)
        winner = random.choice(matching_teams)
        qualified_teams.append(winner)
        remaining_teams.remove(winner)
    print(f"The qualified teams are {qualified_teams} after semi-finals")
    return qualified_teams

def simulate_final(remaining_teams):
    return random.choice(remaining_teams)

def main():
    remaining_teams = simulate_groups()
    quarter_finalists = simulate_quarter_finals(remaining_teams)
    semi_finalists = simulate_semi_finals(quarter_finalists)
    winner = simulate_final(semi_finalists)

    print(f"The winner of the tournament is {winner}")

main()