# """
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# """

class Solution:
    def romanToInt(self, s):
        values = {   #assigning values to roman numerals
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total=0
        length = len(s)


        # the main logic is that if the value of the current symbol is less than the value of the next symbol
        # then subtract the value of the current symbol from the total value otherwise add it
        for index in range(len(s)):
            if index+1 == length:
                total += values[s[index]]
            elif values[s[index]] < values[s[index + 1]]:
                total -= values[s[index]]
            else:
                total += values[s[index]]

        return total

example = Solution() #creating an object of the class
print(example.romanToInt("VIII"))  #calling the method romanToInt and passing the string "VIII" as an argument