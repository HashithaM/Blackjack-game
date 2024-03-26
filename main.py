import random
print("$$ WELCOME TO BLACKJACK $$")

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw !"
    elif user_score == 0:
        return "Win with a blackjack !"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack !"
    elif user_score > 21:
        return "You went over. You lose !"
    elif computer_score > 21:
        return "Opponent went over. You win !"
    elif user_score > computer_score:
        return "You win !"
    else:
        return "You lose !"


def calculate_score(cards):
    """Take a list of cards and return the calculated score from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards are {user_cards} and your score is {user_score}.")
        print(f"Computer's first card is {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get a new card or type 'n' to pass :")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand :{user_cards} Your final score :{user_score}.")
    print(f"Computer's final hand :{computer_cards} Computer's final score :{computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play the game of blackjack ? Type 'y' or 'n' :").lower() == "y":
    play_game()
    print("CLEAR")



# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user = []
# computer = []


# def user_draw():
#     user.append(random.choice(cards))
#     print(f"Your card is :{user[len(user) - 1]}")


# def user_sum():
#     total = 0
#     for i in user:
#         total += i
#     return total


# def computer_draw():
#     computer.append(random.choice(cards))


# def computer_sum():
#     sum = 0
#     for j in computer:
#         sum += j
#     return sum


# # print(f"Computer's card is {computer[0]}")

# # for checking
# # print(user)
# # print(user_sum())
# # print(computer)
# # print(computer_sum())

# user_draw()
# computer_draw()

# hit = "y"
# while hit == "y":
#     user_draw()
#     print(user)
#     print(computer)
#     if user_sum() == 21:
#         print("User wins !")
#         break
#     if computer_sum() == 21:
#         print("Computer wins !")
#         break
#     if user_sum() > 21:
#         for i in user:
#             if i == 11:
#                 user__sum = user_sum() - 10
#                 if user__sum > 21:
#                     print("Computer wins !")
#                     break
#     hit = input("Do you want to draw another card ? Type 'y' to draw or 'n' to stand :").lower()

# while computer_sum() < 17:
#     computer_draw()

# print(user)
# print(f"User sum is {user_sum()}")
# print(computer)
# print(f"Computer sum is {computer_sum()}")

# if computer_sum() > 21:
#     print("User wins !")
# elif computer_sum() == 21:
#     print("Computer wins !")

# user_dif = 21 - user_sum()
# computer_dif = 21 - computer_sum()

# if user_dif < computer_dif:
#     print("User wins !")
# elif user_dif > computer_dif:
#     print("Computer wins !")
# elif user_dif == computer_dif:
#     print("Match draw !")
# else:
#     print("I don't know !")
