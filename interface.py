import score_grabber as scores

if __name__ == '__main__':
    probe = '''
            Hi, what would you like to view today?
            1. View current available scores
            2. View the previous week's scores
            3. View a specific week's scores
            4. View player stats

            ==> '''
    print(probe, end='')
    user = input()
    if user == '1':
        scores.get_current_scores('','')
    if user == '2':
        print("Not available yet")
        #scores.get_current_scores('')
    if user == '3':
        print(f"Which week and season would you like to view?")
        print(f"Week: ", end="")
        week = input()
        print("Season: ", end="")
        season = input()
        scores.get_current_scores(week, season)
    if user == '4':
        print("Not available yet")


