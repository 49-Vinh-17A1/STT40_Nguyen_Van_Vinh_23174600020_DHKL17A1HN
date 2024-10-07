import json
with open("chuong2\\nhanvien.json","r",encoding ="utf-8") as f:
    conten = f.read()
congty = json.loads(conten)
ten_cong_ty= congty["ten_cong_ty"]
dia_chi = congty["dia_chi"]
nhan_vien = congty["nhan_vien"]
print("cong ty:",ten_cong_ty)
print("dia_chi:",dia_chi)
print("Nhan vien:",nhan_vien)
