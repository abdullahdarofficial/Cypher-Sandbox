
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays nums1 and nums2 in-place.
        Modify nums1 in-place to contain the sorted elements.
        """
        # Start from the end of both arrays
        p1, p2 = m - 1, n - 1
        # Start from the end of the nums1 array where it has extra space
        p = m + n - 1
        
        # While there are still elements to compare in nums2 and nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are still elements in nums2, copy them to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]