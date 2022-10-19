import sys,heapq
from collections import defaultdict,deque
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
def invr():
    return(map(int,input().split()))
    
def traverse_password(neighbor, visited, path, key):
    path.append(key)
    visited.add(key)
    for neigh in neighbor[key]:
        if neigh not in visited:
            traverse_password(neighbor, visited, path, neigh)
    return path

def main():
    test = inp()
    for _ in range(test):
        password = insr()
        
        if len(password) == 1:
            res = []
            for i in range(97,123):
                res.append(chr(i))
            print("YES")
            print(''.join(res))
            
        else:
            
            neighbor = defaultdict(set)
            
            for i in range(1,len(password)):
                neighbor[password[i]].add(password[i-1])
                neighbor[password[i-1]].add(password[i])
                
            startKey = None
            isPossible = True
            
            for key in neighbor.keys():
                if len(neighbor[key]) > 2:
                    isPossible = False
                    break
                if len(neighbor[key]) == 1:
                    startKey = key
                    
            if not startKey or not isPossible:
                print("NO")
            else:
                visited = set()
                answer = traverse_password(neighbor, visited, [], startKey)
                for character in range(97,123):
                    letter = chr(character)
                    if letter not in neighbor:
                        answer.append(letter)
                print("YES")
                print(''.join(answer))
                
main()

