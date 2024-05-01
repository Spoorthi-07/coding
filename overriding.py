
class GF:
    def fun(self):
        print("Hello")
    
class F(GF):
    def fun(self):
        print("Hey")
    def mr(self):
        super().fun()
        
pavan=F()
pavan.mr()