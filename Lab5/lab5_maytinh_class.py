import math
from datetime import datetime

class MayTinh:
    def __init__(self):
        # Lưu lịch sử dưới dạng list[dict]
        self.lich_su_tong_quat = []

    # ====== CÁC CHỨC NĂNG ======
    def phep_tinh_co_ban(self):
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
            lua_chon = input("Nhập lựa chọn (1-5): ")

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
            else:
                print("Lựa chọn không hợp lệ.")
        return lich_su

    def luy_thua(self):
        lich_su = {}
        while True:
            try:
                co_so = int(input("Nhập cơ số: "))
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ.")
        while True:
            try:
                so_mu = int(input("Nhập số mũ: "))
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ.")
        ket_qua = co_so ** so_mu
        print(f"{co_so}^{so_mu} = {ket_qua}")
        lich_su[f"{co_so}^{so_mu}"] = ket_qua
        return lich_su

    def can_bac_hai(self):
        lich_su = {}
        while True:
            try:
                x = float(input("Nhập số không âm x: "))
                if x < 0:
                    print("Vui lòng nhập số không âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
        ket_qua = math.sqrt(x)
        print(f"Kết quả: √{x} = {ket_qua}")
        lich_su[f"√{x}"] = ket_qua
        return lich_su

    def ham_luong_giac(self):
        lich_su = {}
        while True:
            ten_ham = input("Nhập hàm lượng giác (sin, cos, tan): ").strip().lower()
            try:
                x = float(input("Nhập góc (đơn vị độ): "))
            except ValueError:
                print("Góc không hợp lệ.")
                continue

            rad = math.radians(x)
            if ten_ham == "sin":
                ket_qua = math.sin(rad)
            elif ten_ham == "cos":
                ket_qua = math.cos(rad)
            elif ten_ham == "tan":
                ket_qua = math.tan(rad)
            else:
                print("Hàm lượng giác không hợp lệ.")
                continue

            print(f"Kết quả: {ten_ham}({x}) = {ket_qua}")
            lich_su[f"{ten_ham}({x})"] = ket_qua
            break
        return lich_su

    def logarit(self):
        lich_su = {}
        while True:
            loai = input("Nhập loại logarit (log10, ln, log_a): ").strip().lower()
            if loai == "log10":
                x = float(input("Nhập số x (x > 0): "))
                if x > 0:
                    kq = math.log10(x)
                    print(f"Kết quả: log10({x}) = {kq}")
                    lich_su[f"log10({x})"] = kq
                    break
                else:
                    print("x phải > 0.")
            elif loai == "ln":
                x = float(input("Nhập số x (x > 0): "))
                if x > 0:
                    kq = math.log(x)
                    print(f"Kết quả: ln({x}) = {kq}")
                    lich_su[f"ln({x})"] = kq
                    break
                else:
                    print("x phải > 0.")
            elif loai == "log_a":
                x = float(input("Nhập số x (x > 0): "))
                a = float(input("Nhập cơ số a (a > 0 và a != 1): "))
                if x > 0 and a > 0 and a != 1:
                    kq = math.log(x, a)
                    print(f"Kết quả: log_{a}({x}) = {kq}")
                    lich_su[f"log_{a}({x})"] = kq
                    break
                else:
                    print("x > 0, a > 0 và a ≠ 1.")
            else:
                print("Loại logarit không hợp lệ.")
        return lich_su

    def phuong_trinh_bac_hai(self):
        lich_su = {}
        print("Giải phương trình bậc hai ax^2 + bx + c = 0")
        while True:
            try:
                a = float(input("Nhập hệ số a (a ≠ 0): "))
                if a == 0:
                    print("a không được bằng 0.")
                    continue
                break
            except ValueError:
                print("Giá trị không hợp lệ.")
        while True:
            try:
                b = float(input("Nhập hệ số b: "))
                break
            except ValueError:
                print("Giá trị không hợp lệ.")
        while True:
            try:
                c = float(input("Nhập hệ số c: "))
                break
            except ValueError:
                print("Giá trị không hợp lệ.")

        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
            lich_su[f"{a}x^2 + {b}x + {c}"] = f"x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            print(f"Phương trình có nghiệm kép: x = {x}")
            lich_su[f"{a}x^2 + {b}x + {c}"] = f"x = {x}"
        else:
            print("Phương trình vô nghiệm.")
            lich_su[f"{a}x^2 + {b}x + {c}=0"] = "Vô nghiệm"
        return lich_su

    def phuong_trinh_bac_nhat(self):
        lich_su = {}
        print("Giải phương trình bậc nhất ax + b = 0")
        while True:
            try:
                a = float(input("Nhập hệ số a (a ≠ 0): "))
                if a == 0:
                    print("a không được bằng 0.")
                    continue
                break
            except ValueError:
                print("Giá trị không hợp lệ.")
        while True:
            try:
                b = float(input("Nhập hệ số b: "))
                break
            except ValueError:
                print("Giá trị không hợp lệ.")

        x = -b / a
        print(f"Nghiệm của phương trình: x = {x}")
        lich_su[f"{a}x + {b}"] = f"x = {x}"
        return lich_su

    def xuat_lich_su(self):
        print("Lịch sử các phép tính:")
        if not self.lich_su_tong_quat:
            print("(Trống)")
            return
        for lich_su in self.lich_su_tong_quat:
            for phep_tinh, ket_qua in lich_su.items():
                print(f"Phép tính: {phep_tinh}  |  Kết quả: {ket_qua}")

    @staticmethod
    def thoi_gian_hien_tai():
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print("Thời gian hiện tại:", formatted_time)
        return formatted_time

    
    def menu(self):
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
            try:
                lua_chon = int(input("Vui lòng chọn một tùy chọn (1-10): "))
            except ValueError:
                print("Giá trị nhập vào không phải số nguyên.")
                continue

            if lua_chon == 1:
                self.lich_su_tong_quat.append(self.phep_tinh_co_ban())
            elif lua_chon == 2:
                self.lich_su_tong_quat.append(self.luy_thua())
            elif lua_chon == 3:
                self.lich_su_tong_quat.append(self.can_bac_hai())
            elif lua_chon == 4:
                self.lich_su_tong_quat.append(self.ham_luong_giac())
            elif lua_chon == 5:
                self.lich_su_tong_quat.append(self.logarit())
            elif lua_chon == 6:
                self.lich_su_tong_quat.append(self.phuong_trinh_bac_hai())
            elif lua_chon == 7:
                self.lich_su_tong_quat.append(self.phuong_trinh_bac_nhat())
            elif lua_chon == 8:
                self.xuat_lich_su()
            elif lua_chon == 9:
                self.thoi_gian_hien_tai()
            elif lua_chon == 10:
                print("Kết thúc chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ.")


def main():
    mt = MayTinh()
    mt.menu()


