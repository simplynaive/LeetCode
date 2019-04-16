import copy

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # for i in range(len(nums)):
    #     temp = copy.deepcopy(nums)
    #     temp.remove(temp[i])
    #     if target - nums[i] in temp:
    #         return [i, temp.index(target - nums[i]) + 1]
    #     # if nums[i] <= target:
    #     #     for j in range(len(nums)):
    #     #         if nums[i] + nums[j] == target and i != j:
    #     #             return [i, j]

    if not nums:
        return
    dic = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dic:
            return [dic[diff], i]
        else:
            dic[nums[i]] = i


def main():
    nums = [-1, -2, -3, -4, -5]
    print(twoSum(nums, -8))


if __name__ == "__main__":
    main()