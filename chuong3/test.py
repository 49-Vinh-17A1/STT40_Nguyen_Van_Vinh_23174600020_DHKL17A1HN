import numpy as np
np_position = np.loadtxt('chuong3\positions.txt',dtype=str, delimiter=',')
np_heights = np.loadtxt('chuong3\heights.txt',dtype=str, delimiter=',')
position = np.reshape(np_position,(20,1))
heights = np.reshape(np_heights,(20,1))
arr = np.hstack((position,heights))
mask = np.any(arr == 'GK', axis=1)  # Kiểm tra xem 'GK' có ở bất kỳ cột nào trong mỗi hàng không
arr_gk = arr[mask]  # Lọc các hàng có chứa 'GK'
heights_gk = arr_gk[::][1:]
print(heights_gk)