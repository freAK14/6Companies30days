#Link to question - https://practice.geeksforgeeks.org/problems/number-following-a-pattern3126/1

#Solution:

#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        ans = ""
 
        i = 0
        cur = 1
        dCount = 0
        while (i < len(S)) :
     
            ch = S[i]

            if (i == 0 and ch == 'I') :
                ans += str(cur)
                cur+=1

            if (ch == 'D') :
                dCount+=1

            j = i + 1
            while (j < len(S) and S[j] == 'D') :
                dCount+=1
                j+=1

            k = dCount
            while (dCount >= 0) :
                ans += str(cur + dCount)
                dCount-=1

            cur += (k + 1)
            dCount = 0
            i = j
     
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends
