"""
Given an array of integer nums and an integer target, return
indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


testcase = [{
    "nums" : [2,7,11,15],
    "target": 9
},{
    "nums" : [3,6,8,9,2],
    "target": 11
},{
    "nums" : [2,3,5,9,7],
    "target": 8
},{
    "nums" : [1,8,9,13,15],
    "target": 28
},{
    "nums" : [2,8,3,6,5],
    "target": 9
}]

def twosum(nums,target):
    hash_table = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[num] = i
    return []

for i in range(len(testcase)):
    data = testcase[i]
    result = twosum(data["nums"],data["target"])
    print(result)
