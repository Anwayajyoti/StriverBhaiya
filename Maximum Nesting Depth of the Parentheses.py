Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3

class Solution:
    def maxDepth(self, s: str) -> int:
        currMax=Maxi=0
        for i in s:
            if i=='(':
                currMax+=1
                Maxi=max(currMax,Maxi)
            elif i==')':
                if currMax>0:
                    currMax-=1
                else:
                    return -1
        if currMax!=0:
            return -1
        else:
            return Maxi
