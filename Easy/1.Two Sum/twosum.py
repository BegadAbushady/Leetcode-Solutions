
class Solution(object):
    def twoSum(self, nums, target):

       
    # Approach 1: Brute Force
    # Time: O(n²)
    # Space: O(1)

        FirstNumCounter=0
        for stnum in nums:
            SecondNumCounter=0
            for ndnum in nums:
                if stnum+ndnum == target:
                    if SecondNumCounter!=FirstNumCounter:
                        
                        solution=[FirstNumCounter,SecondNumCounter]
                        return solution
                SecondNumCounter+=1
            FirstNumCounter+=1


    # Approach 2: Hash Map
    # Time: O(n)
    # Space: O(n)

        seen = {}
        counter = 0
        for current in nums:
            needed= target - current

            if needed in seen:
                return [seen[needed],counter]
            seen[current] = counter
            counter+=1


                    

# some testing variables 
lis = [3,2,4,10,10,22,354,53]
number = 12
sol = Solution()
print(sol.twoSum(lis,number))