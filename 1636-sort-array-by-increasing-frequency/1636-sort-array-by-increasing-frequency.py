class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        arr = list(freq.items())

        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):

                if arr[j][1] > arr[j + 1][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                elif arr[j][1] == arr[j + 1][1] and arr[j][0] < arr[j + 1][0]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        result = []

        for num, count in arr:
            for i in range(count):
                result.append(num)

        return result