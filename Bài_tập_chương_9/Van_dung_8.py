def la_so_hoan_hao(n):
    if n <= 0:
        return False
    tong = 0
    for i in range(1,n):
        if n%i ==0:
          tong += i
    if tong ==n:
        return True
    else:
        return False
so=int(input("NHập vào một sô : "))
if la_so_hoan_hao(so):
    print(so,"đây là số hoàn hảo")
else:
    print(so,"không phải số hoàn hảo")