import random

money = 100

#Write your game of chance functions here

def coinflip(call,amt):
    outcome = random.randint(0,1)
    ## if outcome = 0, then Heads. If 1, then Tails.
    if call in ["Heads!", "heads", "HEADS", "H", "Head"]:
        call = "Heads"
    if call in ["Tails!", "tails", "TAILS", "T", "Tail"]:
        call = "Tails"
    if outcome == 0:
        coin = "Heads"
        print("The coin is Heads.")
    else:
        coin = "Tails"
        print("The coin is Tails.")
    if coin == call:
        print("Congratulations! You won " + str(amt) + ".")
        return amt
    else:
        print("Better luck next time! You lost " + str(amt) + ".")
        return -1*amt

def chohan(call,amt):
    die1 = random.randint(1,6)
    print("First roll: " + str(die1))
    die2 = random.randint(1,6)
    print("Second roll: " + str(die2))
    sum = die1 + die2
    print("Sum: " + str(sum))
    even_or_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
    result = even_or_odd(sum)
    if call == result:
        print("Congratulations! You won " + str(amt) + ".")
        return amt
    else:
        print("Better luck next time! You lost " + str(amt) + ".")
        return -1*amt

def twocards(amt):
    cards = random.sample(range(0,51),2)
    # 0-12 = diamonds, 13-25 = hearts, 26-38 clubs, 39-51 spades
    ##TODO find way to make empty list
    ranks = [0,0]
    suites = [0, 0]
    values = [0, 0]
    #card[0] is your card, card[1] is house card
    ##TODO check for loops
    for i in 0, 1:
        #card values
        ranks[i] = cards[i] % 13
        if ranks[i] == 0:
            values[i] = "Two"
        elif ranks[i] == 1:
            values[i] = "Three"
        elif ranks[i] == 2:
            values[i] = "Four"
        elif ranks[i] == 3:
            values[i] = "Five"
        elif ranks[i] == 4:
            values[i] = "Six"
        elif ranks[i] == 5:
            values[i] = "Seven"
        elif ranks[i] == 6:
            values[i] = "Eight"
        elif ranks[i] == 7:
            values[i] = "Nine"
        elif ranks[i] == 8:
            values[i] = "Ten"
        elif ranks[i] == 9:
            values[i] = "Jack"
        elif ranks[i] == 10:
            values[i] = "Queen"
        elif ranks[i] == 11:
            values[i] = "King"
        elif ranks[i] == 12:
            values[i] = "Ace"
        #suites
        if cards[i] < 13:
            suites[i] = "Diamonds"
        elif cards[i] < 26:
            suites[i] = "Hearts"
        elif cards[i] < 39:
            suites[i] = "Clubs"
        else:
            suites[i] = "Spades"
    print("Your card is the " + values[0] + " of " + suites[0] + ".")
    print("The house card is the " + values[1] + " of " + suites[1] + ".")
    if ranks[0] > ranks[1]:
        print("Congratulations! You won " + str(amt) + ".")
        return amt
    elif ranks[0] < ranks[1]:
        print("Better luck next time! You lost " + str(amt) + ".")
        return -1*amt
    else:
        print("It's a draw. You get your money back.")
        return 0
def roulette(bet,amt):
    #0 is 0, 00 is -1
    #Display tile number and color
    number = random.randint(-1,36)
    if number in range(1,11) or number in range(19,29):
        if number % 2 == 0:
            color = "Black"
        else:
            color = "Red"
    elif number in range(11,19) or number in range(29,37):
        if number % 2 == 0:
            color = "Red"
        else:
            color = "Black"
    else:
        color = "Green"
    if number == -1:
        print("The roll is 00")
    elif number == 0:
        print("The roll is 0")
    else:
        print("The roll is : " + str(number) + " " + color)
    if bet == "Even" or bet == "Odd":
        if number < 1:
            print("Better luck next time! You lost " + str(amt) + ".")
            return -1*amt
        elif (bet == "Even" and (number % 2 == 0)) or (bet == "Odd" and (number % 2 == 1)):
            print("Congratulations! You won " + str(amt) + ".")
            return amt
        else:
            print("Better luck next time! You lost " + str(amt) + ".")
            return -1*amt
    elif bet == "Red" or bet == "Black":
        if color == bet:
            print("Congratulations! You won " + str(amt) + ".")
            return amt
        else:
            print("Better luck next time! You lost " + str(amt) + ".")
            return -1*amt

#Call your game of chance functions here

money += coinflip("HEADS",10)
print("Your current balance: " + str(money))

money += chohan("Even",10)
print("Your current balance: " + str(money))

money += twocards(10)
print("Your current balance: " + str(money))

money += roulette("Black",10)
print("Your current balance: " + str(money))
