class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        
        #register number map
        map = {}
        
        #return list
        list = []
        
        #distinct map
        disMap = {}
        
        #register the numbers in map
        for num in numbers:
            if map.get(num) == None:
                map[num] = 1
            else:
                map[num] = map[num] + 1
        
        for i in range(0,len(numbers)-1):
            for j in range(i+1,len(numbers)):
                #see if the other numbers being registered in the map
                target = -(numbers[i]+numbers[j])
                if numbers[i] == target and map[target] < 2:
                    continue
                if numbers[j] == target and map[target] < 2:
                    continue
                if numbers[i] == 0 and numbers[j] == 0 and map.get(target) < 3:
                    continue
                if  map.get(target) != None:
                    sortedList = sorted([numbers[i],numbers[j],target])
                    key = str(sortedList[0])+""+str(sortedList[1])+""+str(sortedList[2])
                    if disMap.get(key) == None: 
                        list.append(sortedList)
                        disMap[key] = key
        return list
                
