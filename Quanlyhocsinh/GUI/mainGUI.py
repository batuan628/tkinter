from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from GUI.menuGUI import *
from GUI.lophocGUI import *
from GUI.khoilopGUI import *
from GUI.hockyGUI import * 
from GUI.namhocGUI import *
from GUI.monhocGUI import *
from GUI.diemGUI import *
from GUI.ketquaGUI import *
from GUI.hoclucGUI import *
from GUI.hanhkiemGUI import *
from GUI.hocsinhGUI import *

class MainGui:
    def __init__(self,root):
        self.root = root
        self.root.title("QUAN LY HOC SINH".center(350))
        self.root.geometry("1200x700+300+100")

        
        global notebook_tab
        
        thanhcongcu = Frame(self.root,highlightbackground="black",bg="#9CAACA")
        thanhcongcu.place(x=0,y=0,width=1200,height=30)

        banghienthi = Frame(self.root,bg="#CDC9C9",)
        banghienthi.place(x=0,y=130,width=1200,height=550)
        
        thongtin = Frame(self.root,highlightbackground="black",highlightthickness=1,bg="#5D478B")
        thongtin.place(x=0,y=680,width=1200,height=20)
        
        notebook_tab=ttk.Notebook(banghienthi,width=1200,height=545)
        notebook_tab.grid()
        Label(thongtin,bg="#5D478B",text="Người dùng đang đăng nhập: ",font=("arial",10),fg="white").grid(row=0)
        
        self.quanly = Frame(self.root,highlightbackground="black",highlightthickness=1,bg="#CCFFFF")
        self.quanly.place(x=0,y=30,width=1200,height=100)
        self.thongke = Frame(self.root,highlightbackground="black",highlightthickness=1,bg="#CCFFFF")
        self.thongke.place(x=0,y=30,width=1200,height=100)
        self.quydinh = Frame(self.root,highlightbackground="black",highlightthickness=1,bg="#CCFFFF")
        self.quydinh.place(x=0,y=30,width=1200,height=100)
        
        self.bghinhnen=Image.open("hinhanh\hinh nen.jpg").resize((1200,530))
        self.hinhnen=ImageTk.PhotoImage(self.bghinhnen)
        hienthi=Label(notebook_tab,bg="#CDC9C9",image=self.hinhnen)
        hienthi.grid(pady=20,padx=0)
        #
        
    
        #===================================================================================================#
        self.bghome=ImageTk.PhotoImage(file=r"D:\bt\file\PY\tkinter\hinhanh\start.png")
        self.home_button = Button(thanhcongcu,image=self.bghome,bg="#9CAACA",relief=FLAT,command=self.menu_GUI)
        self.home_button.grid(row=0,column=0)
        
        # 
        self.tabquanly = Button(thanhcongcu,bg="#9CAACA",relief=FLAT,text="Quản Lý",fg="white",command=self.quan_ly)
        self.tabquanly.grid(row=0,column=1)
        self.tabthongke = Button(thanhcongcu,bg="#9CAACA",relief=FLAT,text="Thống Kê",fg="white",command=self.thong_ke)
        self.tabthongke.grid(row=0,column=2)
        self.tabquydinh = Button(thanhcongcu,bg="#9CAACA",relief=FLAT,text="Quy Định",fg="white",command=self.quy_dinh)
        self.tabquydinh.grid(row=0,column=3)
        
        #++++++++++++ hinh anh +++++++++++++++++#
        self.bglophoc=ImageTk.PhotoImage(file=r"hinhanh\lop hoc.png")
        self.bgkhoilop=ImageTk.PhotoImage(file=r"hinhanh\khoi lop.png")
        self.bghocky=ImageTk.PhotoImage(file=r"hinhanh\hoc ky.png")
        self.bgnamhoc=ImageTk.PhotoImage(file=r"hinhanh\nam hoc.png")
        self.bgmonhoc=ImageTk.PhotoImage(file=r"hinhanh\mon hoc.png")
        self.bgdiem=ImageTk.PhotoImage(file=r"hinhanh\diem.png")
        self.bgketqua=ImageTk.PhotoImage(file=r"hinhanh\ket qua.png")
        self.bghocluc=ImageTk.PhotoImage(file=r"hinhanh\hoc luc.png")
        self.bghanhkiem=ImageTk.PhotoImage(file=r"hinhanh\hanh kiem.png")
        self.bgdantoc=ImageTk.PhotoImage(file=r"hinhanh\dan toc.png")
        self.bgtongiao=ImageTk.PhotoImage(file=r"hinhanh\ton giao.png")
        self.bgnghenghiep=ImageTk.PhotoImage(file=r"hinhanh\nghe nghiep.png")
        self.bggiaovien=ImageTk.PhotoImage(file=r"hinhanh\giao vien.png")
        self.bgphancong=ImageTk.PhotoImage(file=r"hinhanh\phan cong.png")
        self.bgbaocaomonhoc=ImageTk.PhotoImage(file=r"hinhanh\ket qua hoc sinh mon hoc.png")
        self.bgbaocaocanam=ImageTk.PhotoImage(file=r"hinhanh\ket qua hoc sinh ca nam.png")
        self.bgbaocaotongketmon=ImageTk.PhotoImage(file=r"hinhanh\ket qua lop hoc mon hoc.png")
        self.bgbaocaotongkethocky=ImageTk.PhotoImage(file=r"hinhanh\ket qua lop hoc hoc ky.png")
        self.bgdanhsachhocsinh=ImageTk.PhotoImage(file=r"hinhanh\danh sach hoc sinh.png")
        self.bghosolophoc=ImageTk.PhotoImage(file=r"hinhanh\ho so lop hoc.png")
        self.bgdotuoi=ImageTk.PhotoImage(file=r"hinhanh\qui dinh do tuoi.png")
        self.bgsiso=ImageTk.PhotoImage(file=r"hinhanh\qui dinh si so.png")
        self.bgdiemdat=ImageTk.PhotoImage(file=r"hinhanh\qui dinh diem dat.png")
        self.bghocsinh=ImageTk.PhotoImage(file=r"hinhanh\hoc sinh.png")
        self.bgdangnhap=ImageTk.PhotoImage(file=r"hinhanh\dang nhap.png")
        self.bgdangxuat=ImageTk.PhotoImage(file=r"hinhanh\dang xuat.png")
        self.bgdoimatkhau=ImageTk.PhotoImage(file=r"hinhanh\doi mat khau.png")
        self.bgquanly=ImageTk.PhotoImage(file=r"hinhanh\quan ly nguoi dung.png")
        self.bgsaoluu=ImageTk.PhotoImage(file=r"hinhanh\sao luu du lieu.png")
        self.bgphuchoi=ImageTk.PhotoImage(file=r"hinhanh\phuc hoi du lieu.png")
        self.bgthoat=ImageTk.PhotoImage(file=r"hinhanh\thoat phan mem.png")
        self.bgthongtin=ImageTk.PhotoImage(file=r"hinhanh\thong tin.png")
        self.bgthem=ImageTk.PhotoImage(file=r"hinhanh\them.png")
        self.bgluu=ImageTk.PhotoImage(file=r"hinhanh\luu.png")
        self.bgxoa=ImageTk.PhotoImage(file=r"hinhanh\xoa.png")
        self.bgreset=ImageTk.PhotoImage(file=r"hinhanh\cap nhat.png")
        self.bg_thoat=ImageTk.PhotoImage(file=r"hinhanh\thoat.png")
        
        

        #========================================================================================================#
        
        lop_khoilop = Label(self.quanly,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        lop_khoilop.grid(column=0,row=1)
        namhoc = Label(self.quanly,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        namhoc.grid(column=1,row=1)
        monhoc = Label(self.quanly,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        monhoc.grid(column=2,row=1)
        ketqua = Label(self.quanly,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        ketqua.grid(column=3,row=1)
        hocsinh = Label(self.quanly,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        hocsinh.grid(column=4,row=1)
        giaovien = Label(self.quanly,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        giaovien.grid(column=5,row=1)
        #
        hocsinhtrai =Label(hocsinh,width=18,height=6,bg="#CCFFFF") 
        hocsinhtrai.grid(row=0,column=0)
        hocsinhphai =Label(hocsinh,width=18,height=6,bg="#CCFFFF") 
        hocsinhphai.grid(row=0,column=1)
        
        
        
        #=========================================BUTTON - QUAN LY===========================================================#
        
        self.lophoc=Button(lop_khoilop,image=self.bglophoc,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Lớp học",font=("arial",8),compound=TOP,command=self.lophoc_GUI)
        self.lophoc.grid(row=0,column=0)
        textlop=Label(lop_khoilop,text="Lớp-Khối Lớp",font=("arial",8),fg="white",bg="#9999FF").grid(row=1,columnspan=3)
        
        self.khoilop=Button(lop_khoilop,image=self.bgkhoilop,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Khối lớp",font=("arial",8),compound=TOP,command=self.khoilop_GUI)
        self.khoilop.grid(row=0,column=1)
        #
        
        self.hocky=Button(namhoc,image=self.bghocky,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Học kỳ",font=("arial",8),compound=TOP,command=self.hocky_GUI)
        self.hocky.grid(row=0,column=0)
        texthocky=Label(namhoc,text="Năm Học",font=("arial",8),fg="white",bg="#9999FF").grid(column=0,row=1,columnspan=3)
        
        self.nam_hoc=Button(namhoc,image=self.bgnamhoc,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Năm học",compound=TOP,font=("arial",8),command=self.namhoc_GUI)
        self.nam_hoc.grid(row=0,column=1)
        #
        
        self.mon_hoc=Button(monhoc,image=self.bgmonhoc,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Môn học",font=("arial",8),compound=TOP,command=self.monhoc_GUI)
        self.mon_hoc.grid(row=0,column=0)
        self.textmonhoc=Label(monhoc,text="Môn Học",font=("arial",8),fg="white",bg="#9999FF").grid(column=0,row=1,columnspan=3)
        
        self.diem=Button(monhoc,image=self.bgdiem,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Điểm",font=("arial",8),compound=TOP,command=self.diem_GUI)
        self.diem.grid(row=0,column=1)
        #
        
        self.ket_qua=Button(ketqua,image=self.bgketqua,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Kết quả",font=("arial",8),compound=TOP,command=self.ketqua_GUI)
        self.ket_qua.grid(row=0,column=0)
        textketqua=Label(ketqua,text="Kết Quả",font=("arial",8),fg="white",bg="#9999FF").grid(column=0,row=1,columnspan=3)
        
        self.hocluc=Button(ketqua,image=self.bghocluc,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Học lực",font=("arial",8),compound=TOP,command=self.hocluc_GUI)
        self.hocluc.grid(row=0,column=1)
        
        self.hanhkiem=Button(ketqua,image=self.bghanhkiem,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Hạnh kiểm",font=("arial",8),compound=TOP,command=self.hanhkiem_GUI)
        self.hanhkiem.grid(row=0,column=2)
        #
        
        self.hoc_sinh=Button(hocsinhtrai,image=self.bghocsinh,bg="#CCFFFF",height=59,width=50,relief=FLAT,text="Học sinh",fg="black",compound=TOP,command=self.hocsinh_GUI)
        self.hoc_sinh.grid(row=0,column=0)
        texthocsinh=Label(hocsinh,text="Học sinh",font=("arial",8),fg="white",bg="#9999FF").grid(columnspan=3)
        
        self.dantoc=Button(hocsinhphai,image=self.bgdantoc,bg="#CCFFFF",height=10,width=90,relief=FLAT,text=" Dân Tộc",fg="black",compound=LEFT,anchor='w')
        self.dantoc.grid(row=0,column=0)
        
        self.tongiao=Button(hocsinhphai,image=self.bgtongiao,bg="#CCFFFF",height=10,width=90,relief=FLAT,text=" Tôn giáo",fg="black",compound=LEFT,anchor='w')
        self.tongiao.grid(row=1,column=0)
        
        self.nghenghiep=Button(hocsinhphai,image=self.bgnghenghiep,bg="#CCFFFF",height=10,width=90,relief=FLAT,text=" Nghề Nghiệp",fg="black",compound=LEFT,anchor='w')
        self.nghenghiep.grid(row=2,column=0)        
        #
        
        self.giao_vien=Button(giaovien,image=self.bggiaovien,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Giáo Viên",font=("arial",8),compound=TOP)
        self.giao_vien.grid(row=0,column=0)
        textmonhoc=Label(giaovien,text="Giáo viên",font=("arial",8),fg="white",bg="#9999FF").grid(column=0,row=1,columnspan=3)
        
        self.phancong=Button(giaovien,image=self.bgphancong,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Phân Công",font=("arial",8),compound=TOP)
        self.phancong.grid(row=0,column=1)
    
    
        
        #
        #============================================THONG - KE=================================================#
        
        
        #
        ketquahocsinh = Label(self.thongke,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        ketquahocsinh.grid(column=0,row=1)
        ketqualophoc = Label(self.thongke,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        ketqualophoc.grid(column=1,row=1)
        xuatdanhsach = Label(self.thongke,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        xuatdanhsach.grid(column=2,row=1)
        
        #
        
        self.baocaotheomonhoc=Button(ketquahocsinh,image=self.bgbaocaomonhoc,bg="#CCFFFF",height=63,width=60,relief=FLAT,text="Báo cáo theo \n môn học",font=("arial",8),compound=TOP)
        self.baocaotheomonhoc.grid(row=0,column=0)
        textbaocaotheolop=Label(ketquahocsinh,text="Kết quả học sinh",font=("arial",8),fg="white",bg="#9999FF").grid(row=1,columnspan=3)
        
        self.baocaocanam=Button(ketquahocsinh,image=self.bgbaocaocanam,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Báo cáo \n cả năm",font=("arial",8),compound=TOP)
        self.baocaocanam.grid(row=0,column=1)
        #
        
        self.baocaotongketmon=Button(ketqualophoc,image=self.bgbaocaotongketmon,bg="#CCFFFF",height=63,width=60,relief=FLAT,text="Báo cáo tổng \n kết môn",font=("arial",8),compound=TOP)
        self.baocaotongketmon.grid(row=0,column=0)
        textketqualophoc=Label(ketqualophoc,text="Kết quả lớp học",font=("arial",8),fg="white",bg="#9999FF").grid(row=1,columnspan=3)
        
        self.baocaotongkethocky=Button(ketqualophoc,image=self.bgbaocaotongkethocky,bg="#CCFFFF",height=63,width=60,relief=FLAT,text="Báo cáo tổng \n kết học kỳ",font=("arial",8),compound=TOP)
        self.baocaotongkethocky.grid(row=0,column=1)       
        #
        
        self.danhsachhocsinh=Button(xuatdanhsach,image=self.bgdanhsachhocsinh,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Danh sách \n học sinh",font=("arial",8),compound=TOP)
        self.danhsachhocsinh.grid(row=0,column=0)
        textxuathocsinh=Label(xuatdanhsach,text="Xuất danh sách",font=("arial",8),fg="white",bg="#9999FF").grid(row=1,columnspan=3)
        
        self.hosolophoc=Button(xuatdanhsach,image=self.bghosolophoc,bg="#CCFFFF",height=63,width=50,relief=FLAT,text="Hồ sơ \n lớp học",font=("arial",8),compound=TOP)
        self.hosolophoc.grid(row=0,column=1)
        
        #
        #===========================================================QUY - DINH================================================#
  
        quydinhchung = Label(self.quydinh,highlightbackground="black",highlightthickness=1,width=18,height=6,bg="#CCFFFF")
        quydinhchung.grid()
        
        #
        self.quydinhvedotuoi=Button(quydinhchung,image=self.bgbaocaomonhoc,bg="#CCFFFF",height=63,width=60,relief=FLAT,text="Quy định \n về độ tuổi",font=("arial",8),compound=TOP)
        self.quydinhvedotuoi.grid(row=0,column=0)
        textquidinh=Label(quydinhchung,text="Quy định chung",font=("arial",8),fg="white",bg="#9999FF").grid(row=1,columnspan=3)
        
        self.quidinhsiso=Button(quydinhchung,image=self.bgbaocaocanam,bg="#CCFFFF",height=63,width=60,relief=FLAT,text="Quy định \n về sĩ số",font=("arial",8),compound=TOP)
        self.quidinhsiso.grid(row=0,column=1)
        
        self.quidinhdiemdat=Button(quydinhchung,image=self.bgdiemdat,bg="#CCFFFF",height=63,width=60,relief=FLAT,text="Quy định \n về điểm đạt",font=("arial",8),compound=TOP)
        self.quidinhdiemdat.grid(row=0,column=2)
        self.quan_ly()      
  
    def menu_GUI(self):
        hienthi_menu = MenuGUI(self.root,self.home_button)
        hienthi_menu.mo_menu()   
    def quan_ly(self):
        self.tabquanly.config(bg="#B0E0E6")
        self.tabthongke.config(bg="#9CAACA")
        self.tabquydinh.config(bg="#9CAACA")
        self.quanly.tkraise()
        
    def thong_ke(self):
        self.tabthongke.config(bg="#B0E0E6")
        self.tabquanly.config(bg="#9CAACA")
        self.tabquydinh.config(bg="#9CAACA")
        self.thongke.tkraise()
        
    def quy_dinh(self):
        self.tabquydinh.config(bg="#B0E0E6")
        self.tabthongke.config(bg="#9CAACA")
        self.tabquanly.config(bg="#9CAACA")
        self.quydinh.tkraise()
    
    def lophoc_GUI(self):
        hienthi_lop_hoc = lophocGUI(self.root,self.lophoc,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgreset,self.bgluu,self.bgthongtin)
        hienthi_lop_hoc.lop_hoc()
    def khoilop_GUI(self):
        hienthi_khoilop = khoi_lopGUI(self.root,self.khoilop,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgluu)
        hienthi_khoilop.khoi_lop()
        
    def hocky_GUI(self):
        hienthi_hocky = hoc_kyGUI(self.root,self.hocky,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgluu)
        hienthi_hocky.hoc_ky()
    def namhoc_GUI(self):
        hienthi_namhoc = nam_hocGUI(self.root,self.nam_hoc,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgluu)
        hienthi_namhoc.nam_hoc()
    def monhoc_GUI(self):
        hienthi_monhoc = mon_hocGUI(self.root,self.mon_hoc,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgluu)
        hienthi_monhoc.mon_hoc()
    def diem_GUI(self):
        
        hienthi_diem = diemGUI(self.root,self.diem,notebook_tab,self.bg_thoat,self.bgluu,self.bgthongtin,self.bgthem)
        hienthi_diem.nhap_diem()
    
    def ketqua_GUI(self):
        hienthi_ketqua = ket_quaGUI(self.root,self.ket_qua,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgluu)
        hienthi_ketqua.ket_qua()
        
    def hocluc_GUI(self):
        hienthi_hocluc = hoc_lucGUI(self.root,self.hocluc,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgluu)
        hienthi_hocluc.hoc_luc()
    
    def hanhkiem_GUI(self):
        hienthi_hanhkiem = hanh_kiemGUI(self.root,self.hanhkiem,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgluu)
        hienthi_hanhkiem.hanh_kiem()

    def hocsinh_GUI(self):
        hienthi_hocsinh = hocsinhGUI(self.root,self.hoc_sinh,notebook_tab,self.bgthem,
                                    self.bgxoa,self.bg_thoat,self.bgreset,self.bgluu,self.bgthongtin)
        hienthi_hocsinh.hoc_sinh()