class Solution(object):
    def isPalindrome(self, x):

        # Convert the number to a string so we can compare digits
        s = str(x)
        length = len(s)
        halflength = length//2
        # Compare digits from both ends toward the middle excluding the middle itself
        for index in range(halflength):
            if s[index] != s[length-index-1]:
                return False

        return True


# the first test case is 555, the output is True
# the second test case is 345, the output is False
test = 555
test2 = 123
example = Solution()
print(example.isPalindrome(test))
print(example.isPalindrome(test2))
