import requests
from bs4 import BeautifulSoup



URL = "https://www.pro-football-reference.com/boxscores/"


def get_current_scores(week, season):
    if week == "":
        URL = "https://www.pro-football-reference.com/boxscores/"
    else:
        URL = f"https://www.pro-football-reference.com/years/{season}/week_{week}.htm"
    response = requests.get(URL)
    parsed = BeautifulSoup(response.content, "html.parser")

    games = parsed.find_all("table", class_="teams")

    for game in games: 
        draws = game.find_all("tr", class_="draw")
        if len(draws) > 0:
            draw_result = ""
            for draw in draws:
                W_N = draw.find("a")
                W_S = draw.find("td", class_="right")
                if(draw_result == ""):
                    draw_result = draw_result + W_N.text + " " + W_S.text + "-"
                else:
                    draw_result = draw_result + W_S.text + " " + W_N.text
            print(f"{draw_result}\n")
        else:
            winner = game.find("tr", class_="winner")
            if winner: 
                W_N = winner.find("a")
                W_S = winner.find("td", class_="right")
                loser = game.find("tr", class_="loser")
                L_N = loser.find("a")
                L_S = loser.find("td", class_="right")
                print(f"{W_N.text} {W_S.text}-{L_S.text} {L_N.text}\n")    
    return 0

def get_specific_score(desired):
    desired = desired.upper()
    response = requests.get(URL)
    parsed = BeautifulSoup(response.content, "html.parser")

    games = parsed.find_all("table", class_="teams")

    for game in games: 
        teams = game.find_all("tr")
        first_team = ""
        first_score = ""
        second_team = ""
        second_score = ""
        for team in teams:
            if team.find("a") != None:
                if first_team == "":
                    first_team = team.find("a").text.upper()
                    first_score = team.find("td", class_="right").text
                else: 
                    second_team = team.find("a").text.upper()
                    second_score = team.find("td", class_="right").text
            if first_team == desired and second_team != "":
                print(f"{first_team} {first_score}-{second_score} {second_team}")
                return 0
            elif second_team == desired:
                print(f"{first_team} {first_score}-{second_score} {second_team}")
                return 0
            else:
                continue
    print(f"Either you spelt it wrong, or the {desired} had a bye this week!")
    return 0

def get_player_stats(week, season, team):
    if week == "":
        URL = "https://www.pro-football-reference.com/boxscores/"
    else:
        URL = f"https://www.pro-football-reference.com/years/{season}/week_{week}.htm"
    winner = ""
    loser = ""
    response = requests.get(URL)
    parsed = BeautifulSoup(response.content, "html.parser")

    games = parsed.find_all("div", class_="game_summary expanded nohover")
    for game in games:
        # ADD CHECK FOR DRAWS
        draws = game.find_all("tr", class_="draw")
        if len(draws) > 0:
            for draw in draws:
                winner = draw.find("a").text
                if winner != "":
                    loser = draw.find("a").text
        else:    
            # FINISH CODE TO CHECK IF THIS GAME IS THE CORRECT ONE 
            winner = game.find("tr", class_="winner").find("a").text
            loser = game.find("tr", class_="loser").find("a").text

        if team == winner or team == loser:
            stats = game.find("table", class_="stats").find_all("td")
            print(f"\nThe leader in {stats[0].text} was {stats[1].text} with {stats[2].text} yards!\n")
            print(f"The leader in {stats[3].text} was {stats[4].text} with {stats[5].text} yards!\n")
            print(f"The leader in {stats[6].text} was {stats[7].text} with {stats[8].text} yards!\n")
            return 0

    print(f"The {team} does not seem to have had a game this week, or you misspelled it.")
