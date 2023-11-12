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




if __name__ == "__main__":
    #score = get_current_scores()
    #print(score)
    # print(f"Which week and season would you like to view?")
    
    # print(f"Week: ", end="")
    # week = input()
    # print("Season: ", end="")
    # season = input()
    # print()
    
    # get_current_scores(week, season)

    get_specific_score("New York Jets")