"""
--------------PROBABILITY--------
FORMULA: PROBABILITY OF X =NO OF OUTCOMES THAT INCLUDE X/NO OF ALL POSSIBLE OUTCOMES"""

"""TOSS THE NUMBER"""



from random import randint


odd_even=['odd','even']


def tossing_times():
    while True:
        try:
            tosses=int(input("how many times to toss?"))
            
        except ValueError:
            print("not a valid integer")
            print("\n *100")
            continue
        return tosses

def odds_ends(odd=0,even=1):
    for num in range(0,1):
        selected=randint(0,1)
        print(odd_even[selected])
        if selected == 0:
            odd +=1
        else:
            even +=1
            
times = tossing_times()
odds_ends(times)

