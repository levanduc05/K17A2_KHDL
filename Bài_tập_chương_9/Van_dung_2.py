def am_lich(nam_duong: int) -> str:
    if nam_duong%10:
      can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    if nam_duong%12:
        chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    return can[nam_duong % 10] + " " + chi[nam_duong % 12]
nam_duong = 2017
print("Năm âm lịch tương ứng với năm dương lịch", nam_duong, "là", am_lich(nam_duong))