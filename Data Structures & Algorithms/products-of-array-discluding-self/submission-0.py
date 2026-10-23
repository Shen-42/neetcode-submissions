class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprefix = [1] * len(nums)
        rightprefix = [1] * len(nums)
        answer = []

        for i in range(1, len(nums)):
            leftprefix[i] = leftprefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rightprefix[i] = rightprefix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            answer.append(leftprefix[i] * rightprefix[i])

        return answer
