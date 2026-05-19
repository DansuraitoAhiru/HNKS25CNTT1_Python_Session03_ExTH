is_continue = ""
while is_continue != 'n':
    employee_number = int(input("\nNhập số lượng nhân viên: "))
    if employee_number <= 0:
        print("Hãy nhập 1 số > 0 để điền thông tin")
    for i in range (1, employee_number+1):
        print(f"\nNhân viên {i}")
        name = input("Nhập tên nhân viên: ")
        work_days = int(input("Nhập số ngày đi làm: "))

        print("Thông tin nhân viên:")
        print(f"Tên: {name}")
        print(f"Số ngày đi làm: {work_days}")

        if work_days < 0:
            print("Số ngày đi làm không được âm")
        elif work_days < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")
    
    is_continue = input("\nTiếp tục chương trình? (y/n): ")

print("\nChương trình kết thúc")