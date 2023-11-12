from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class diemGUI:
    def __init__(self,root,diem,notebook_tab,thoat,luu,bgthongtin,them):
        self.root=root
        self.diem=diem
        self.notebook_tab=notebook_tab
        self.thoat=thoat
        self.luu=luu
        self.bgthongtin=bgthongtin
        self.them=them
        
    def nhap_diem(self):
        global nhap_thongtin
        
        note_frame=Frame(self.notebook_tab)
        self.notebook_tab.add(note_frame,text="Điểm")
        hienthi_diem=LabelFrame(note_frame,width=950,height=530,text="Danh sách điểm")
        hienthi_diem.grid(column=0,row=0,padx=1)
        nhapthongtin = Label(note_frame,bg="white",width=35,height=35)
        nhapthongtin.grid(column=1,row=0)
        #
        
        self.congcu=Frame(hienthi_diem,bg="white",width=123)
        self.congcu.place(x=0,y=0,height=30)
        hienthi=ttk.Treeview(hienthi_diem,columns=("Mahocsinh","hoten","diemmieng","diem15phut","diem45phut","diemthi"))
        
        hienthi.heading("Mahocsinh",text="Mã học sinh")
        hienthi.heading("hoten",text="Họ tên")
        hienthi.heading("diemmieng",text="Điểm miệng")
        hienthi.heading("diem15phut",text="Điểm 15 phút")
        hienthi.heading("diem45phut",text="Điểm 45 phút")
        hienthi.heading("diemthi",text="Điểm thi")
        
        hienthi["show"]="headings"
        
        hienthi.column("Mahocsinh",width=145)
        hienthi.column("hoten",width=145)
        hienthi.column("diemmieng",width=145)
        hienthi.column("diem15phut",width=145)
        hienthi.column("diem45phut",width=145)
        hienthi.column("diemthi",width=145)

        hienthi.place(x=0,y=30)
        
        
        self.chucnang=Label(self.congcu,bg="white")
        self.chucnang.grid(row=0,column=0)
        luu=Button(self.chucnang,image=self.luu,relief=FLAT,bg="white",text="Lưu điểm",compound=LEFT)
        luu.grid(column=1,row=0,padx=1)
        thoat=Button(self.chucnang,image=self.thoat,relief=FLAT,command=self.thoat_khoi,text="Thoát",compound=LEFT)
        thoat.grid(column=2,row=0,padx=1)
#
        nhap_thongtin=Frame(nhapthongtin,highlightbackground="black",highlightthickness=1,bg="white")
        nhap_thongtin.place(x=0,y=0,width=240,height=460)
        thanhcongcu=Frame(nhapthongtin,highlightbackground="black",highlightthickness=1,bg="white")
        thanhcongcu.place(x=0,y=465,width=240,height=60)
        
        
        
        nhap=Button(thanhcongcu,width=228,text="    Nhập liệu thông tin",image=self.bgthongtin,compound=LEFT,anchor='w',relief=RIDGE,height=20,command=self.thong_tin)
        nhap.grid(row=0,column=0,sticky="E",pady=(1,0))
        timkiem=Button(thanhcongcu,width=228,text="    Tìm kiếm thông tin",image=self.bgthongtin,compound=LEFT,anchor='w',relief=RIDGE,height=20,command=self.tim_kiem)
        timkiem.grid(row=1,column=0,sticky="E")
        self.thong_tin()
        
    def thong_tin(self):
            
            thongtin=Frame(nhap_thongtin,bg="white")
            thongtin.place(x=0,y=0,width=240,height=460)
            
            Label(thongtin,text="Nhập liệu thông tin",font=("arial",13,"bold"),width=22,bg="White").grid(row=0,column=0)
            Label(thongtin,text="Mã lớp:",font=("arial",10),bg="White",anchor="w").grid(row=1,column=0,sticky="W",padx=20)
            malop=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
            malop.grid(row=2,column=0,sticky="W",padx=20)
            
            Label(thongtin,text="Tên lớp:",font=("arial",10),bg="White",anchor="w").grid(row=3,column=0,sticky="W",padx=20)
            tenlop=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
            tenlop.grid(row=4,column=0,sticky="W",padx=20)
            
            Label(thongtin,text="Sĩ số:",font=("arial",10),bg="White",anchor="w").grid(row=5,column=0,sticky="W",padx=20)
            siso=Entry(thongtin,font=("arial",10),width=25,highlightbackground="black",highlightthickness=1)
            siso.grid(row=6,column=0,sticky="W",padx=20)
            
            Label(thongtin,text="Khối lớp:",font=("arial",10),bg="White",anchor="w").grid(row=7,column=0,sticky="W",padx=20)
            khoilop=ttk.Combobox(thongtin,font=("arial",10),width=22)
            khoilop.grid(row=8,column=0,sticky="W",padx=(20,1))
            
            themkhoilop = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themkhoilop.grid(row=8,column=0,sticky="E",padx=(0,20))
            
            Label(thongtin,text="Năm học:",font=("arial",10),bg="White",anchor="w").grid(row=9,column=0,sticky="W",padx=20)
            namhoc=ttk.Combobox(thongtin,font=("arial",10),width=22)
            namhoc.grid(row=10,column=0,sticky="W",padx=20)
            
            themnamhoc = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themnamhoc.grid(row=10,column=0,sticky="E",padx=(0,20))
            
            Label(thongtin,text="Chủ nhiệm:",font=("arial",10),bg="White",anchor="w").grid(row=11,column=0,sticky="W",padx=20)
            chunhiem=ttk.Combobox(thongtin,font=("arial",10),width=22)
            chunhiem.grid(row=12,column=0,sticky="W",padx=20)
            
            themgiaovien = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themgiaovien.grid(row=12,column=0,sticky="E",padx=(0,20))
            
            luu_thongtin=Button(thongtin,text="Lưu vào danh sách",font=("arial",8),width=32,relief=FLAT)
            luu_thongtin.grid(row=13,pady=10,sticky="W",padx=20)
            
        #
    def tim_kiem(self):
        timkiem_thongtin=Frame(nhap_thongtin,bg="white")
        timkiem_thongtin.place(x=0,y=0,width=240,height=460) 
        
        Label(timkiem_thongtin,text="Tìm kiếm thông tin",font=("arial",13,"bold"),width=22,bg="White").grid(row=0,column=0)
        Label(timkiem_thongtin,text="Nhập thông tin tìm kiếm:",font=("arial",10),bg="White",anchor="w").grid(row=1,column=0,sticky="W",padx=20)
        timkiem=Entry(timkiem_thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        timkiem.grid(row=2,column=0,sticky="W",padx=20)
        
        x=IntVar()
        tim_malop=Radiobutton(timkiem_thongtin,text="Tìm theo mã lớp",bg="white",variable=x,value=1)
        tim_malop.grid(row=3,column=0,sticky="W",padx=15,pady=(10,5))
        tim_ten=Radiobutton(timkiem_thongtin,text="Tìm theo tên lớp",bg="white",variable=x,value=2)
        tim_ten.grid(row=4,column=0,sticky="W",padx=15)
        timkiem_button=Button(timkiem_thongtin,text="Tìm kiếm",width=25)
        timkiem_button.grid(row=5,column=0,sticky=W,padx=15)
            
    def thoat_khoi(self):
        
        self.notebook_tab.forget(self.notebook_tab.index(self.notebook_tab.select()))