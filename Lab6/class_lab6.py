class ChuNhat():
    def __init__(self, _dai=0, _rong=0):
        self.dai = _dai
        self.rong = _rong

    def get_chu_vi(self):
        return (self.dai + self.rong) * 2

    def get_dien_tich(self):
        return self.dai * self.rong
    
    def __str__(self) -> str: 
        return f"{self.dai:^10} {self.rong:^10} {self.get_chu_vi():^10} {self.get_dien_tich():^10}"
    
class HinhVuong(ChuNhat):
    def __init__(self,_canh = 0):
        self.canh=_canh
        super().__init__(self.canh, self.canh)
        

    def __str__(self) -> str: 
        return f"{self.canh:^10} {self.get_chu_vi():^10} {self.get_dien_tich():^10}"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Class bài 2
        
class SinhVienPoly():
    def __init__(self,_ten = "", _nganh = ""):
        self.ho_ten = _ten
        self.nganh = _nganh
    
    def get_diem(self):
        pass
    
    def get_hoc_luc(self):
        hoc_luc = ""
        if self.get_diem() < 5  :
            hoc_luc= "Yếu"
        elif self.get_diem() < 7 :
            hoc_luc = "Trung Bình"
        elif self.get_diem() < 8 :
            hoc_luc = "Khá"
        elif self.get_diem() < 9 :
            hoc_luc = "Giỏi"
        elif self.get_diem() <= 10:
            hoc_luc = "Xuất sắc"
        else: 
            print("Điểm không hợp lệ !")
        return hoc_luc
    
    def nhap_sv(self):
        print ("Nhập thông tin sinh viên :")
        self.ho_ten = input("Nhập họ tên sinh viên : ")
        return self
        
    def xuat(self) :
        print (f"{self.ho_ten:^20} {self.nganh:^12} {self.get_diem():^10} {self.get_hoc_luc():^10} ")
        

class SinhVienIT(SinhVienPoly):
    def __init__(self,  _ten = "", _nganh = "IT", _java=0, _html=0, _css=0):
        super().__init__(_ten, _nganh)
        self.java = _java
        self.html = _html
        self.css = _css
    
    def nhap_sv(self):
        super().nhap_sv()
        while True:
            try:
                self.html = float(input("Nhập điểm HTML : "))
                if self.html > 0 and  self.html <= 10:
                    break
                else:
                    print("Vui lòng nhập điểm trong khoảng 0-10")
            except ValueError :
                print("Vui lòng nhập đúng định dạng!")
                
        while True:
            try:
                self.java = float(input("Nhập điểm JAVA : "))
                if self.java >= 0 and self.java <= 10:
                    break
                else:
                    print("Vui lòng nhập điểm trong khoảng 0-10")
            except ValueError :
                print("Vui lòng nhập đúng định dạng!")
                
        while True:
            try:
                self.css = float(input("Nhập điểm CSS : "))
                if self.css >= 0 and  self.css <= 10:
                    break
                else:
                    print("Vui lòng nhập điểm trong khoảng 0-10")
            except ValueError :
                print("Vui lòng nhập đúng định dạng!")
        return self

    def get_diem(self):
        return  round((2 * self.java + self.html + self.css) / 4 ,2)

class SinhVienBiz(SinhVienPoly):
    def __init__(self, _ten = "", _nganh = "BIZ", _marketing = 0, _sales = 0):
        super().__init__(_ten, _nganh)
        self.marketing = _marketing
        self.sales = _sales
        
    def nhap_sv(self):
        super().nhap_sv()
        while True:
            try:
                self.marketing = float(input("Nhập điểm Marketing : "))
                if self.marketing >= 0 and  self.marketing <= 10:
                    break
                else:
                    print("Vui lòng nhập điểm trong khoảng 0-10")
            except ValueError :
                print("Vui lòng nhập đúng định dạng!")
        while True:
            try:
                self.sales = float(input("Nhập điểm Sales : "))
                if self.sales >= 0 and  self.sales <= 10:
                    break
                else:
                    print("Vui lòng nhập điểm trong khoảng 0-10")
            except ValueError :
                print("Vui lòng nhập đúng định dạng!")
        return self
        
    def get_diem(self):
        return round((2 * self.marketing + self.sales) / 3,2)
    
    
#++++++++++++++++++++++++++++++++++++
#Class bài 4:
class QuanLySinhVien():
    def __init__ (self,):
        self.danh_sach_sinh_vien=[]
    def them_sinh_vien(self, sv):
        self.danh_sach_sinh_vien.append(sv)
        
    def nhap_ds_sinh_vien(self):
        while True:
            print("\nLoại sinh viên muốn nhập:")
            print(" 1 : Sinh viên IT")
            print(" 2 : Sinh viên Biz")
            print(" 3 : Thoát nhập sinh viên ")    
            while True:
                try:
                    lua_chon = int(input("Nhập lựa chọn : "))
                    if lua_chon in [1,2,3]:
                        break
                    else:
                        print("Vui lòng chọn đúng chức năng!")
                except ValueError:
                    print("Vui lòng nhập giá trị hợp lệ !!")
            match lua_chon:
                case 1:
                    sv = SinhVienIT().nhap_sv()
                    self.them_sinh_vien(sv)
                case 2:
                    sv = SinhVienBiz().nhap_sv()
                    self.them_sinh_vien(sv)
                case 3:
                    print("Thoát nhập sinh viên!")
                    break
        return self
                    

        
    def xuat_danh_sach(self):
        print("\nDanh sách sinh viên")
        print(f"{"Họ và tên":^20} {"Ngành học":^12} {"Điểm":^10} {"Học lực":^10}"  )
        for sv in self.danh_sach_sinh_vien:
            sv.xuat()
            
    def sap_xep_diem(self):
        self.danh_sach_sinh_vien.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print("Đã sắp xếp!")
        
    def xuat_sv_hoc_luc_gioi(self):
        print("\nDanh sách sinh viên học lực Giỏi")
        print(f"{"Họ và tên":^20} {"Ngành học":^12} {"Điểm":^10} {"Học lực":^10}"  )
        for sv in self.danh_sach_sinh_vien:
            if sv.get_hoc_luc() == "Giỏi":
                sv.xuat()
            
        
        