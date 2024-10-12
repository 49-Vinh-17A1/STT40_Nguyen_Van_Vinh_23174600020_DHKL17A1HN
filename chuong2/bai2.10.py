import json
with open("chuong2\\nhanvien.json","r",encoding ="utf-8") as f:
    conten = f.read()
congty = json.loads(conten)
ten_cong_ty= congty["ten_cong_ty"]
dia_chi = congty["dia_chi"]
nhan_vien = congty["nhan_vien"]
print("cong ty:",ten_cong_ty)
print("dia_chi:",dia_chi)
print("----Thống kê nhân viên theo đơn vị----")
tong_so_nhan_vien = len(nhan_vien)
thong_ke_don_vi = {}
for nv in nhan_vien:
    don_vi = nv["don_vi"]
    if don_vi in thong_ke_don_vi:
        thong_ke_don_vi[don_vi] += 1
    else:
        thong_ke_don_vi[don_vi] = 1
print(f"Tên công ty: {ten_cong_ty}")
print(f"Địa chỉ: {dia_chi}")
print(f"Tổng số nhân viên: {tong_so_nhan_vien}\n")
print("Thống kê nhân viên theo đơn vị:")
for don_vi, so_nhan_vien in thong_ke_don_vi.items():
    ti_le = (so_nhan_vien / tong_so_nhan_vien) * 100
    print(f"Đơn vị: {don_vi}, Số nhân viên: {so_nhan_vien}, Tỷ lệ: {ti_le}%")