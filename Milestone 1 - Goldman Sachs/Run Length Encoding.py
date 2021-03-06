#Link to question - https://practice.geeksforgeeks.org/problems/run-length-encoding/1/#

#Solution:

#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    i = 0
    ans = ""
    
    while i < len(arr):
        temp = arr[i]
        cnt = 1
        while i+1 < len(arr) and temp == arr[i+1]:
            i += 1
            cnt += 1
        ans += temp + str(cnt)
        i += 1
    return ans

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends
