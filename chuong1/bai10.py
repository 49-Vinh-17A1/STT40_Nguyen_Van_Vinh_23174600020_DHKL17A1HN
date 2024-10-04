import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Điểm có tọa độ ({self.x}, {self.y})")


class Elip(Point):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y)
        self.ban_truc_lon = ban_truc_lon  
        self.ban_truc_nho = ban_truc_nho  

    def dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho  

    def display(self):
        return (f"Elip với tọa độ tâm ({self.x}, {self.y}), "
                f"bán trục lớn {self.ban_truc_lon}, bán trục nhỏ {self.ban_truc_nho}, "
                f"diện tích {self.dien_tich()}")


class obj2(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r) 
        self.r = r

    def dien_tich(self):
        return math.pi * (self.r**2)

    def display(self):
        return (f"Đường tròn với tọa độ tâm ({self.x}, {self.y}), "
                f"bán kính {self.r}, diện tích {self.dien_tich()}")
obj1 = Elip(0, 2, 4, 5)
print(obj1.display())

obj2 = obj2(1, 1, 7)
print(obj2.display())    