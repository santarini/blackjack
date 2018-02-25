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

i = random.sample(range(0,51), 51)
Dealerhandvalue = deck[i[0]][2] + deck[i[1]][2]
Playerhandvalue = deck[i[2]][2] + deck[i[3]][2]
print("Dealer Hand: ", deck[i[0]][0], deck[i[1]][0])
print(Dealerhandvalue)
print("Player Hand: ", deck[i[2]][0], deck[i[3]][0])
print(Playerhandvalue)

turn = input("\nHit or Stay?\n")

if (turn == "Hit") or (turn == "hit"):
    Playerhandvalue = deck[i[2]][2] + deck[i[3]][2] + deck[i[4]][2]
    print("Dealer Hand: ", deck[i[0]][0], deck[i[1]][0])
    print(Dealerhandvalue)
    print("Player Hand: ", deck[i[2]][0], deck[i[3]][0], deck[i[4]][0])
    print(Playerhandvalue)

elif (turn == "Stay") or (turn == "stay"):
    print("You hit stay?")
else:
    print("Huh?")
