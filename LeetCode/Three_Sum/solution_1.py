class Solution(object):

    # Given an array nums of n integers, 
    # are there elements a, b, c in nums such that a + b + c = 0? 
    # Find all unique triplets in the array 
    # which gives the sum of zero.
    # Note:
    # The solution set must not contain duplicate triplets.
    # Example:
    # Given array nums = [-1, 0, 1, 2, -1, -4],
    # 
    # A solution set is:
    # [
    #   [-1, 0, 1],
    #   [-1, -1, 2]
    # ]
    def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## Idea: first sort nums, then iterate for the 
        # smallest number in the triple. 
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n-2): 
            ## iterate over nums[i] 
            ## for each nums[i] value, we need to find 
            ## a pair nums[j], nums[k] with i < j < k 
            ## st nums[j] + nums[k] = -nums[i]
            ## then decompose to a two sum problem
            print('========================')
            print('i = ', i)
            if i > 0 and nums[i] == nums[i-1]:
                ## To avoid duplicates:
                ## if nums[i] == nums[i-1], it means 
                ## we have already considerded nums[i]
                ## to be the smallest number in the triple 
                ## hence continue
                print("nums[i] = {}, nums[i-1] = {}, "\
                      "THEY ARE EQUAL, Continue"\
                      .format(nums[i], nums[i-1]))
                continue
            ## for fixed nums[i], we need two pointers 
            ## k > j > i st nums[j] + nums[k] = -nums[i]
            j = i+1 ## initialise j = i + 1, increment by 1. 
            k = n-1 ## initialise k = len(nums) - 1, decrease by 1
            new_target = -nums[i] ## find k > j > i st nums[j] + nums[k] = -nums[i]
            while j < k:
                print("j = {}, k = {}, new_target = {}"\
                .format(j, k, new_target))
                summ = nums[j] + nums[k]
                print("j < k TRUE, nums[j] = {}, "\
                      "nums[k] = {}, sum = {}"\
                      .format(nums[j], nums[k], 
                              nums[j]+nums[k]))
                if summ < new_target:
                    print("summ < new_target ! ")
                    print(" ----- ")
                    j += 1
                elif summ > new_target:
                    print("summ > new_target ! ")
                    print(" ----- ")
                    k -= 1
                else:
                    print("summ === new_target !,"\
                          "APPEND [{}, {}, {}]"\
                          .format(nums[i], nums[j], nums[k]))
                    print(" ----- ")
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]: 
                        ## Deal with duplicates
                        ## if having two same number in a roll
                        ## jump to the next one j += 1 
                        print("Increase j ... ")
                        j += 1
                    j += 1
                    while k > j and nums[k-1] == nums[k]:
                        ## Deal with duplicates 
                        ## decrease to the next one k -= 1 
                        print("Decrease k ... ")
                        k -= 1
                    k -= 1
        return res
        