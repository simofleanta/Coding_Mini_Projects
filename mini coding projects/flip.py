"""
--------------PROBABILITY--------
FORMULA: PROBABILITY OF X =NO OF OUTCOMES THAT INCLUDE X/NO OF ALL POSSIBLE OUTCOMES""" 


from random import randint

coin_facets=['h','t']


def coin_guess_times():
    while True:
        try:
            guessing_times=int(input("how many times to toss?"))
            
        except ValueError:
            print("not a valid integer")
            print("\n *100")
            continue
        return guessing_times

def toss_coin(h=0,t=1):
    for num in range(0,1):
        target=randint(0,1)
        print(coin_facets[target])
        if target == 0:
            h +=1
        else:
            t +=1
            
times = coin_guess_times()
toss_coin(times)





