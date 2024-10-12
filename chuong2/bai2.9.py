import json
sinhvien = {"ten": "Nguyen Van A","age": 19,"truong": "uneti"}
sv = json.dumps(sinhvien, indent =4)
print(sv)
print(type(sv))
