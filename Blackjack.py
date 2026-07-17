import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def detect_blackjack(sum_u, sum_d):
    if sum_u == 21 and sum_d != 21:
        print("You won! by Blackjack!")
        return
    if sum_d == 21:
        print("Dealer won! by Blackjack!")
        return

user = []
dealer = []
for i in range(1, 3):
    user.append(random.choice(cards))
    dealer.append(random.choice(cards))
print("Cards in Your hands = ", user)
print("First Cards in Dealer  = ", dealer[0])
sum_u = sum(user)
sum_d = sum(dealer)
print("Sum of your hands = ", sum_u)

detect_blackjack(sum_u, sum_d)
onemorecard = True
while onemorecard:
    another_card = input("Do you want to get another card ? (yes/no): ").lower()
    if sum_u > 17 and another_card == "yes":
        print("You cannot pick another card ! Now . Dealer Picks one ")
    if another_card == "yes" and sum_u < 17:
        user.append(random.choice(cards))
        if user[-1] == 11 and sum(user) > 21:
            user.remove(11)
            user.append(1)
        sum_u = sum(user)
        print("Sum of your hands = ", sum_u)
        if sum_u == 21:
            print("User won! by Blackjack!")
            break
        elif sum_u > 21:
            print("Your sum exceeded 21. You lose!")
            break
        else:
            continue
    else :
        print("Dealer picks a card")
        dealer.append(random.choice(cards))
        if dealer[-1] == 11 and sum(dealer) > 21:
            dealer.remove(11)
            dealer.append(1)
        sum_d = sum(dealer)
        if sum_d == 21:
            print("Dealer won! by Blackjack!")
            break
        elif sum_d > 21:
            print("Dealer's sum exceeded 21. You Win!")
            break
        else:
            continue

if sum_d > 18:
    print("\n\n++++++++++++++++++++ GAME RESULTS +++++++++++++++++++++\n\n")
    print("Dealer's cards = ", dealer)
    print("Dealer's Sum = ", sum_d)
    print("User's cards = ", user)
    print("user's Sum = ", sum_u)

    onemorecard = False