import random

deck = [
    ["A♠",1,11],
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
    ["A♥",14,11],
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
    ["A♣",27,11],
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
    ["A♦",40,11],
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




def NewHand():
    i = []
    i = random.sample(range(0,51), 51)
    z = 3
    main(i, z)




def main(i, z):
    x = 0
    y = 2
    DealerHandValue = 0
    PlayerHandValue = 0

    print("Dealer Hand: ")
    print(deck[i[0]][0])
    print("?")
    while x < y:
        DealerHandValue = DealerHandValue + deck[i[x]][2]
        x +=1
    print("\nPlayer Hand: ")
    while y <= z:
        print(deck[i[y]][0])
        PlayerHandValue = PlayerHandValue + deck[i[y]][2]
        y +=1
    print("Total", PlayerHandValue)
    turn(i, x, y, z, PlayerHandValue, DealerHandValue)




def turn(i, x, y, z, PlayerHandValue, DealerHandValue):
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
            z += 1
            main(i, z)
        elif (PlayerHandValue > 21):
            print("Busted")
        elif (decision == "Stay") or (turn == "stay"):
            print("You stayed\n")
            decision = "end"
            result(i, z, PlayerHandValue, DealerHandValue)
        else:
            print("Huh?")




def result(i, z, PlayerHandValue, DealerHandValue):
    x = 0
    y = 2
    print("Dealer Hand: ")
    while x < y:
        print(deck[i[x]][0])
        x +=1
    print("Total", DealerHandValue)
    print("\nPlayer Hand: ")
    while y <= z:
        print(deck[i[y]][0])
        y += 1
    print("Total", PlayerHandValue)
    if (PlayerHandValue > DealerHandValue):
        print("You Win!")
    if (DealerHandValue > PlayerHandValue):
        print("You Lose!")
