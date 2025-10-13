import math
#Bai 1:
def tinh_tien_nuoc():
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    so_luong_nuoc = int(input("Nhập số lượng nước đã sử dụng: "))
    if so_luong_nuoc <= 10:
        tien_nuoc = so_luong_nuoc * gia_ban_nuoc[0]
    elif so_luong_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_luong_nuoc - 10) * gia_ban_nuoc[1]
    elif so_luong_nuoc <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_luong_nuoc - 20) * gia_ban_nuoc[2]   
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_luong_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc

#Bai 2:

def tinh_nguyen_lieu(nguyen_lieu):
    duong=0
    dau=0
    for key in nguyen_lieu.keys():
        duong+=nguyen_lieu[key][2]*nguyen_lieu[key][0]
        dau+=nguyen_lieu[key][2]*nguyen_lieu[key][1]
    return round(duong,3),round(dau,3)
def nguyen_lieu():
    print("Chương trình tính nguyên liệu làm bánh")
    sl_banh_dau_xanh=int(input("Nhập số lượng bánh đậu xanh: "))
    sl_banh_thap_cam=int(input("Nhập số lượng bánh thập cẩm: "))
    sl_banh_deo=int(input("Nhập số lượng bánh dẻo: "))

    nguyen_lieu={
        "banh_dau_xanh":[0.04,0.07,sl_banh_dau_xanh],
        "banh_thap_cam":[0.06,0,sl_banh_thap_cam],
        "banh_deo":[0.05,0.02,sl_banh_deo]
    }

    duong,dau=tinh_nguyen_lieu(nguyen_lieu)
    khoi_luong_nguyen_lieu={
        "Duong":duong,
        "Dau": dau
    }
    
    print(f"Khối lượng đường: {khoi_luong_nguyen_lieu["Duong"]} kg\nKhối lượng đậu: {khoi_luong_nguyen_lieu["Dau"]} kg")

# nguyen_lieu()
#Bai 3:
def so_chan():
    my_list=[]
    so_luong_so_nguyen=int(input("Nhập số lượng số nguyên: "))
    i=0
    while i < so_luong_so_nguyen:
        try:
            so_nguyen=int(input(f"Nhập số nguyên thứ {i+1}: "))
            my_list.append(so_nguyen)
            i+=1
        except ValueError:
            print("Giá trị nhập vào không phải số nguyên, vui lòng thử lại")
            continue
    print("Danh sách các số nguyên vừa nhập là: ",my_list)

    new_list = list(filter(lambda x: (x % 2 == 0) , my_list))
    return new_list


