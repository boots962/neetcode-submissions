class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beginning = 0
        end = len(nums)-1
        while beginning<=end:
            mid =(beginning+end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid -1
                continue
            else:
                beginning = mid+1
        return -1
