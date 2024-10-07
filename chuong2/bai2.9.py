import json
# Đối tượng Python (đối tượng JSON)
sinhvien = {"ten": "Nguyen Van A","age": 19,"truong": "uneti"}
# Chuyển đối tượng Python thành chuỗi JSON
sv = json.dumps(sinhvien, indent =4)
print(sv)
print(type(sv))
