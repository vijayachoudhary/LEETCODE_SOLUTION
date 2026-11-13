class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxx = max(candies)
        result = []

        for candy in candies:
            if candy+extraCandies >= maxx:
                result.append(True)
            else:
                result.append(False)
        return result