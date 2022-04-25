import time
import random
import sys


def print_msg(msg):
    print(msg)
    time.sleep(1)


def intro():  # introduction message at the start of the game
    print_msg("You find yourself standing in an open field,"
              "filled with grass and yellow wildflowers.")
    print_msg("Rumor has it that a gorgon is somewhere around here,"
              " and has been terrifying the nearby village.")
    print_msg('In front of you is a house.')
    print_msg('To your right is a dark cave.')
    print_msg("In your hand you hold your trusty"
              " (but not very effective) dagger.")


def valid_input(msg, option1, option2):
    while True:
        options = input(msg).lower()

        if option1 in options:
            break
        elif option2 in options:
            break

    return options


def replay(weapon):  # to replay the game
    replay = valid_input('Would you like to play again? (y/n)', 'y', 'n')

    if replay == 'y':
        adventure_game()
    elif replay == 'n':
        print_msg('Thanks for playing! See you next time.')
        sys.exit()
    else:
        print_msg("Sorry, I don't understand")
        start_game(weapon)


def fight_options1(weapon):  # fight options if player chooses option 1
    print_msg("You feel a bit under-prepared for this,"
              " what with only having a tiny dagger.")
    fight_options = valid_input('Would you like to (1)'
                                ' fight or (2) run away?', '1', '2')

    if fight_options == '1':
        print_msg('You do your best...')
        print_msg('but your dagger is no match for the gorgon.')
        print_msg('You have been defeated!')
        replay(weapon)

    elif fight_options == '2':
        print_msg("You run back into the field. Luckily,"
                  " you don't seem to have been followed.")
        start_game(weapon)


def fight_option2(weapon):  # fight options if player chooses option 2
    fight_options = valid_input('Would you like to '
                                '(1) fight or (2) run away?', '1', '2')

    if fight_options == '1':
        print_msg("As the troll moves to attack,"
                  " you unsheath your new sword.")
        print_msg(f"The {weapon} of Ogoroth shines brightly in your"
                  " hand as you brace yourself for the attack.")
        print_msg("But the troll takes one look at your"
                  " shiny new toy and runs away!")
        print_msg('You have rid the town of the troll. You are victorious!')
        replay(weapon)

    elif fight_options == '2':
        print_msg("You run back into the field."
                  " Luckily, you don't seem to have been followed.")
        start_game(weapon)


def continue_option2():  # for player option 2 when weapons are availiable
    print_msg('Enter 1 to knock on the door of the house.')
    print_msg('Enter 2 to peer into the cave.')
    print_msg('What would you like to do?')
    option = valid_input('(Please enter 1 or 2.)', '1', '2')

    if option == '1':
        print_msg('You approach the door of the house.')
        print_msg("You are about to knock when the door"
                  " opens and out steps a gorgon.")
        print_msg("Eep! This is the gorgon's house!")
        print_msg('The gorgon attacks you!')


def game_option1(weapon):  # parent function for game option 1
    print_msg('You approach the door of the house.')
    print_msg("You are about to knock when the"
              " door opens and out steps a gorgon.")
    print_msg("Eep! This is the gorgon's house!")
    print_msg('The gorgon attacks you!')
    fight_options1(weapon)


def game_option2(weapon):  # parent option for game option 2
    print_msg(' You peer cautiously into the cave.')
    print_msg('It turns out to be only a very small cave.')
    print_msg('Your eye catches a glint of metal behind a rock.')
    print_msg(f"You have found the magical {weapon} of Ogoroth!")
    print_msg(f"You discard your silly old dagger"
              f" and take the {weapon} with you.")
    print_msg('You walk back out to the field.')
    for n in weapon:
        continue_option2()
        fight_option2(weapon)
        break


def start_game(weapon):  # game function
    print_msg('Enter 1 to knock on the door of the house.')
    print_msg('Enter 2 to peer into the cave.')
    print_msg('What would you like to do?')
    option = valid_input('(Please enter 1 or 2.)', '1', '2')

    if option == '1':
        game_option1(weapon)

    elif option == '2':
        game_option2(weapon)

    else:
        start_game(weapon)


def adventure_game():  # refactored function
    weapon = random.choice(['sword', 'dagger', 'chains'])
    intro()
    start_game(weapon)


adventure_game()
