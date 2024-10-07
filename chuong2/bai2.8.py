import json
nhanvien = {"name": "Nguyen Van A","age": 19,"company": "viettel"}
# Chuyển đối tượng Python thành chuỗi JSON
nv = json.dumps(nhanvien)
print(nv)
