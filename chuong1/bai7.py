class Date():
    def __init__(self, day=7, month =9, year = 2005):
        self.day = day
        self.month = month
        self.year = year
    def Display(self):
        print(f"{self.day}/{self.month}/{self.year}")
    def nam_nhuan(self):
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                return True
            return False

    def days_in_month(self):
        if self.month in [4, 6, 9, 11]:
            return 30 
        elif self.month == 2:
            if self.nam_nhuan():
                return 29 
            else:
                return 28
        else:
            return 31
    def next_day(self):
        if self.day < self.days_in_month():
            self.day +=1
        else:
            self.day = 1
            if self.month <= 12:
                self.month +=1
            else:
                self.month = 1
                self.year +=1
ngay = Date(7,9,2005)
ngay.Display()

ngay.next_day()
ngay.Display() 