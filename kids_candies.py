
""" Your job is to give all the kids the same amount of candies as the kid with the most 
candies and then return the total number candies that have been given out. If there are no kids, or only one, return -1.

In the first case (look below) the most candies are given to second kid (i.e second place in list/array), 8.
Because of that we will give the first kid 3 so he can have 8 and the third kid 2 and the fourth kid 4, 
so all kids will have 8 candies.So we end up handing out 3 + 2 + 4 = 9. """


def sweets_for_kids(kids):
    if not kids or len(kids) == 1:
        return -1
    return len(kids) * max(kids) - sum(kids)

print(sweets_for_kids(input("result?")))
sweets_for_kids([5,8,6,4])

sweets_for_kids ([1,6])