#bai 4: menu
def menu():
    while True:    
        print("~~~~~~~~~~~~~~~Menu~~~~~~~~~~~~~~~")
        print("|1. Tính tiền nước sinh hoạt     |")
        print("|2. Tính nguyên liệu làm bánh    |")
        print("|3. Tìm số chẵn trong danh sách  |")
        print("|4. Kết thúc chương trình        |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while True:
            try:
                lua_chon = int(input("Vui lòng chọn một tùy chọn (1-4): "))
                if lua_chon in [1, 2, 3,4]:
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
                    continue
                    
            except ValueError:
                print("Giá trị nhập vào không phải số nguyên, vui lòng thử lại")
                continue
        
        match lua_chon:
            case 1:
                tien_nuoc=tinh_tien_nuoc()
                print(f"Số tiền nước phải trả là: {tien_nuoc:,} VND")
            case 2:
                nguyen_lieu()
            case 3:
                new_list=so_chan()
                print("Danh sách các số chẵn là: ",new_list)
            case 4:
                print("Kết thúc chương trình.")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
# menu()



#=================================================
#Hàm máy tính bỏ túi
def phep_tinh_co_ban():
    lich_su = {}
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    while True:
        print("Chọn phép tính cơ bản:")
        print("1. Cộng (+)")
        print("2. Trừ (-)")
        print("3. Nhân (*)")
        print("4. Chia (/)")
        print("5. Thoát")
        lua_chon = input("Nhập lựa chọn (1-6): ")
        if lua_chon == "1":
            ket_qua = a + b
            print(f"Kết quả: {a} + {b} = {ket_qua}")
            lich_su[f"{a} + {b}"] = ket_qua
        elif lua_chon == "2":
            ket_qua = a - b
            print(f"Kết quả: {a} - {b} = {ket_qua}")
            lich_su[f"{a} - {b}"] = ket_qua 
        elif lua_chon == "3":
            ket_qua = a * b
            print(f"Kết quả: {a} * {b} = {ket_qua}")
            lich_su[f"{a} * {b}"] = ket_qua   
        elif lua_chon == "4":
            if b != 0:
                ket_qua = a / b
                print(f"Kết quả: {a} / {b} = {ket_qua}")
                lich_su[f"{a} / {b}"] = ket_qua 
            else:
                print("Lỗi: Không thể chia cho 0.")    
        elif lua_chon == "5":
            print("Thoát phép tính cơ bản.")
            break
        return lich_su
    
def luy_thua():
    lich_su={}
    while True:
        try:
            co_so = int(input("Nhập cơ số"))
            break
        except  ValueError:
            print("Vui lòng nhập số nguyên hợp lệ") 
            continue 
    while True:
        try:
            so_mu = int(input("Nhập số mũ"))
            break
        except  ValueError:
            print("Vui lòng nhập số nguyên hợp lệ") 
            continue 
    print(f"{co_so}^{so_mu} = {co_so**so_mu}")
    lich_su[f'{co_so}^{so_mu}']=co_so**so_mu
    return lich_su

def can_bac_hai():
    lich_su={}
    while True:
        try:
            x = float(input("Nhập số dương x: "))
            break
        except ValueError:
            print("Vui lòng nhập số dương!")
            continue
    ket_qua = math.sqrt(x)
    print(f"Kết quả: √{x} = {ket_qua}")
    lich_su[f"√{x}"]=ket_qua
    return lich_su
    
def ham_luong_giac():
    lich_su={}
    while True:
        ham_luong_giac=input("Nhập hàm lượng giác (sin, cos, tan): ")
        x = float(input("Nhập góc (đơn vị độ): "))
        radian = math.radians(x) #đổi độ sang radian
        if ham_luong_giac == "sin":
            ket_qua=math.sin(radian)
            print(f"Kết quả: sin({x}) = {ket_qua}")
            break
        elif ham_luong_giac == "cos":
            ket_qua = math.cos(radian)
            print(f"Kết quả: cos({x}) = {ket_qua}")
            break
        elif ham_luong_giac == "tan":
            ket_qua = math.tan(radian)
            print(f"Kết quả: tan({x}) = {ket_qua}")
            break
        else:
            print("Hàm lượng giác không hợp lệ.")
            continue
    lich_su[f"{ham_luong_giac}({x})"]=ket_qua
    return lich_su

def logarit():
    lich_su={}
    while True:
        loai_log=input("Nhập loại logarit (log10, ln, log_a): ")
        if loai_log == "log10":
            x = float(input("Nhập số x (x > 0): "))
            if x > 0:
                ket_qua = math.log10(x)
                print(f"Kết quả: log10({x}) = {ket_qua}") 
                lich_su[f"log10({x})"]=ket_qua
                break
            else:
                print("Lỗi: x phải lớn hơn 0.")
                continue
        elif loai_log == "ln":
            x=float(input("Nhập số x (x > 0): "))
            if x > 0:
                ket_qua = math.log(x)
                print(f"Kết quả: ln({x}) = {ket_qua}")
                lich_su[f"ln({x})"]=ket_qua
                break
            else:
                print("Lỗi: x phải lớn hơn 0.")
                continue
                
        elif loai_log == "log_a" :
            x = float(input("Nhập số x (x > 0): "))
            a = float(input("Nhập cơ số a (a > 0 và a != 1): "))
            if x > 0 and a > 0 and a != 1 :
                ket_qua=math.log(x,a)
                print(f"Kết quả: log_{a}({x}) = {ket_qua}")
                lich_su[f"log_{a}({x})"]=ket_qua
                break
            else:
                print("Lỗi: x phải lớn hơn 0, a phải lớn hơn 0 và khác 1.")
                continue
                
        else:
            print("Loại logarit không hợp lệ.")
            continue
    return lich_su

def phuong_trinh_bac_hai():
    lich_su={}
    print("Giải phương trình bậc hai ax^2 + bx + c = 0")
    while True:
        try:
            a = float(input("Nhập hệ số a (a ≠ 0): "))
            if a == 0:
                print("Hệ số a không được bằng 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")
            continue
    while True:
        try:
            b = float(input("Nhập hệ số b: "))
            break
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")
            continue
    while True:
        try:
            c = float(input("Nhập hệ số c: "))
            break
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")
            continue

    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
        lich_su[f"{a}x^2 + {b}x + {c}"] = f"x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
        lich_su[f"{a}x^2 + {b}x + {c}"]=f"x = {x}"
    else:
        print("Phương trình vô nghiệm.")
        lich_su[f"{a}x^2 + {b}x + {c}=0"]="Vô nghiệm"
    return lich_su

def phuong_trinh_bac_nhat():
    lich_su={}
    print("Giải phương trình bậc nhất ax + b = 0")
    while True:
        try:
            a = float(input("Nhập hệ số a (a ≠ 0): "))
            if a == 0:
                print("Hệ số a không được bằng 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")
            continue
    while True:
        try:
            b = float(input("Nhập hệ số b: "))
            break
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")
            continue

    x = -b / a
    print(f"Nghiệm của phương trình là: x = {x}")
    lich_su[f"{a}x + {b}"]=f"x = {x}"
    return lich_su

def xuat_lich_su(lich_su_tong_quat):
    print("Lịch sử các phép tính:")
    for lich_su in lich_su_tong_quat:
        for phep_tinh, ket_qua in lich_su.items():
            print(f"Phép tính :{phep_tinh}  Kết quả {ket_qua}")
        
def thoi_gian_hien_tai():
    from datetime import datetime
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Thời gian hiện tại:", formatted_time)
    return formatted_time

def menu_may_tinh():
    lich_su_tong_quat = []
    while True:
        print("~~~~~~~~~~~~~~~Menu Máy Tính Bỏ Túi~~~~~~~~~~~~~~~")
        print("|1. Phép tính cơ bản                             |")
        print("|2. Lũy thừa                                     |")
        print("|3. Căn bậc hai                                  |")
        print("|4. Hàm lượng giác (sin, cos, tan)               |")
        print("|5. Logarit (log10, ln, log_a)                   |")
        print("|6. Phương trình bậc hai                         |")
        print("|7. Phương trình bậc nhất                        |")
        print("|8. Xem lịch sử các phép tính                    |")
        print("|9. Hiển thị thời gian hiện tại                  |")
        print("|10. Kết thúc chương trình                       |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        while True:
            try:
                lua_chon = int(input("Vui lòng chọn một tùy chọn (1-10): "))
                if lua_chon in range(1, 11):
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
                    continue
            except ValueError:
                print("Giá trị nhập vào không phải số nguyên, vui lòng thử lại")
                continue
        
        match lua_chon:
            case 1:
                lich_su = phep_tinh_co_ban()
                lich_su_tong_quat.append(lich_su)
            case 2:
                lich_su = luy_thua()
                lich_su_tong_quat.append(lich_su)
            case 3:
                lich_su = can_bac_hai()
                lich_su_tong_quat.append(lich_su)
            case 4:
                lich_su = ham_luong_giac()
                lich_su_tong_quat.append(lich_su)
            case 5:
                lich_su = logarit()
                lich_su_tong_quat.append(lich_su)
            case 6:
                lich_su = phuong_trinh_bac_hai()
                lich_su_tong_quat.append(lich_su)
            case 7:
                lich_su = phuong_trinh_bac_nhat()
                lich_su_tong_quat.append(lich_su)
            case 8:
                    xuat_lich_su(lich_su_tong_quat)
            case 9:
                thoi_gian_hien_tai()
            case 10:
                print("Kết thúc chương trình.")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
                
