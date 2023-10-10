"""This program was written by a student attending the S23-Python Development I course through OntarioLearn in fulfilment
one of the requirements of the Course of Studies. This program may not be released, quoted or copied, except with the
express permission of the author.

Copyright (c) 2023 John Alexander"""

import random, time

# Generate a random card
def gen_random_card():
    card = random.randint(1, 10)
    return card


def hit_or_stand():
    while True:
        hit_stand = str(input('\nHit or stand? (h/s): ')).lower()
        if hit_stand == 'h':
            return True
        elif hit_stand == 's':
            return False
        else:
            print('Please try again with a valid response. Only \'h\' or \'s\' are acceptable responses.')


def game_begins():
    """I decided to make the main portion of the program one big function. It makes it easier to recall based on whether
    the player wants to play again."""


#Initialize card deck and get ready to count cards so that no more than four of any one card may be selected

    card_deck = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}
    player_cards = []
    dealer_cards = []



#deal player cards

    pl_counter = 0
    while pl_counter < 2:
        dealt_card = gen_random_card()
        while card_deck[str(dealt_card)] == 4:
            dealt_card = gen_random_card()
        card_deck[str(dealt_card)] = card_deck[str(dealt_card)] + 1
        player_cards.append(dealt_card)
        pl_counter +=1

    print(f'You draw a {player_cards[0]} and a {player_cards[1]}. Your total is {sum(player_cards)}.')

#deal dealer cards

    dl_counter = 0
    while dl_counter < 2:
        dealt_card = gen_random_card()
        while card_deck[str(dealt_card)] == 4:
            dealt_card = gen_random_card()
        card_deck[str(dealt_card)] = card_deck[str(dealt_card)] + 1
        dealer_cards.append(dealt_card)
        dl_counter +=1
    print(f'The dealer draws a {dealer_cards[0]} and a hidden card.')


# Player option to hit or stand

    while sum(player_cards)<21:
        lets_hit = hit_or_stand()
        print(lets_hit)
        while lets_hit is True:
            dealt_card = gen_random_card()
            while card_deck[str(dealt_card)] == 4:
                dealt_card = gen_random_card()
            card_deck[str(dealt_card)] = card_deck[str(dealt_card)] + 1
            player_cards.append(dealt_card)
            if sum(player_cards) == 21:
                print(f'\nHit! You draw a {player_cards[pl_counter]}. You have Blackjack! Your total is {sum(player_cards)}.')
                break

            elif sum(player_cards) > 21:
                print(f'\nHit! You draw a {player_cards[pl_counter]}. Your total is {sum(player_cards)}.')
                print(f'\nYou bust!')
                print(f'\nDealer wins!')
                break

            else:
                print(f'\nHit! You draw a {player_cards[pl_counter]}. Your total is {sum(player_cards)}.')
                pl_counter += 1
                lets_hit = hit_or_stand()

        else:
            break

# Dealer option to hit or stand

    time.sleep(1)

    print(f'\nThe dealer reveals the hidden card of {dealer_cards[1]} and has a total of {sum(dealer_cards)}.')
    if sum(player_cards)>21 and sum(dealer_cards)<17:
        print(f'Dealer must still draw to 17 to win.  Let\'s see what happens...')

    while sum(dealer_cards) < 17:
        print(f'\nThe dealer hits.')
        time.sleep(1)
        dealt_card = gen_random_card()
        while card_deck[str(dealt_card)] == 4:
            dealt_card = gen_random_card()
        card_deck[str(dealt_card)] = card_deck[str(dealt_card)] + 1
        dealer_cards.append(dealt_card)
        time.sleep(1)
        print(f'\nDealer is dealt a {dealt_card}. The dealer\'s total is {sum(dealer_cards)}.')

# Evaluate if dealer has 21 or not or whether the dealer has busted

    if sum(dealer_cards) == 21:
        print(f'\nDealer has Blackjack and wins!\n')
    elif (sum(player_cards)>21 and sum(dealer_cards)>21):
        print(f'\nYou have both busted!')
    elif sum(dealer_cards)>21:
        print(f'\nDealer busts! You win!\n')
    else:
        print(f'\nThe dealer stands.')
        time.sleep(.5)
        print(f'\nYou have a total of {sum(player_cards)} and the dealer has {sum(dealer_cards)}.')
        if sum(player_cards) == sum(dealer_cards):
            print(f'\nYou both have {sum(player_cards)}. Draw goes to the dealer\n')
        elif (sum(player_cards) > sum(dealer_cards)) and (sum(player_cards) < 22):
            print(f'\nYou win!\n')
        else:
            print(f'\nDealer wins!\n')




#Welcome Splash

print(f'Welcome to Blackjack.')
print(f'---------------------------------------------------\n')



while True:
    play = str(input('Do you wish to start a new game? (y/n): ')).lower()
    if play == 'y':
        game_begins()
    elif play == 'n':
        break
    else:
        print('Please try again with a valid response. Only \'y\' or \'n\' are acceptable responses.')

print(f'\nThank you for playing... Goodbye.')

exit()

