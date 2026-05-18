import sys
name_patient = input ("Nhập tên bệnh nhân : ")
year_btd = int(input("Nhập năm sinh:"))
day = int(input("Nhập số ngày bị bệnh:"))
temperature = float(input("Nhập nhiệt độ cơ thể:"))
price = float(input("Nhập chi phí khám"))
text_messenger = False
priority_level = False
text_price = False


if name_patient == "":
    print("Lỗi! Không được để trống tên")
    sys.exit()
elif year_btd < 1900 or year_btd > 2024:
    print("Lỗi! Năm sinh không hợp lệ")
    sys.exit()
elif day <= 0:
    print("Lỗi! Ngày bị bệnh phải lớn hơn 0")
    sys.exit()
elif temperature < 30 or temperature > 45:
    print("Lôi! Nhiệt độ phải trong khoảng 30-45")
    sys.exit()
elif price <= 0:
    print("Lỗi! Chi phí khám phải lớn hơn 0")
    sys.exit()
else:
    age = 2026 - year_btd
    surcharge = price * 0.1
    total_price = price + surcharge
    if temperature > 38 and day > 3:
        text_messenger = "Nguy hiểm"
        if age > 60:
            priority_level = "Cấp cứu"
        else:
            priority_level = "Ưu tiên cao"
    elif temperature > 38:
        text_messenger = "Sốt cao"
        priority_level = "Bình thường"
    elif temperature > 37.5:
        text_messenger = "Sốt nhẹ"
        priority_level = "Bình thường"
    else:
        text_messenger = "Bình thường"
        priority_level = "Bình thường"
    if total_price > 500000:
        text_price = "Cao"
    else:
        text_price = "Thấp"

print(f"""---KẾT QUẢ
      Tên: {name_patient}
      Tuổi: {age}
      Nhiệt độ: {temperature} độ C
      Số ngày bệnh: {day}

      Tình trạng: {text_messenger}
      Mức độ ưu tiên: {priority_level}

      Tổng chi phí: {total_price} VND
      Mức chi phí: {text_price}
    """)







