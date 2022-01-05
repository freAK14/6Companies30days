#Link to question - https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1/#

#Solution:

#User function Template for python3

class Solution:
    def findTwoElement( self, arr, n): 
        # code here
        numberMap = {}
        for i in arr:
            if not i in numberMap:
                numberMap[i] = True
            else:
                rep = i
         
        for i in range(1, n + 1):
            if not i in numberMap:
                miss = i
                
        return rep, miss

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
