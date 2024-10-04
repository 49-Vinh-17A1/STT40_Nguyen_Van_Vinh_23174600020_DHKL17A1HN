class da_giac():
    def dien_tich(self):
        raise NotImplementedError("Phương thức này cần được định nghĩa trong lớp con.")
    def chu_vi(self):
        raise NotImplementedError("Phương thức này cần được định nghĩa trong lớp con.")
class Hinh_binh_hanh(da_giac):
    def __init__(self, day_lon,day_be, chieu_cao):
        self.day_lon = day_lon
        self.day_be = day_be
        self.chieu_cao = chieu_cao
    def chu_vi(self):
        chuvi= (self.day_be + self.day_lon)*2
        return chuvi
    def dien_tich(self):
        S = self.day_lon * self.chieu_cao
        return S
class Hinh_chu_nhat(Hinh_binh_hanh):
    def __init__(self, dai, rong):
        super().__init__(dai, rong)
        self.dai = dai
        self.rong = rong
    def chu_vi(self):
        chuvi = (self.dai +self.rong)*2
        return chuvi
    def dien_tich(self):
        S = self.dai * self.rong
        return S
class Hinh_vuong(Hinh_chu_nhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh
    def dien_tich(self):
        S = self.canh*self.canh
        return S
    def chu_vi(self):
        chuvi = self.canh*4
        return chuvi
hinh_binh_hanh = Hinh_binh_hanh(day_lon= 9, day_be =6, chieu_cao=5)
print("Chu vi hình bình hành:", hinh_binh_hanh.chu_vi())
print("Diện tích hình bình hành:", hinh_binh_hanh.dien_tich())

hinh_chu_nhat = Hinh_chu_nhat(9,7)
print("chu vi hình chữ nhật: ",hinh_chu_nhat.chu_vi())
print("diện tích hình chữ nhật: ",hinh_chu_nhat.dien_tich())
hinh_vuong = Hinh_vuong(5)
print("chu vi hình vuông: ",hinh_vuong.chu_vi())
print("diện tích hình vuông: ",hinh_vuong.dien_tich()) 