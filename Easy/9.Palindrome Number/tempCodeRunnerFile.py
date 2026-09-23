class Solution(object):
    def isPalindrome(self, x):

        # Convert the number to a List so we can compare digits
        s = x
        theList = []
        digit=0
        index = 0
        while s > 0:
            digit = s%10
            s//=s
            theList.append(digit)


        halflength = len(theList)//2
        # Compare digits from both ends toward the middle excluding the middle itself
        for index in range(halflength):
            if theList[index] != theList[halflength*2-index-1]:
                return False

        return True


# the first test case is 555, the output is True
# the second test case is 345, the output is False
test = 555
test2 = 123
example = Solution()
print(example.isPalindrome(test))
print(example.isPalindrome(test2))
