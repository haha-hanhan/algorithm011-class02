
class Solution():
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        for i in range(len(nums)):
           for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if (nums[i] + nums[j]) == target:
                        return [i,j]
                    else:
                        continue

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))