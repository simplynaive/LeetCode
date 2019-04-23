class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.dic[number] = self.dic.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.dic:
            diff = value - n
            if diff in self.dic and (diff != n or self.dic[n] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(0)
param_1 = obj.find(0)
obj.add(0)
param_2 = obj.find(0)
print(param_1, param_2)