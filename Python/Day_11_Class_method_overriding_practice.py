class grandparent:
    def land(self):
        return "10 acre land"
class father(grandparent):
    def land(self):
        return "5 acre land"
class son(father):
    def land(self):
        return "3 acre land"
a=son()
print(a.land())

