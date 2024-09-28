class Stack:
    def __init__(self, size):
        self.size = size      
        self.stack = []          
        self.top = -1                 


    def is_full(self):
        return self.top == self.size - 1

    def push(self, value):
        if self.is_full():
            print("Ngăn xếp đã đầy")
        else:
            self.top += 1
            self.stack.append(value)
            print(f"đã thêm {value} vào ngăn xếp")
            
    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self.stack.pop()
            self.top -= 1
            print(f"đã lấy {value} từ ngăn xếp")
            return value

    def delete(self):
        del self.stack
        print("đã xóa ngăn xếp")
    
    def count(self):
        print(f"số phần tử trên ngăn xếp là {self.top +1}")
obj1 = Stack(3)
obj1.push(6)
obj1.push(4)
obj1.push(3)
obj1.push(5)
obj1.count()
