class Solution(object):
    def nodesBetweenCriticalPoints(self, head):

        positions = []
        index = 1

        prev = head
        curr = head.next

        while curr.next:

            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                positions.append(index)

            prev = curr
            curr = curr.next
            index += 1

        if len(positions) < 2:
            return [-1, -1]

        min_dist = float('inf')

        for i in range(1, len(positions)):
            min_dist = min(min_dist, positions[i] - positions[i-1])

        max_dist = positions[-1] - positions[0]

        return [min_dist, max_dist]