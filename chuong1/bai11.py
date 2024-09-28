import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_tamgiac(self):
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)
    
    def chu_vi(self):
        if not self.is_tamgiac():
            return -1  # Trả về mã lỗi nếu không hợp lệ
        return self.a + self.b + self.c

    def dien_tich(self):
        if not self.is_tamgiac():
            return -1  # Trả về mã lỗi nếu không hợp lệ
        s = self.chu_vi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Tam_giac_vuong(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def is_tamgiacvuong(self):
        if not self.is_tamgiac():
            return False
        return (self.a ** 2 + self.b ** 2 == self.c ** 2 or
                self.a ** 2 + self.c ** 2 == self.b ** 2 or
                self.b ** 2 + self.c ** 2 == self.a ** 2)


class Tam_giac_can(Triangle):
    def __init__(self, a, b):
        super().__init__(a, a, b) 

    def is_tamgiaccan(self):
        if not self.is_tamgiac():
            return False
        return self.a == self.b or self.a == self.c or self.b == self.c


class Tam_giac_deu(Tam_giac_can):
    def __init__(self, a):
        super().__init__(a, a) 

    def is_tamgiacdeu(self):
        """Kiểm tra tam giác có phải tam giác đều không"""
        if not self.is_tamgiac():
            return False
        return self.a == self.b == self.c

obj1 = Triangle(2,3,4)
if obj1.is_tamgiac():
    print("diện tích tam giác là: ",obj1.dien_tich)
    print("chu vi tam giác là: ",obj1.chu_vi)
else:
    print("tam giác kh hợp lệ")

obj2 = Tam_giac_vuong(3,4,5)
if obj2.is_tamgiacvuong():
    print("diện tích tam giác là: ",obj2.dien_tich)
    print("chu vi tam giác là: ",obj2.chu_vi)
else:
    print("kh phải tam giác vuông")


obj3 = Tam_giac_can(4,5)
if obj3.is_tamgiaccan():
    print("diện tích tam giác là: ",obj3.dien_tich)
    print("chu vi tam giác là: ",obj3.chu_vi)
else:
    print("không phải tam giác đều")

