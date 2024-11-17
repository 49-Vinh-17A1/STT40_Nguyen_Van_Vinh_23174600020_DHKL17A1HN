class TS():
    
    def __init__(self,ho_ten="", toan=0, ly=0, hoa=0):
        self.ho_ten = ho_ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.danh_sach_thi_sinh = []
    def nhap_thong_tin(self):
        self.ho_ten = input("nhap ho ten: ")
        self.toan  = float(input("nhap diem toan: "))
        self.ly    = float(input("nhap diem ly: "))
        self.hoa   = float(input("nhap diem hoa: "))
    def in_thong_tin(self):
        print("ho va ten thi sinh: {}".format(self.ho_ten))
        print("diem toan: {}".format(self.toan))
        print("diem hoa : {}".format(self.hoa))
        print("diem ly : {}".format(self.ly))
    def tong_diem(self):
        return self.toan + self.ly + self.hoa
    def nhap_danh_sach_thi_sinh(self):
        flag = True
        while flag:
            thi_sinh = TS()
            thi_sinh.nhap_thong_tin()
            if thi_sinh.tong_diem() >= 20:
                self.danh_sach_thi_sinh.append(thi_sinh)
            hoi = input("Có nhập tiếp không? (Yes/No): ")
            if hoi.lower() == "no":
                flag = False
              
    def in_danh_sach_thi_sinh(self):
        """In danh sách các thí sinh đạt tổng điểm >= 20"""
        print("Danh sách thí sinh đủ điểm:")
        for ts in self.danh_sach_thi_sinh:
            ts.in_thong_tin()
            print("Tổng điểm: {}\n".format(ts.tong_diem()))

quan_ly_thi_sinh = TS()
quan_ly_thi_sinh.nhap_danh_sach_thi_sinh()
quan_ly_thi_sinh.in_danh_sach_thi_sinh()
    