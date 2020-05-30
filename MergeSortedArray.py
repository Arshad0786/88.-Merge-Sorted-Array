class Solution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        output = []
        while (
            i < m and j < n
        ):  # compare them til one of the Index hit the end of the list
            if nums1[i] > nums2[j]:
                output.append(nums2[j])
                j = j + 1
            elif nums1[i] < nums2[j]:
                output.append(nums1[i])
                i = i + 1
            else:
                output.append(nums1[i])
                i = i + 1
        while i < m:  # if the left over is nums1, put rest of nums1 to output
            output.append(nums1[i])
            i = i + 1
        while j < n:  # if the left over is nums2, put rest of nums2 to output
            output.append(nums2[j])
            j = j + 1
        # overwrite output to nums1 since the problem require us to, instead of returning a list
        for i in range(len(nums1)):
            nums1[i] = output[i]
