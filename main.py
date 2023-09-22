from champ_setup import Champion, Guess
import pandas as pd

data = pd.read_json('champions.json') #Reads champions database
names = data.name.to_list()
is_game_over = False

champion = Champion()

def check_guess(user_input):
    guess = Guess(user_input)
    #Checks if the user's champion has mutual lanes info in the champion's lanes
    for lane in guess.lanes:
        if lane not in champion.lanes:
            print(f'not {lane}')
    if guess.lanes == champion.lanes:
        print(f'{champion.lanes}')
    else:
        for lane in guess.lanes:
            if lane in champion.lanes:
                print(f'{lane} + more')
    #Checks if the user's champion has mutual species info in the champion's species
    if guess.species == champion.species:
        print(f'{guess.species}')
    else:
        print(f'not {guess.species}')
    #Checks if the user's champion has mutual resource info in the champion's resources
    if guess.resource == champion.resource:
        print(f'{guess.resource}')
    else:
        print(f'not {guess.resource}')
    #Checks if the user's champion has mutual range_type info in the champion's range_types
    if guess.range_type == champion.range_type:
        print(f'{guess.range_type}')
    else:
        print(f'not {champion.range_type}')
    #Checks if the user's champion has mutual region info in the champion's regions
    if guess.region == champion.region:
        print(f'{guess.region}')
    else:
        print(f'not {guess.region}')
    #Compares the user's champion's release date to the champion's release date
    if int(guess.release_date[:4]) == int(champion.release_date[:4]):
        print(f'{guess.release_date}\n')
    elif int(guess.release_date[:4]) > int(champion.release_date[:4]):
        print(f'Earlier than {guess.release_date[:4]}\n')
    elif int(guess.release_date[:4]) < int(champion.release_date[:4]):
        print(f'Later than {guess.release_date[:4]}\n')

while not is_game_over:
    try:
        user_input = str(input("Guess a champion: ")).title()
        if user_input not in names:
            raise ValueError('Please enter full name of the champion')
        if user_input == champion.name:
            print(f'You won! The champion was: {champion.name}')
            is_game_over = True
        else:
            check_guess(user_input)
    except ValueError as e:
        print(f'Error: {e}')