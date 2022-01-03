#Link to question - https://practice.geeksforgeeks.org/problems/print-anagrams-together/1/#

#Solution:

#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        #code here
        def get_sorted_string(word):
            char_array = [c for c in word]
            char_array.sort()
            return "".join(char_array)
            
        groups = {}
        
        for word in words:
            sorted_letters = get_sorted_string(word)
            if sorted_letters in groups:
                groups[sorted_letters].append(word)
            else:
                groups[sorted_letters] = [word]
        ans = []
        for key, words in groups.items():
            ans.append(words)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
