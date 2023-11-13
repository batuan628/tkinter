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
        global nhap_thongtin,title,note_frame
        title = "Điểm"
        self.trunglap()
        note_frame=Frame(self.notebook_tab)
        self.notebook_tab.add(note_frame,text="Điểm")
        self.notebook_tab.select(note_frame)
        
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
            
            Label(thongtin,text="Mã học sinh:",font=("arial",10),bg="White",anchor="w").grid(row=1,column=0,sticky="W",padx=20)
            mahocsinh=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
            mahocsinh.grid(row=2,column=0,sticky="W",padx=20)
            
            Label(thongtin,text="Môn học:",font=("arial",10),bg="White",anchor="w").grid(row=3,column=0,sticky="W",padx=20)
            mamonhoc=ttk.Combobox(thongtin,font=("arial",10),width=22)
            mamonhoc.grid(row=4,column=0,sticky="W",padx=20)
            
            themmonhoc = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themmonhoc.grid(row=4,column=0,sticky="E",padx=(0,20))
            
            Label(thongtin,text="Học kỳ:",font=("arial",10),bg="White",anchor="w").grid(row=5,column=0,sticky="W",padx=20)
            mahocky=ttk.Combobox(thongtin,font=("arial",10),width=22)
            mahocky.grid(row=6,column=0,sticky="W",padx=20)
            
            themhocky = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themhocky.grid(row=6,column=0,sticky="E",padx=(0,20))
            
            Label(thongtin,text="Năm học:",font=("arial",10),bg="White",anchor="w").grid(row=7,column=0,sticky="W",padx=20)
            manamhoc=ttk.Combobox(thongtin,font=("arial",10),width=22)
            manamhoc.grid(row=8,column=0,sticky="W",padx=(20,1))
            
            themnamhoc = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themnamhoc.grid(row=8,column=0,sticky="E",padx=(0,20))
            
            Label(thongtin,text="Lớp học:",font=("arial",10),bg="White",anchor="w").grid(row=9,column=0,sticky="W",padx=20)
            malop=ttk.Combobox(thongtin,font=("arial",10),width=22)
            malop.grid(row=10,column=0,sticky="W",padx=20)
            
            themlophoc = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themlophoc.grid(row=10,column=0,sticky="E",padx=(0,20))
            
            Label(thongtin,text="Loại điểm:",font=("arial",10),bg="White",anchor="w").grid(row=11,column=0,sticky="W",padx=20)
            maloai=ttk.Combobox(thongtin,font=("arial",10),width=22)
            maloai.grid(row=12,column=0,sticky="W",padx=20)
            
            themloaidiem = Button(thongtin,image=self.them,relief=FLAT,bg="white")
            themloaidiem.grid(row=12,column=0,sticky="E",padx=(0,20))
            
            Label(thongtin,text="Điểm:",font=("arial",10),bg="White",anchor="w").grid(row=13,column=0,sticky="W",padx=20)
            nhap_diem=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
            nhap_diem.grid(row=14,column=0,sticky="W",padx=20)
            
            luu_thongtin=Button(thongtin,text="Lưu vào danh sách",font=("arial",8),width=32,relief=FLAT)
            luu_thongtin.grid(row=15,pady=10,sticky="W",padx=20)
            
        #
    def tim_kiem(self):
        timkiem_thongtin=Frame(nhap_thongtin,bg="white")
        timkiem_thongtin.place(x=0,y=0,width=240,height=460) 
        
        Label(timkiem_thongtin,text="Tìm kiếm thông tin",font=("arial",13,"bold"),width=22,bg="White").grid(row=0,column=0)
        Label(timkiem_thongtin,text="Môn học:",font=("arial",10),bg="White",anchor="w").grid(row=1,column=0,sticky="W",padx=20)
        mamonhoc=ttk.Combobox(timkiem_thongtin,font=("arial",10),width=22)
        mamonhoc.grid(row=2,column=0,sticky="W",padx=20)
            
        themmonhoc = Button(timkiem_thongtin,image=self.them,relief=FLAT,bg="white")
        themmonhoc.grid(row=2,column=0,sticky="E",padx=(0,20))
            
        Label(timkiem_thongtin,text="Học kỳ:",font=("arial",10),bg="White",anchor="w").grid(row=3,column=0,sticky="W",padx=20)
        mahocky=ttk.Combobox(timkiem_thongtin,font=("arial",10),width=22)
        mahocky.grid(row=4,column=0,sticky="W",padx=20)
            
        themhocky = Button(timkiem_thongtin,image=self.them,relief=FLAT,bg="white")
        themhocky.grid(row=4,column=0,sticky="E",padx=(0,20))
            
        Label(timkiem_thongtin,text="Năm học:",font=("arial",10),bg="White",anchor="w").grid(row=5,column=0,sticky="W",padx=20)
        manamhoc=ttk.Combobox(timkiem_thongtin,font=("arial",10),width=22)
        manamhoc.grid(row=6,column=0,sticky="W",padx=(20,1))
            
        themnamhoc = Button(timkiem_thongtin,image=self.them,relief=FLAT,bg="white")
        themnamhoc.grid(row=6,column=0,sticky="E",padx=(0,20))
            
        Label(timkiem_thongtin,text="Lớp học:",font=("arial",10),bg="White",anchor="w").grid(row=7,column=0,sticky="W",padx=20)
        malop=ttk.Combobox(timkiem_thongtin,font=("arial",10),width=22)
        malop.grid(row=8,column=0,sticky="W",padx=20)
        
        themlophoc = Button(timkiem_thongtin,image=self.them,relief=FLAT,bg="white")
        themlophoc.grid(row=8,column=0,sticky="E",padx=(0,20))
        
        xem_thongtin=Button(timkiem_thongtin,text="Lưu vào danh sách",font=("arial",8),width=32,relief=FLAT)
        xem_thongtin.grid(row=9,pady=10,sticky="W",padx=20)
            
    def thoat_khoi(self):
        
        self.notebook_tab.forget(self.notebook_tab.index(self.notebook_tab.select()))
    
    def trunglap(self):
        kq=[]
        for i in self.notebook_tab.tabs():
            kq.append(self.notebook_tab.tab(i,"text"))
        for j in kq:
            if j ==title:
                self.notebook_tab.forget(note_frame)
                
                
                