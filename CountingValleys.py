8
UDDDUDUU

def countingValleys(steps, path):
    # Write your code here
    currLevel=0
    valley=0
    for steps in path:
        if steps=='U':
            currLevel+=1
            if currLevel==0:
                valley+=1
        elif steps=='D':
            currLevel-=1
    return valley
