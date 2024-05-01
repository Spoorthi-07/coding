class GF():
    def __init__(self):
        self.property=100000000
        
class F(GF):
    def __init__(self):
        super().__init__()
        self.father_property=50000000+self.property
        
class Pavan(F):
    def __init__(self):
        super().__init__()
        self.my_property=self.father_property+50000000

my_father=Pavan()
print(my_father.my_property)
