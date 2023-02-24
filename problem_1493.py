'''
Author: Alice
Date: 2023-02-24 00:48:17
LastEditors: Alice
LastEditTime: 2023-02-24 16:24:27
Description: 
'''
from typing import List
import copy
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return merge_ones(nums,get_ones_index(nums))
def get_zeros(nums: List[int]) -> int:
    zeros = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros.append(i)
    return zeros

def nums_filter(nums: List[int], index: int) -> List[int]:
    new_nums = copy.deepcopy(nums)
    new_nums.pop(index)
    return new_nums

def get_long(nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        if nums[i]==1:
            ones = 0
            nums_after = nums[i:]
            for j in nums_after:
                if j==0:
                    break
                if j==1:
                    ones = ones + 1
            if ones >= res:
                res = ones
    return res

def get_ones_index(nums: List[int]) -> int:
    flag = 0
    index1 = 0
    index2 = 0
    ones_list = []
    for i in range(len(nums)):
        if (flag == 0) & (nums[i]==1):
            index1 = i
            index2 = i
            flag = 1
        if (flag == 1) & (nums[i]==1):
            index2 = i
            if (i+1==len(nums)):
                ones_list.append([index1,index2])
                flag = 0
            elif (i+1<len(nums)) & (nums[i+1]==0):
                ones_list.append([index1,index2])
                flag = 0
        i = i + 1
    return ones_list
def merge_ones(nums,ones_list):
    if len(ones_list)==1:
        if((ones_list[0][1] - ones_list[0][0] + 1)==len(nums)):
            return len(nums) - 1
    result = 0
    for i in range(len(ones_list)):
        temp_long = 0
        temp_long = ones_list[i][1] - ones_list[i][0] + 1
        if temp_long > result:
            result = temp_long
        if (i+1<len(ones_list)):
            if ((ones_list[i][1]+2)==ones_list[i+1][0]):
                temp_long = (ones_list[i][1]-ones_list[i][0]+1)+(ones_list[i+1][1]-ones_list[i+1][0]+1)
                # print(temp_long)
                if temp_long > result:
                    result = temp_long
    return result
        
def test01():
    s = Solution()
    nums = [1,1,1]
    print(s.longestSubarray(nums))
    
def test02():
    s = Solution()
    nums = [0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0]
    ones_list = get_ones_index(nums)
    print(ones_list)
    print(merge_ones(nums,ones_list))
    
def test03():
    temp = [[1, 6], [8, 10]]
    print(temp[0][1]+2)
    print(temp[1][0])
    print(len(temp[0]))
    print(len(temp[0])+len(temp[1]))
if __name__ == "__main__":
    test01()


    


