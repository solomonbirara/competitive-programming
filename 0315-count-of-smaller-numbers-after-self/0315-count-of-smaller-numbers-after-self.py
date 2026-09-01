class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n
        arr = list(enumerate(nums))

        def merge_sort(a):
            if len(a) <= 1:
                return a

            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])

            i = j = 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    ans[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                ans[left[i][0]] += j
                merged.append(left[i])
                i += 1

            merged.extend(right[j:])
            return merged

        merge_sort(arr)
        return ans