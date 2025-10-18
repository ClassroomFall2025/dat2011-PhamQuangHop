from datetime import datetime
import os



class TaiKhoan ():
    def __init__ (self,soTaiKhoan="",ten="",loai="",soDu=0):
        self.soTaiKhoan=soTaiKhoan
        self.ten=ten
        self.loai=loai
        self.soDu=soDu
    
    def setSoDu (self):
        if self.loai == 'T':
            while True:
                try:
                    soDu=int(input("Nhập số dư ban đầu (>=500000): ")) 
                    if soDu >= 500000:
                        self.soDu = soDu
                        break
                    else:
                        print("Số dư ban đầu phải >= 500.000 VND, vui lòng nhập lại")
                except:
                    print("Số tiền nhập không hợp lệ, vui lòng nhập lại")
        elif self.loai == 'C':
            while True:
                try:
                    soDu=int(input("Nhập số dư ban đầu (>=1000000): ")) 
                    if soDu >= 1000000:
                        self.soDu = soDu
                        break
                    else:
                        print("Số dư ban đầu phải >= 1.000.000 VND, vui lòng nhập lại")
                except:
                    print("Số tiền nhập không hợp lệ, vui lòng nhập lại")
                    
                   
        
    def tao_tai_khoan (self,):
        while True:
            try:
                self.soTaiKhoan=int(input("Nhập số tài khoản: "))
                if self.soTaiKhoan<0:
                    print("Số tài khoản phải là số nguyên dương, vui lòng nhập lại")  
                if any (self.soTaiKhoan == tk.soTaiKhoan for tk in danh_sach_tai_khoan.danhSachTaiKhoan):
                    print("Số tài khoản đã tồn tại, vui lòng nhập lại")
                else:
                    break
            except:
                print("Số tài khoản phải là số nguyên dương, vui lòng nhập lại")
                
        self.ten=input("Nhập tên chủ tài khoản: ")
        while True:
            self.loai=input("Nhập loại tài khoản (T / C): ")  
            if self.loai in ['T','C']:
                break
            else:
                print("Loại tài khoản không hợp lệ, vui lòng nhập lại")
        self.setSoDu()
        print("Tài khoản đã được tạo thành công \n")
        
        
        
    
    def napTien (self):
        while True:
            try:
                soTienNap=int(input("Nhập số tiền nạp: "))
                break
            except:
                print("Số tiền nạp không hợp lệ, vui lòng nhập lại")
        if soTienNap>0:
            self.soDu += soTienNap
            print("Nạp tiền thành công")
        else:
            print("Số tiền nạp không hợp lệ")
            
    def rutTien (self):
        while True:
            try:
                soTienRut=int(input("Nhập số tiền rút: "))
                break
            except:
                print("Số tiền rút không hợp lệ, vui lòng nhập lại")
        if self.loai == "T":
            if self.soDu - soTienRut >= 500000:
                self.SoDu -= soTienRut
                print("Rút tiền thành công \n")
            else:
                print("Số dư không đủ để rút tiền, số dư tối thiểu phải là 500.000 VND")
        elif self.loai == "C":
            if self.soDu - soTienRut >= 1000000:
                self.soDu -= soTienRut
                print("Rút tiền thành công")
            else:
                print("Số dư không đủ để rút tiền, số dư tối thiểu phải là 1.000.000 VND")
    
    def kiemTraSoDu (self):
        print(f"Số dư hiện tại : {self.soDu:,} VND")
        
    def chinhSuaThongTin (self):
        self.ten=input("Nhập tên chủ tài khoản mới: ")
        while True:
            self.loai=input("Nhập loại tài khoản mới (T / C): ")  
            if self.loai in ['T','C']:
                break
            else:
                print("Loại tài khoản không hợp lệ, vui lòng nhập lại")
        print("Chỉnh sửa thông tin thành công")
    
    def xuatThongTin (self):
        return f"| {self.soTaiKhoan:^15} | {self.ten:^20} | {self.loai:^10} | {self.soDu:^15,} VND  |"
    
    def toDict(self):
        return {
            "Số tài khoản": self.soTaiKhoan,
            "Tên": self.ten, 
            "Loại tài khoản": self.loai,
            "Số dư": self.soDu
        }
        
    
    
