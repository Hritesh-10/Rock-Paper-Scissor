import random

def game_input(comp_choice, human_choice):
    if comp_choice == human_choice:
        print('\n')
        print("it's a draw")

    elif comp_choice == 'rock' and human_choice == 'paper':
        print('\n')
        print(name, 'wins the round')
    elif comp_choice == 'rock' and human_choice == 'scissor':
        print('\n')
        print('computer wins the round')
    elif comp_choice == 'paper' and human_choice == 'scissor':
        print('\n')
        print(name, 'wins the round')
    elif comp_choice == 'paper' and human_choice == 'rock':
        print('\n')
        print('computer wins the round')
    elif comp_choice == 'scissor' and human_choice == 'rock':
        print('\n')
        print(name, 'wins the round')
    elif comp_choice == 'scissor' and human_choice == 'paper':
        print('\n')
        print('computer wins the round')
    else:
        print('\n')
        print('Wrong input')


name = input('Enter your name: ')
print('Welcome', name)

while True:
    option_list = ['Rock', 'Paper', 'Scissor']

    comp_choice = random.choice(option_list).lower()

    print('\n[Rock]', '[Paper]', '[Scissor]')
    human_choice = input('Enter your choice: ').lower()

    print('Computer chooses: ', comp_choice)

    game_input(comp_choice, human_choice)

    print('_____________________________')
    cont = int(input('\nEnter 0 to exit or enter 1 to continue: '))
    if cont == 0:
        break

print('\nThankyou for playing \nHope you enjoyed the game')