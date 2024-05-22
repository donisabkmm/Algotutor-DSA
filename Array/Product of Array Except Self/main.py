"""
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[I].
The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.
You must write an algorithm that runs in O(n) time and without
using the division operation.
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""
from typing import List

testcase = [{"nums":[1,2,3,4]},
            {"nums":[2,3,4,5]},
            {"nums":[5,6,7,8,9]},
            {"nums":[9,10,11,12]}]



class ProductOfArray:
    def product_list(self,nums:List[int])->int:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        answer = [1] * n
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = left_product[i] * right_product[i]
        return answer



model = ProductOfArray()

for i in range(len(testcase)):
    print(model.product_list(testcase[i]["nums"]))