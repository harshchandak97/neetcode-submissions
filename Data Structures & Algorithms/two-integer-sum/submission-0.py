class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        for j in range(len(nums)):
            if (target - nums[j]) in num_dict and num_dict[target - nums[j]] != j:
                return sorted([num_dict[target - nums[j]], j])
        
            

