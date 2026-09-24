class Solution(object):
    def isPalindrome(self, x):

        # Convert the number to a List so we can compare digits
        num = x
        theList = []
        digit = 0

        if num < 0:
            return False

        while num > 0:
            digit = num % 10
            num //= 10
            theList.append(digit)

        length = len(theList)
        # Compare digits from both ends toward the middle excluding the middle itself
        
        for index in range(length//2):
            if theList[index] != theList[length-index-1]:
                return False

        return True


# the first test case is 555, the output is True
# the second test case is 345, the output is False

test = 555
test2 = 345
example = Solution()
print(example.isPalindrome(test))
print(example.isPalindrome(test2))
