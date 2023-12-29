def so_nguyen_to(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
x = int(input("Nhập một số: "))
if so_nguyen_to(x):
    print(x,"là số ngueyen tố")
else:
    print(x, "không phải là số nguyên tố.")