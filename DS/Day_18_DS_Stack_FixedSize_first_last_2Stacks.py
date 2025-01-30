#stack top1 from first and top2 from last(cut by half)
class tftl:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1#start
        self.top2=n#end
    def push1(self,data):
        if self.top1 < self.top2-1:
            self.top1+=1
            self.arr[self.top1]=data
            print(f"Pushed {data} into stack1")
        else:
            print("Stack1 is Over flow")
    def push2(self,data):
        if self.top1 < self.top2-1:
            self.top2-=1
            self.arr[self.top2]=data
            print(f"Pushed {data} into stack2")
        else:
            print("Stack1 is Over flow")
    def pop1(self):
        if self.top1 >= 0:
            data = self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            print(f"Popped {data} from stack1")
        else:
            print("Stack1 is empty")
    def pop2(self):
        if self.top2 < self.size:
            data = self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2+=1
            print(f"Popped {data} from stack2")
        else:
            print("Stack2 is empty")
    def display(self):
        print(f"Array: {self.arr}")
        print(f"Stack1: {self.arr[:self.top1+1]}")
        print(f"Stack2: {self.arr[self.top2:]}")
s = tftl(8)
s.display()
s.push1(10)
s.push2(20)
s.display()
s.push1(30)
s.push2(40)
s.display()
s.pop2()
s.display()
#Balancing of symbols
#Infix to Postfix/Prefix conversion
