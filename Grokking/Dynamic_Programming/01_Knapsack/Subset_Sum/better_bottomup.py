## O(S) space comp: 
# Only keep the last row 

def can_partition(num, sum):
    n = len(num)
    dp = [False for x in range(sum+1)]

    # handle sum=0, as we cal always have "0" sum with an empty set 
    dp[0] = True

    # with only one number, we can have a subset only when the required sum 
    # is equal to its value 
    for s in range(1, sum+1):
        dp[s] = (num[0]==s)

    # process all subsets for all sums 
    for i in range(1,n):
        for s in range(sum, -1, -1):
            # if dp[s] == True, this means we can get the sum "s" without num[i]
            # hence we can move on to the next number else we can conclude num[i]
            # and see we can find a subset to get the remining sum 
            if (not dp[s]) and (s >= num[i]):
                dp[s] = dp[s - num[i]]
            
    return dp[sum], dp


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))

main()
