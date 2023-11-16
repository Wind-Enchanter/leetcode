class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_num = []
        self.cnt = {}


    def push(self, x: int) -> None:
        self.stack.append(x)
        if x in self.cnt.keys():
            self.cnt[x] += 1
        else:
            self.cnt[x] = 1
        if self.sorted_num == []:
            self.sorted_num.append(x)
        else:
            i = 0
            while i < len(self.sorted_num) and x > self.sorted_num[i]:
                i += 1
            if i == len(self.sorted_num):
                self.sorted_num.append(x)
            else:
                self.sorted_num = self.sorted_num[0:i]+[x]+self.sorted_num[i:]


    def pop(self) -> None:
        temp = self.stack.pop()
        self.cnt[temp] -= 1
        i = 0

        while len(self.sorted_num)>=1 and self.cnt[self.sorted_num[0]] == 0:
            self.sorted_num = self.sorted_num[1:]


    def top(self) -> int:
        return self.stack[len(self.stack)-1]


    def getMin(self) -> int:
        return self.sorted_num[0]