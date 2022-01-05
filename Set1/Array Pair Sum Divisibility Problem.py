#Link to question - https://practice.geeksforgeeks.org/problems/array-pair-sum-divisibility-problem3257/1

#Solution:

#User function Template for python3

class Solution:
    def canPair(self, nuns, k):
        # Code here
        if(len(nuns)==0 or len(nuns)==1):
            return 0
        dic = {}
        for i in range(len(nuns)):
            if(((nuns[i] % k) + k) % k in dic):
                dic[((nuns[i] % k) + k) % k]+=1
            else:
                dic[((nuns[i] % k) + k) % k]=1
        for x in dic:
            if(x==0):
                if(dic[x]%2!=0):
                    return 0
            elif(2*x==k):
                if(dic[x]%2!=0):
                    return 0
            else:
                if((k-x) in dic):
                    if(dic[x]!=dic[k-x]):
                        return 0
                else:
                    return 0
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
# } Driver Code Ends
