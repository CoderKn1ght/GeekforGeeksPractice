def remove_duplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if not nums:
        return 0
    insertion_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[insertion_index] = nums[i]
            insertion_index += 1
    return insertion_index
