class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        firstWord = strs[0]
        shortWord = strs[0]
        prefix = ""
        for word in strs:
            if len(word) < len(shortWord):
                shortWord = word
            for i in range(len(shortWord)):
                if firstWord[i] == shortWord[i]:
                   prefix = prefix + shortWord[i]
                else:
                    break
        return prefix
     
example = Solution()
print(example.longestCommonPrefix(["ab","a"]))