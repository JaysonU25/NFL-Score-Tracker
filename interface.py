import score_grabber as scores
import nfl_name_changer as names

if __name__ == '__main__':
    probe = '''
            Hi, what would you like to view today?
            1. View current available scores
            2. View a specific team's score
            3. View a specific week's scores
            4. View player stats

            ==> '''
    print(probe, end='')
    user = input()
    while user != '0':
        if user == '1':
            print()
            scores.get_current_scores('','')
        elif user == '2':
            print("\tWhich team would you like to view? \n\t==> ", end='')
            desired = input()
            desired = names.change_name(desired)
            scores.get_specific_score(desired)
        elif user == '3':
            print(f"\nWhich week and season would you like to view?")
            print(f"Week: ", end="")
            week = input()
            print("Season: ", end="")
            season = input()
            scores.get_current_scores(week, season)
        elif user == '4':
            print("\n\tNot available yet")
        else:
            print("\n\tNot valid input")
        probe = '''
            What else would you like to view today?
            1. View current available scores
            2. View a specific team's score
            3. View a specific week's scores
            4. View top player stats for a game

            ==> '''
        print(probe, end='')
        user = input()
    


