class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        arr = []
        self.flat(arr,nestedList)
        return arr
    
    def flat(self,arr,nestedList):
        for item in nestedList:
            if isinstance(item,list):
                self.flat(arr,item)
            else:
                arr.append(item)
