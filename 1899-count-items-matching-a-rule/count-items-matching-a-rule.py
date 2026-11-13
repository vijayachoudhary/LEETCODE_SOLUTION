class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        
        count = 0
        index = {'type':0,'color':1,'name':2}    

        for item in items:
            if item[index[ruleKey]] == ruleValue:
                count +=1
        return count        