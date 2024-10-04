class square():
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong
    def chuvi(self):
        chuvi= (self.dai + self.rong)*2
        return chuvi
    def dien_tich(self):
        S = self.dai * self.rong
        return S
    def thong_tin(self):
        print("chieu dai: {},chieu rong: {}, chu vi: {},dien tich: {}".format(self.dai,self.rong,self.chuvi(),self.dien_tich()))
obj = square(4,5)
obj.thong_tin() 