class QuanLyTaiKhoan():
    def __init__ (self):
        self.danhSachTaiKhoan=[]
    
    def themTaiKhoan (self):
        taiKhoan=TaiKhoan()
        taiKhoan.tao_tai_khoan()
        self.danhSachTaiKhoan.append(taiKhoan)
        
    def luuFile (self):
        with open("taikhoan.csv","w",encoding="utf-8") as f:
            f.write(f"{'Số TK'},{'Tên chủ TK'},{'Loại TK'},{'Số dư':}\n")
            for taiKhoan in self.danhSachTaiKhoan:
                f.write(f"{taiKhoan.soTaiKhoan},{taiKhoan.ten},{taiKhoan.loai},{taiKhoan.soDu} VND\n")
                
    
                
    def timTheoSoTaiKhoan (self,soTaiKhoan):
        
        for taiKhoan in self.danhSachTaiKhoan:
            if taiKhoan.soTaiKhoan == soTaiKhoan:
                return taiKhoan
        return None
    
    def timTheoTen (self):
        ten=input("Nhập tên chủ tài khoản cần tìm: ")
        ketQua=[]
        for taiKhoan in self.danhSachTaiKhoan:
            if taiKhoan.ten.lower() == ten.lower():
                ketQua.append(taiKhoan)
                taiKhoan.xuatThongTin()
        if len(ketQua) == 0:
            print("Không tìm thấy tài khoản nào")
        else:
            print(f"Tìm thấy {len(ketQua)} tài khoản")
            print("="*78)
            print(f'| {"Số TK":^15} | {"Tên chủ TK":^20} | {"Loại TK":^10} | {"Số dư":^20} |')
            for taiKhoan in ketQua:
                print(taiKhoan.xuatThongTin())
    
    
    def xuatDanhSachTaiKhoan (self):
        print("Danh sách tài khoản hiện có:")
        print("="*78)
        print(f"| {'Số TK':^15} | {'Tên chủ TK':^20} | {'Loại TK':^10} | {'Số dư':^20} |")
        print("-"*78)
        for taiKhoan in self.danhSachTaiKhoan:
            print(taiKhoan.xuatThongTin())
        print("="*78)
            
    def dongTaiKhoan (self,soTaiKhoan):
        taiKhoan=self.timTheoSoTaiKhoan(soTaiKhoan)
        if taiKhoan is not None:
            self.danhSachTaiKhoan.remove(taiKhoan)
            print("Đóng tài khoản thành công")
        else:
            print("Không tìm thấy tài khoản cần đóng")

    def taoFileBaoCao (self):
        with open("BaoCao.txt","w",encoding="utf-8") as f:
            f.write("="*120 + "\n")
            f.write(f"{'Tổng số tài khoản':^20} | {'Tổng số dư':^30} | {'Số tài khoản T':^20} | {'Số tài khoản C':^20} | {'Thời gian':^20} |\n")
            
    def xuatBaoCao (self):
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y : %H-%M-%S")
        if os.path.exists("BaoCao.txt") == False:
            self.taoFileBaoCao()
        with open("BaoCao.txt","a",encoding="utf-8") as f:
            tongSoTaiKhoan=len(self.danhSachTaiKhoan)
            tongSoDu=int(sum(taiKhoan.soDu for taiKhoan in self.danhSachTaiKhoan))
            soTaiKhoanTietKiem=sum(1 for taiKhoan in self.danhSachTaiKhoan if taiKhoan.loai=='T')
            soTaiKhoanCaNhan=sum(1 for taiKhoan in self.danhSachTaiKhoan if taiKhoan.loai=='C')
            f.write("-"*120 + "\n")
            f.write(f"{tongSoTaiKhoan:^20} | {tongSoDu:^25,} VND  | {soTaiKhoanTietKiem:^20} | {soTaiKhoanCaNhan:^20} | {timestamp:^20} |\n")
            print("Xuất báo cáo thành công!")
     
    
    @staticmethod     
    def saoLuuDuLieu():
        os.makedirs("backup", exist_ok=True)
        now = datetime.now()
        timestamp = now.strftime("%d%m%Y_%H%M%S")
        if os.path.exists("taikhoan.csv"):
            file=open ("taikhoan.csv","r",encoding="utf-8") 
            danhSach=file.read()
            file_path="backup/taikhoan"+timestamp +".csv"
            with open (file_path,"w",encoding="utf-8") as newfile:
                newfile.write(danhSach)
                print("Sao lưu thành công!")
        else:
            print("File chưa tồn tại , sao lưu thất bại !")
    
        
    
    @staticmethod            
    def docFileVaoDanhSach ():
        pass
    
    
danh_sach_tai_khoan = QuanLyTaiKhoan()