def countingValleys(steps, path):
    # Write your code here
    valley = 0
    seaLevel = 0
    arr = list(path)
    for p in arr:
        previousLevel = seaLevel
        if p=="U":
            seaLevel += 1
        else:
            seaLevel -= 1
        if seaLevel == 0 and previousLevel < 0:
            valley +=1
    return valley
