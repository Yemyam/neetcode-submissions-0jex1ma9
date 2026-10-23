class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                slow2 = 0
                while True:
                    slow2 = nums[slow2]
                    slow = nums[slow]
                    if slow2 == slow:
                        return slow
                