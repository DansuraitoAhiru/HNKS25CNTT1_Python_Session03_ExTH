from datetime import datetime  # lấy hàm ngày tháng từ thư viện datetime

patient_name = input("Nhập tên bệnh nhân: ")
birth_year = int(input("Nhập năm sinh: "))
sick_days = int(input("Nhập số ngày bị bệnh: "))
temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
fee = float(input("Nhập chi phí khám: "))

if patient_name.strip() == "":
    print("Lỗi tên đăng nhập ko được để trống")
elif birth_year<1900 or birth_year > (datetime.now().year):
    print("Lỗi: Năm sinh không hợp lệ")

elif sick_days < 0:
    print("Lỗi: Số ngày bị bệnh phải >= 0")

elif temperature < 30 or temperature > 45:
    print("Lỗi: Nhiệt độ phải từ 30 đến 45°C")

elif fee <= 0:
    print("Lỗi: Chi phí khám phải > 0")

else:
    age = datetime.now().year - birth_year
    surcharge = fee * 0.1
    total_fee = fee + surcharge

    if temperature>38 and sick_days>3:
        status = "Nguy hiểm"
    elif temperature > 38:
        status = "Sốt cao"
    elif temperature > 37.5:
        status = "Sốt nhẹ"
    else:
        status = "Bình thường"

    if status == "Nguy hiểm":
        if age > 60:
            priority = "Cấp cứu"
        else:
            priority = "Ưu tiên cao"
    else:
        priority = "Bình thường"
    
    message = "Cao" if total_fee > 500000 else "Thấp"

    print("\n--- KẾT QUẢ ---")
    print(f"Tên bệnh nhân: {patient_name}")
    print(f"Tuổi: {age}")
    print(f"Nhiệt độ: {temperature} °C")
    print(f"Số ngày bệnh: {sick_days}")

    print(f"\nTình trạng: {status}")
    print(f"Mức độ ưu tiên: {priority}")

    print(f"\nTổng chi phí: {total_fee}")
    print(f"Mức chi phí: {message}")