# calculates how many possibilities there are to climb on a ladder, taking 1 or two stages at a time.
# param stages- number of ladder stages
# return number of possibilities.
def nine_twenty_one(stages):
    if stages == 1:
        return 1
    elif stages == 2:
        return 2
    else:   # whether the first step is one stage, or two.
        return(nine_twenty_one(stages-1) + nine_twenty_one(stages-2))
