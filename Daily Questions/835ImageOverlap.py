class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        d=defaultdict(int)
        maxVal=0
        for row1 in range(n):
            for col1 in range(n):
                if img1[row1][col1]==1:
                    for row2 in range(n):
                        for col2 in range(n):
                            if img2[row2][col2]==1:
                                offset=((row2-row1),(col2-col1))                    
                                d[offset]+=1
                                maxVal=max(maxVal,d[offset])
        return maxVal