from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
        
        n = len(nums)
        for i in range(n):
            # print(abs(nums[i]) - 1)
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                print(-nums[index])
                nums[index] = -nums[index]
        
        return [i + 1 for i in range(n) if nums[i] > 0]

def sortedSquares(nums: List[int]) -> List[int]:
        print([x * x for x in nums])
        return [x * x for x in nums].sort()

if __name__ == "__main__":
    
    nums = [4,3,2,7,8,2,3,1]
    result_list = findDisappearedNumbers(nums)
    print(result_list)
    
    nums2 = [-4,-1,0,3,10]
    result_list2 = sortedSquares(nums2)
    print(result_list2)