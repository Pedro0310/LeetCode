class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        left, right = 0, len(nums1)

        while left <= right:
            part1 = (left + right) // 2
            part2 = half_len - part1

            max_left1 = nums1[part1 - 1] if part1 > 0 else -float('inf')
            min_right1 = nums1[part1] if part1 < len(nums1) else float('inf')

            max_left2 = nums2[part2 - 1] if part2 > 0 else -float('inf')
            min_right2 = nums2[part2] if part2 < len(nums2) else float('inf')

            # Check for valid partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is odd
                if total_len % 2 != 0:
                    return min(min_right1, min_right2)
                # If total length is even
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0

            # Move partition to the left
            elif max_left1 > min_right2:
                right = part1 - 1
            # Move partition to the right
            else:
                left = part1 + 1