class Solution(object):

    # Given nums = [2, 7, 11, 15], target = 9,
    # Because nums[0] + nums[1] = 2 + 7 = 9,
    # return [0, 1].

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a hash table: 
        h = {val: idx for idx, val in enumerate(nums)}
        
        ## e.g. nums = [10, 20, 30]
        ##      h = {10: 0, 20: 1, 30: 2}

        for i, v in enumerate(nums):
            diff = target - v 
            # (diff in h) equivalent to 
            # (diff in list(h.keys()))
            if (diff in h) and (h[diff] != i): 
                return [i, h[diff]]


