'''
MS:Intern - 
Maximum Product Subarray
Given an array that contains both positive and negative integers, find the product of the maximum product subarray. Expected Time complexity is O(n) and only O(1) extra space can be used.
Examples:

Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -3, 0, -2, -40}
Output:   80  // The subarray is {-2, -40}



https://www.geeksforgeeks.org/maximum-product-subarray/
'''

'''
Time Complexity: O(n)
Auxiliary Space: O(1)
'''
'''
언제 부호가 뒤바뀔지 모르므로, 양극의 가장 큰 절댓값 max min을 둘다 기록해두는 것!
'''

def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        # else
        maxList = [nums[0]]
        minList = [nums[0]]
        for i in nums[1:]:
            #maxList[-1] == maxList[len(maxList)-1]
            mx = max(maxList[-1]*i, i, minList[-1]*i)
            mn = min(maxList[-1]*i, i, minList[-1]*i)
            maxList.append(mx)
            minList.append(mn)
        return max(maxList)
