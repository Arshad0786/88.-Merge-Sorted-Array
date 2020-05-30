class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        tail = len(nums1) - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[tail] = nums2[j]
                j = j - 1
            else:
                nums1[tail] = nums1[i]
                i = i - 1
            tail = tail - 1
        while j >= 0:
            nums1[tail] = nums2[j]
            j = j - 1
            tail = tail - 1
