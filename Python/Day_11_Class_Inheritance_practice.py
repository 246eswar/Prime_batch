class ravi:
    def land(self):
        return  "ravi has 10 acre land"
class somu(ravi):
    def software(self):
        return "somu has a software engineer"
a=somu()
print(a.software())
print(a.land())
