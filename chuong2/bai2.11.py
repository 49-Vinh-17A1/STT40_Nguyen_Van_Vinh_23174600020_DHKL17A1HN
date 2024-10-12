import json
from datetime import datetime
giao_dich = []

while True:
    print("Nhập thông tin giao dịch:")
    loai_giao_dich = input("Loại giao dịch (mua laptop,mua...): ")
    so_luong = float(input("Số lượng: "))
    gia = float(input("Giá: "))
    giao_dich.append({"loai": loai_giao_dich, "so_luong": so_luong, "gia": gia})
    tiep_tuc = input("Bạn có muốn nhập thêm giao dịch? (yes/no): ")
    if tiep_tuc.lower() == 'no':
        break
print("có muốn ghi vào tập tin hay không? 1: có, 2 không")
lua_chon = input()
if lua_chon == '1':
    thoi_gian_hien_tai = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') 
    ten_tap_tin = f"{thoi_gian_hien_tai}.json"
    with open("chuong2\\{}".format(ten_tap_tin), 'w', encoding='utf-8') as file:
        json.dump(giao_dich, file, indent=4)

    print(f"Dữ liệu đã được lưu vào tệp tin {ten_tap_tin}.")
else:
    print("Dữ liệu giao dịch không được lưu.")