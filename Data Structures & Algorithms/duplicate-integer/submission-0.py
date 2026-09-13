class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num_dict.get(num, 0) != 0:
                return True
            else:
                num_dict[num] = 1
        return False
