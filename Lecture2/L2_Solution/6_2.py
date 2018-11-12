# 4.24: 游戏: 选出一张牌
###############################################
import random

Number = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
Suit   = ["Spade", "Heart", "Diamond", "Club"]

num  = random.randint(0, 12)
suit = random.randint(0, 3)

print("The card you picked is the %s of %s" % (Number[num], Suit[suit]))