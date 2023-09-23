from champ_setup import Champion, Guess
import pandas as pd

data = pd.read_json('champions.json') #Reads champions database
names = data.name.to_list()
is_game_over = False

champion = Champion()

def check_guess(user_input):
    guess = Guess(user_input)
    #Checks if the user's champion has mutual lanes info in the champion's lanes
    if guess.lanes == champion.lanes:
        print(f'Lanes: {guess.lanes}')
    elif any(lane in guess.lanes for lane in champion.lanes):
        print(f'Lanes: One of {guess.lanes}')
    else:
        print(f'Lanes: Not {guess.lanes}')
    #Checks other attributes of the guess and champion
    for attribute_name, attribute_value in vars(champion).items():
        if attribute_name in ['species', 'resource', 'range_type', 'region']:
            if getattr(guess, attribute_name) == getattr(champion, attribute_name):
                print(f'{attribute_name.title().replace("_"," ")}: {getattr(guess, attribute_name)}')
            else:
                print(f'{attribute_name.title().replace("_"," ")}: Not {getattr(guess, attribute_name)}')
    #Compares the user's champion's release date to the champion's release date
    if int(guess.release_date[:4]) == int(champion.release_date[:4]):
        print(f'Release date: {guess.release_date[:4]}\n')
    elif int(guess.release_date[:4]) > int(champion.release_date[:4]):
        print(f'Release date: Earlier than {guess.release_date[:4]}\n')
    elif int(guess.release_date[:4]) < int(champion.release_date[:4]):
        print(f'Release date: Later than {guess.release_date[:4]}\n')

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