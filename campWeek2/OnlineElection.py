def topVotedCandidate(persons, times):
    persons = persons
    times = times
def q(t):
    left = 0
    right = len(persons)-1
    mid = 0
    while left<=right:
        mid = left + (right-left)//2
        if times[mid] < t:
            left = mid+1
        elif times[mid] > t:
            right = mid-1
        else:
            break
    if not times[mid] >= t:
        mid-=1
    zeroCount = 0
    oneCount = 0
    for i in range(mid+1):
        if persons[mid] == 0:
            zeroCount += 1
        else:
            oneCount += 1
    if oneCount > zeroCount:
        return 1
    elif zeroCount < oneCount:
        return 0 
    else:
        return persons[mid]