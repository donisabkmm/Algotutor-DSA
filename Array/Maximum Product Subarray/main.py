"""
Given an integer array nums, find a subarray that has the largest
product, and return the product.
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a
subarray.
"""
from typing import List


testcases = [{"nums":[2,3,-2,4]},
             {"nums":[-2,0,-1]}]

class ProductOfMaxArray:
    def MaxValue(self,nums: List[int]) -> int:
        minValue = nums[0]
        maxValue = nums[0]
        result = nums[0]

        for num in nums[1:]:
            if num < 0:
                maxValue,minValue = minValue,maxValue
            maxValue = max(num,maxValue*num)
            minValue = min(num,minValue*num)
            result = max(result,maxValue)
        return result

model = ProductOfMaxArray()

for i in range(len(testcases)):
    print(model.MaxValue(nums=testcases[i]["nums"]))





