class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # pointers for nums1, nums2 and merged array, 
        # put pointer at the end of the nums1 and nums2 (not zero)
        p1, p2, p = m-1, n-1, m+n-1
        
        """
        print(p1)
        print(nums1[p1])
        print(p2)
        if len(nums2) > 0:
            print(nums2[-1])
        else:
            print("nums2 is empty!")
        print(p)
        """

        """
        nums1 = 1,2,3,0,0,0
        nums2 = 2,5,6
        result/nums1 = 1,2,2,3,5,6
        p1 = 1
        p2 = -1 
        p = 1
        """
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are any remaining elements in nums2
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

