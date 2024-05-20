"""
3. Contains Duplicate
Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is
distinct.
Input: nums = [1,2,3,1]
Output: true
"""
from typing import List

testcases = [{"nums":[1,2,3,1]},
             {"nums":[2,3,1,5,8,1,2]},
             {"nums":[2,1,3,4,4,0]},
             {"nums":[0,2,5,1,3]}]



class duplicates:
    def check_duplicate(self,nums: List[int])->int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

model = duplicates()
for i in range(len(testcases)):
    print(model.check_duplicate(nums=testcases[i]["nums"]))
