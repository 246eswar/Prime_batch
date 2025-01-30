#1.single inheritance
'''class ravi:
    def land(self):
        return  "ravi has 10 acre land"
class somu(ravi):
    def software(self):
        return "somu has a software engineer"
a=somu()
print(a.software())
print(a.land())'''
#2.Multiple Inheritance
'''class ravi:
    def land(self):
        return  "ravi has 10 acre land"
class somu:
    def software(self):
        return "somu has a software engineer"
class minu(ravi,somu):
    def student(self):
        return "minu is a B.Tech Student"
b=minu()
print(b.student())
print(b.software())'''
#3.multilevel inheritance
'''class ravi:
    def land(self):
        return  "ravi has 10 acre land"
class somu(ravi):
    def software(self):
        return "somu has a software engineer"
class minu(somu):
    def student(self):
        return "minu is a B.Tech Student"
b=minu()
print(b.student())
print(b.software())'''
#4.hierarchical inheritance
class ravi:
    def land(self):
        return  "ravi has 10 acre land"
class somu(ravi):
    def software(self):
        return "somu has a software engineer"
class toni(ravi):
    def software(self):
        return "somu has a software engineer"    
class minu(ravi):
    def student(self):
        return "minu is a B.Tech Student"
b=minu()
print(b.student())
print(b.land())








