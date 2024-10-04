class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")
    def __str__(self):
       return f"{self.day}/{self.month}/{self.year}"

class Employees():
    def __init__(self, ho_ten , ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty
    def display(self):
        print("ho và tên: ",self.ho_ten)
        print("ngay sinh: ",self.ngay_sinh)
        print("ngay vao cong ty: ",self.ngay_vao_cong_ty)
class Company(Employees):
    def __init__(self):
        self.employees = []
    def add_employees(self,employees):
        self.employees.append(employees)
    def display_all(self):
        for emp in self.employees:
            emp.display()
birth_date_1 = Date(25, 6, 1990)
start_date_1 = Date(9, 3, 2015)
emp1 = Employees("Nguyễn Văn A", birth_date_1, start_date_1)


birth_date_2 = Date(22, 8, 2001)
start_date_2 = Date(12, 11, 2010)
emp2 = Employees("Nguyễn Văn B", birth_date_2, start_date_2)

company = Company()
company.add_employees(emp1)
company.add_employees(emp2)

company.display_all()