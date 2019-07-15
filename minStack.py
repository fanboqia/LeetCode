class MinStack:
    
    
    def __init__(self):
        # do intialization if necessary
        self.helpStack = []
        self.mainStack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if len(self.mainStack) == 0:
            self.helpStack.append(number)
            self.mainStack.append(number)
        else:
            if self.helpStack[-1] > number:
                self.helpStack.append(number)
                self.mainStack.append(number)
            else:
                self.helpStack.append(self.helpStack[-1])
                self.mainStack.append(number)
        

    """
    @return: An integer
    """
    def pop(self):
        if len(self.mainStack) == 0:
            return None
        else:
            self.helpStack.pop()
            return self.mainStack.pop()

                
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if len(self.helpStack) == 0:
            return None
        return self.helpStack[-1]
