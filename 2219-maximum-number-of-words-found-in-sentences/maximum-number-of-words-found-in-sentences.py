class Solution(object):
    def mostWordsFound(self, sentences):
        maxx = 0 

        for sentence in sentences:
            words = sentence.split()
            count = len(words)

            maxx=max(maxx,count)

        return maxx    