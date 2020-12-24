class calculator:
    def __init__(self, list):
        self.list = list
    def sum(self):
        result = 0
        for num in self.list:
            result += num
        return result
    def avg(self):
        total = self.sum()
        return total / len(self.list)
