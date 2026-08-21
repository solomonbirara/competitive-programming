class Solution:

    def maxConsecutive(self, bottom, top, special):

        special.sort()

        special = [bottom - 1] + special + [top + 1]

        answer = 0

        for i in range(1, len(special)):

            answer = max(
                answer,
                special[i] - special[i - 1] - 1
            )

        return answer