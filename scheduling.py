#perfroms a greedy algorithm to find the max number of courses that can be taken given thathe start and end times of courses t in O(n)
class Event():

    def __init__(self, start, end):
        self.start = start
        self.end = end


S = [1,3,4,5,7]
F = [4,6,7,9,10]

def count(S, F):
    ans = 1
    last =  0
    for i in range(len(S)):
        if S[i] >= F[last]:
            print("adding event starting at ", S[i])
            ans+=1
            last = i
    print(ans)


count(S, F)



