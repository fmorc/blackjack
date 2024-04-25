import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_score(cards):
    sum = 0
    for card in cards:
        sum += card
    if sum > 21 and 11 in cards:
        sum = sum - 10
    return sum


def set_initial_cards(cards):
    return [random.choice(cards), random.choice(cards)]


def show_scores(player_cards, dealer_cards):
    print(f"Your cards: {player_cards}")
    show_current_score(player_cards)
    print(f"Dealer first card: {dealer_cards[0]}")


def show_current_score(cards):
    print(f"Your score: {get_score(cards)}")


def calculate_dealer_cards(dealer_cards):
    dealer_score = get_score(dealer_cards)
    while dealer_score < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)
        dealer_score = get_score(dealer_cards)


def final_results_conditions(dealer_score, player_score):
    if (dealer_score > player_score or player_score > 21) and dealer_score <= 21:
        print("House wins! You lose")
    elif (player_score > dealer_score and player_score <= 21) or (
            player_score < dealer_score and dealer_score > 21 and player_score <= 21):
        print("You won! Congrats!")
    elif dealer_score == player_score or (dealer_score > 21 and player_score > 21):
        print("It was a draw")


def final_results(dealer_score, player_score):
    print(f"Player cards: {player_cards}")
    print(f"Dealer cards: {dealer_cards}")
    print(f"Your final score: {player_score}")
    print(f"Dealer final score: {dealer_score}")
    final_results_conditions(dealer_score, player_score)


play_again = input("Do you want to play a game of Blackjack? Type 'y' to play or 'n' to skip:")
while play_again == 'y':
    player_cards = set_initial_cards(cards)
    dealer_cards = set_initial_cards(cards)
    calculate_dealer_cards(dealer_cards)
    show_scores(player_cards, dealer_cards)

    if get_score(player_cards) < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    else:
        another_card = 'n'

    while another_card == 'y':
        new_card = random.choice(cards)
        player_cards.append(new_card)
        print(f"Your new card is {new_card}")
        show_scores(player_cards, dealer_cards)
        if get_score(player_cards) < 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            another_card = 'n'
    else:
        dealer_score = get_score(dealer_cards)
        player_score = get_score(player_cards)
        final_results(dealer_score, player_score)
        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
