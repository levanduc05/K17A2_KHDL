#1
a = float(input("Nhập số cần tính bình phương: "))
if a > 0:
    b =a**2
    print(f"Bình phương của {a} là {b}")
else:
    print("Số bạn nhập không phải số dương.")
#2
n=int(input("Nhập 1 số nguyên bất kỳ:"))
print("các số nguyên từ 1 đến ",n,"là:")
for i in range(1,n+1):
    print(i)
#3
m = int(input("Nhập số tự nhiên m:"))
n = int(input("Nhập số tự nhiên n (n>m):"))
if m>= n:
    print("Vui lòng nhập m<n.")
else:
    print(f"Các số chia hết cho m trong khoảng từ 1 đến {n} là:")
    for i in range(1, n+1):
        if i % m ==0:
            print(i)
#4
number1 = float(input("Nhập số thứ nhất:"))
number2 = float(input("Nhập số thứ hai:"))
number3 = float(input("Nhập số thứ ba:"))
max_number = max(number1, number2, number3)
print("Số lớn nhất trong ba số là:", max_number)
#5
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return a * b // ucln(a, b)
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
result_bcnn = bcnn(num1, num2)
print(f"Bội chung nhỏ nhất của {num1} và {num2} là: {result_bcnn}")

#7
def tinh_tong_chu_so(N):
    chuoi_so = str(N)
    tong = 0
    for chu_so in chuoi_so:
        tong += int(chu_so)

    return tong

so_nguyen = int(input("Nhập số nguyên N:"))
ket_qua = tinh_tong_chu_so(so_nguyen)
print("Tổng các chữ số của", so_nguyen, "là:", ket_qua)