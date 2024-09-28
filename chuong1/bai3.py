class PS():
    def __init__(self,tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        if not self.kiem_tra_hop_le():
            print("Mẫu số phải khác 0")
            self.mau_so=1
    def kiem_tra_hop_le(self):
        return self.mau_so != 0
    def nhap_thong_tin(self):
        self.tu_so = int(input("nhập tử số: " ))
        self.mau_so = int(input("nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            print("mẫu số phải khác 0")
            self.mau_so = int(input("nhập mẫu số: "))
    def in_phan_so(self):
        if self.tu_so == 0:
            print(" phân số: 0") 
        else:
            print(f"phân số: {self.tu_so}/{self.mau_so}") 
      
ps = PS()
ps.nhap_thong_tin()
ps.in_phan_so()


    
    
