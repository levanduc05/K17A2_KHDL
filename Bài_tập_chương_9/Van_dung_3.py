def bmi(chiều_cao: float, cân_nặng: float) -> float:
    return cân_nặng / (chiều_cao *chiều_cao)
chiều_cao= float(input("Nhập chiều cao của bạn (m): "))
cân_nặng = float(input("Nhập cân nặng của bạn (kg): "))
bmi_value = bmi(chiều_cao, cân_nặng)
print(f"Chỉ số BMI của bạn là {bmi_value:.2f}")
if bmi_value < 18.5:
    print("Bạn bị gầy!")
elif bmi_value < 25:
    print("Bạn đang bình thường!")
elif bmi_value < 30:
    print("Bạn bị thừa cân")