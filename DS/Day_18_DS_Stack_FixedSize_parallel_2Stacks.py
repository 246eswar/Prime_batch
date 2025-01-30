#stack parellel(cut by half)
class TwoStackSpace:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.mid=(n+1)//2#for middle values
        self.top1=-1
        self.top2=self.mid-1
    def push1(self,data):
        if self.top1 < self.mid -1:
            self.top1+=1
            self.arr[self.top1]=data
            print(f"Pushed {data} into stack1")
        else:
            print("Stack1 is Over flow")
    def push2(self,data):
        if self.top2 < self.size -1:
            self.top2+=1
            self.arr[self.top2]=data
            print(f"Pushed {data} into stack2")
        else:
            print("Stack2 is Over flow")
    def pop1(self):
        if self.top1 >= 0:
            data = self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            print(f"Popped {data} from stack1")
        else:
            print("Stack1 is empty")
    def pop2(self):
        if self.top2 >= self.mid:
            data = self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2-=1
            print(f"Popped {data} from stack2")
        else:
            print("Stack2 is empty")
    def display(self):
        print(f"Array: {self.arr}")
        print(f"Stack1: {self.arr[:self.mid]}")
        print(f"Stack2: {self.arr[self.mid:]}")
s = TwoStackSpace(8)
s.display()
s.push1(10)
s.push2(20)
s.display()
s.push1(30)
s.push2(40)
s.display()
s.push1(50)
s.push2(60)
s.display()
s.push1(70)
s.push2(80)
s.display()
s.push1(90)
s.push2(100)
s.display()
s.pop1()
s.pop2()
s.display()
