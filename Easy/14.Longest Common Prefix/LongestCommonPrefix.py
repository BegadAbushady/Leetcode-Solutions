class Solution(object):
    def longestCommonPrefix(self, strs):

        # Start by assuming the first word is the longest common prefix.
        # We will gradually shorten it whenever another word doesn't match.
        prefix = strs[0]
        newPrefix = strs[0]

        # If the first string is empty, there cannot be a common prefix.      
        if len(strs[0]) == 0:
            return ""
        
        # Compare the current prefix with every word in the list.
        for word in strs:
            # The common prefix cannot be longer than the current word
            # so shorten it to the length of the current word if necessary.
            if len(word) < len(prefix):
                prefix = prefix[:len(word)]
            # Compare the prefix and the current word character by character.
            for i in range(len(prefix)):

                if word[i] == prefix[i]:
                   # If the characters match, keep everything up to this position 
                   # as the new possible common prefix.
                   newPrefix = word[:i+1]
                
                else:
                   # A mismatch means the common prefix ends before this index.
                   # Remove the mismatching character and stop checking this word.
                   newPrefix = newPrefix[:i]
                   break

            prefix = newPrefix
            
        return newPrefix


     
example = Solution() # an example and the output is "a"
print(example.longestCommonPrefix(["ab","a","ad"]))