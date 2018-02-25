import random

deck = [
    ["A♠",1,11 or 1],
    ["2♠",2,2],
    ["3♠",3,3],
    ["4♠",4,4],
    ["5♠",5,5],
    ["6♠",6,6],
    ["7♠",7,7],
    ["8♠",8,8],
    ["9♠",9,9],
    ["10♠",10,10],
    ["J♠",11,10],
    ["Q♠",12,10],
    ["K♠",13,10],
    ["A♥",14,11 or 1],
    ["2♥",15,2],
    ["3♥",16,3],
    ["4♥",17,4],
    ["5♥",18,5],
    ["6♥",19,6],
    ["7♥",20,7],
    ["8♥",21,8],
    ["9♥",22,9],
    ["10♥",23,10],
    ["J♥",24,10],
    ["Q♥",25,10],
    ["K♥",26,10],
    ["A♣",27,11 or 1],
    ["2♣",28,2],
    ["3♣",29,3],
    ["4♣",30,4],
    ["5♣",31,5],
    ["6♣",32,6],
    ["7♣",33,7],
    ["8♣",34,8],
    ["9♣",35,9],
    ["10♣",36,10],
    ["J♣",37,10],
    ["Q♣",38,10],
    ["K♣",39,10],
    ["A♦",40,11 or 1],
    ["2♦",41,2],
    ["3♦",42,3],
    ["4♦",43,4],
    ["5♦",44,5],
    ["6♦",45,6],
    ["7♦",46,7],
    ["8♦",47,8],
    ["9♦",48,9],
    ["10♦",49,10],
    ["J♦",50,10],
    ["Q♦",51,10],
    ["K♦",52,10]
]

print("BLACK JACK")
print("***************")
print("***************")
print("Dealer hits on 16")
print("***************")
print("***************")
print("Aces are 11")
print("***************")
print("Call NewHand() to start")


def NewHand():
    i = random.sample(range(0,51), 51)
    dealerCeiling = 1
    playerCeiling = 21
    main(i, playerCeiling,dealerCeiling)
   



def main(i, playerCeiling,dealerCeiling):
    x = 0
    y = 20
    DealerHandValue = 0
    PlayerHandValue = 0

    print("Dealer Hand: ")
    print(deck[i[0]][0])
    print("?")
    while x < dealerCeiling:
        DealerHandValue = DealerHandValue + deck[i[x]][2]
        x +=1
    print("\nPlayer Hand: ")
    while y <= playerCeiling:
        print(deck[i[y]][0])
        PlayerHandValue = PlayerHandValue + deck[i[y]][2]
        y +=1
    print("Total", PlayerHandValue)
    turn(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue)




def turn(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue):
    if (PlayerHandValue == 21):
        print("\nBlack Jack!")
        decision = "end"
    if (PlayerHandValue > 21):
        print("\nBUSTED!")
        decision = "end"
    if(PlayerHandValue <= 21):
        decision = ""  
    if(decision != "end"):
        decision = input("\nHit or Stay?\n")
        if (decision == "Hit") or (decision == "hit"):
            playerCeiling += 1
            main(i, playerCeiling, dealerCeiling)
        elif (PlayerHandValue > 21):
            print("Busted")
        elif (decision == "Stay") or (decision == "stay"):
            print("You stayed\n")
            decision = "end"
            dealerPlay(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue)
        else:
            print("Huh?\n Type \"hit\" or \"stay\" dude, it's not that difficult")


def dealerPlay(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue):
    if (DealerHandValue == 21):
        print("\n Dealer has Black Jack")
        result(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue)
    elif (DealerHandValue > 21):
        print("\n Dealer Busts!")
        result(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue)
    elif(DealerHandValue <= 16):
        DealerHandValue = 0
        dealerCeiling += 1
        x = 0
        while x < dealerCeiling:
            DealerHandValue = DealerHandValue + deck[i[x]][2]
            x +=1
        dealerPlay(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue)
    elif(DealerHandValue >= 16):
        result(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue)


def result(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue):
    x = 0
    y = 20
    print("Dealer Hand: ")
    while x < dealerCeiling:
        print(deck[i[x]][0])
        x +=1
    print("Total", DealerHandValue)
    print("\nPlayer Hand: ")
    while y <= playerCeiling:
        print(deck[i[y]][0])
        y += 1
    print("Total", PlayerHandValue)
    if (DealerHandValue > 21):
        win()
    elif (PlayerHandValue > DealerHandValue):
        wind()
    elif (DealerHandValue > PlayerHandValue):
        lose()
    elif (DealerHandValue == PlayerHandValue):
        tie()


def win():
    print("You Win!")

def lose():
    print("You Lose!")

def tie():
    print("Push!")
