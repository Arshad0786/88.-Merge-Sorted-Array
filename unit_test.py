import unittest
from MergeSortedArray_Dev import Solution


class MergeSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.nums1 = [1, 2, 3, 0, 0, 0]
        self.m = 3
        self.nums2 = [2, 5, 6]
        self.n = 3
        temp.merge(self.nums1, self.m, self.nums2, self.n)
        self.assertEqual(self.nums1, [1, 2, 2, 3, 5, 6])

    def test_nums1_ahead(self):
        temp = Solution()
        self.nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0]
        self.m = 9
        self.nums2 = [10, 11, 12]
        self.n = 3
        temp.merge(self.nums1, self.m, self.nums2, self.n)
        self.assertEqual(self.nums1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_nums2_ahead(self):
        temp = Solution()
        self.nums1 = [10, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.m = 3
        self.nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.n = 9
        temp.merge(self.nums1, self.m, self.nums2, self.n)
        self.assertEqual(self.nums1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


if __name__ == "__main__":
    unittest.main()
