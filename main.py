import numpy as np

# ============================================
#  HƯỚNG DẪN CƠ BẢN THƯ VIỆN NUMPY
# ============================================

# --- 1. Tạo mảng (Array) ---
print("=== 1. Tạo mảng ===")
a = np.array([1, 2, 3, 4, 5])           # mảng 1 chiều
b = np.array([[1, 2, 3], [4, 5, 6]])    # mảng 2 chiều

print("Mảng 1 chiều:", a)
print("Mảng 2 chiều:\n", b)

# --- 2. Các hàm tạo mảng đặc biệt ---
print("\n=== 2. Mảng đặc biệt ===")
print("Mảng toàn số 0:", np.zeros(5))
print("Mảng toàn số 1:", np.ones(4))
print("Mảng từ 0 đến 9:", np.arange(10))
print("Mảng 10 số từ 1 đến 100:", np.linspace(1, 100, 10))
print("Ma trận đơn vị 5x5:\n", np.eye(5))

# --- 3. Thuộc tính của mảng ---
print("\n=== 3. Thuộc tính mảng ===")
print("Kích thước (shape):", a.shape)
print("Số chiều (ndim):", a.ndim)
print("Tổng phần tử (size):", a.size)
print("Kiểu dữ liệu (dtype):", a.dtype)

# --- 4. Thay đổi hình dạng mảng ---
print("\n=== 4. Thay đổi hình dạng ===")
c = np.arange(12)
print("Mảng gốc:", c)
print("Reshape 3x4:\n", c.reshape(3, 4))
print("Reshape 4x3:\n", c.reshape(4, 3))

# --- 5. Truy cập phần tử (Indexing & Slicing) ---
print("\n=== 5. Truy cập phần tử ===")
arr = np.array([10, 20, 30, 40, 50])
print("Phần tử đầu:", arr[0])
print("Phần tử cuối:", arr[-1])
print("Từ vị trí 1 đến 3:", arr[1:4])

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Phần tử hàng 3, cột 3:", mat[2, 2])
print("Hàng đầu tiên:", mat[0])
print("Cột thứ 2:", mat[:, 1])

# --- 6. Phép toán trên mảng ---
print("\n=== 6. Phép toán ===")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Cộng:", x + y)
print("Trừ:", x - y)
print("Nhân:", x * y)
print("Chia:", x / y)
print("Lũy thừa:", x ** 2)

# --- 7. Các hàm toán học ---
print("\n=== 7. Hàm toán học ===")
data = np.array([1, 2, 3, 4, 5])
print("Tổng:", np.sum(data))
print("Trung bình:", np.mean(data))
print("Độ lệch chuẩn:", np.std(data))
print("Giá trị lớn nhất:", np.max(data))
print("Giá trị nhỏ nhất:", np.min(data))
print("Căn bậc 2:", np.sqrt(data))

# --- 8. Phép toán ma trận ---
print("\n=== 8. Phép toán ma trận ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Nhân ma trận:\n", B @ A)           # hoặc np.dot(A, B)
print("Chuyển vị:\n", A.T)
print("Định thức:", np.linalg.det(A))

# --- 9. Mảng ngẫu nhiên ---
print("\n=== 9. Mảng ngẫu nhiên ===")
print("Ngẫu nhiên [0,1):", np.random.rand(5))
print("Ngẫu nhiên số nguyên:", np.random.randint(1, 100, size=5))
print("Phân phối chuẩn:", np.random.randn(5))

# --- 10. Lọc với điều kiện (Boolean Indexing) ---
print("\n=== 10. Lọc với điều kiện ===")
scores = np.array([45, 78, 92, 35, 88, 67, 55])
print("Điểm số:", scores)
print("Điểm >= 60:", scores[scores >= 60])
print("Số lượng đạt:", np.sum(scores >= 60))

# --- 11. Ghép và tách mảng ---
print("\n=== 11. Ghép và tách mảng ===")
m = np.array([1, 2, 3])
n = np.array([4, 5, 6])
print("Ghép ngang:", np.concatenate([m, n]))
print("Xếp dọc:\n", np.vstack([m, n]))
print("Xếp ngang:\n", np.hstack([m, n]))

# --- 12. Sắp xếp ---
print("\n=== 12. Sắp xếp ===")
unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("Mảng gốc:", unsorted)
print("Sắp xếp tăng:", np.sort(unsorted))
print("Vị trí sắp xếp:", np.argsort(unsorted))
