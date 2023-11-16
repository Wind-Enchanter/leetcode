num_list = ['0','1','2','3','4','5','6','7','8','9']

class Automation:
    def __init__(self):
        self.state = 'start'
        self.result = False
        self.node_cnt = 0
        self.num_before_node = 0
        self.table = {
            'start':['start','signed','num','end','node','end'],
            'signed':['end','end','num','end','node','end'],
            'node':['end','end','num','end','end','end'],
            'num':['end','end','num','more','node','end'],
            'more':['end','zz-signed','zz','end','end','end'],
            'zz-signed':['end','end','zz','end','end','end'],
            'zz':['end','end','zz','end','end','end'],
            'end':['end','end','end','end','end','end']
        }
    def get_col(self,c):
        if c == " ":
            return 0
        elif c == "+" or c == "-":
            return 1
        elif c in num_list:
            return 2
        elif c == "e" or c == "E":
            return 3
        elif c == ".":
            self.node_cnt += 1
            return 4
        else:
            return 5

    def change_state(self,c):
        if c in num_list and self.node_cnt == 0:
            self.num_before_node = 1

        if self.state == 'node':
            if c == "e" or c == "E":
                if self.num_before_node == 1:
                    self.state = 'more'
                    return
                else:
                    self.state = self.table[self.state][self.get_col(c)]
                    return

        if self.state == 'num':
            if_node = self.get_col(c)
            if if_node == 4 and self.node_cnt==1:
                self.state = self.table[self.state][if_node]
            elif if_node == 4 and self.node_cnt > 1:
                self.state = 'end'
            else:
                self.state = self.table[self.state][self.get_col(c)]
        else:
            self.state = self.table[self.state][self.get_col(c)]

class Solution:
    def validNumber(self, s: str) -> bool:
        true_state = ['num','zz']
        s = s.strip()
        if not s:return False
        my_auto = Automation()
        for i in s:
            my_auto.change_state(i)
        if my_auto.node_cnt > 1:
            return False
        elif my_auto.state in true_state:
            return True
        elif my_auto.state == 'node' and my_auto.num_before_node == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    my_so = Solution()
    temp = "46.e3"
    print(my_so.validNumber(temp))