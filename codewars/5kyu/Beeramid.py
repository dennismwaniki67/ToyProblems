# Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.
#
# A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...
#
# Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:
#
# 1) your referral bonus, and
#
# 2) the price of a beer can



# BEER PYRAMID WOULD LOOK SOMETHING LIKE THIS:
#                     1
#              2      2
#       2         2          2
# 2           2       2       2
# 2       2        2        2           2
# The number of beer cans in each row equals number of the row to the power of 2 (square)

def beeramid(bonus, price):
    print(bonus, price)
    counter = 1
    beers = bonus // price
    total = 0
    if bonus < 0:
        return 0
    while True:
        deck = counter * counter
        total += deck
        print(total)
        if beers < total:
            break
        else:
            counter += 1

    return counter - 1

    # your code
    # your code
#
#
# def function (n):
#
#     return n **2