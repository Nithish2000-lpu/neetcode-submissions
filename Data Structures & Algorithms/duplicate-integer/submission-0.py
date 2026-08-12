class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        self.nums = nums
        for i in range(len(self.nums)):
            if self.nums[i] in hash_set:
                return True
            hash_set.add(self.nums[i])

        return False
