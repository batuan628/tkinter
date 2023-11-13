from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class mon_hocGUI:
    def __init__(self,root,monhoc,notebook_tab,them,xoa,thoat,luu):
        self.root=root
        self.monhoc=monhoc
        self.notebook_tab=notebook_tab
        self.them=them
        self.xoa=xoa
        self.thoat=thoat
        self.luu=luu
        
    def mon_hoc(self):
        global nhap_thongtin
        
        note_frame=Frame(self.notebook_tab)
        self.notebook_tab.add(note_frame,text="Môn học")
        self.notebook_tab.select(note_frame)
        
        hienthi_monhoc=LabelFrame(note_frame,width=950,height=530,text="Danh sách môn học")
        hienthi_monhoc.grid(column=0,row=0,padx=1)
        nhapthongtin = Label(note_frame,bg="white",width=35,height=35)
        nhapthongtin.grid(column=1,row=0)
        #
        
        self.congcu=Frame(hienthi_monhoc,bg="white",width=123)
        self.congcu.place(x=0,y=0,width=123,height=30)
        hienthi=ttk.Treeview(hienthi_monhoc,columns=("Mamonhoc","Tenmonhoc","sotiet","heso"))
        
        hienthi.heading("Mamonhoc",text="Mã môn học")
        hienthi.heading("Tenmonhoc",text="Tên môn học")
        hienthi.heading("sotiet",text="Số tiết")
        hienthi.heading("heso",text="Hệ số")
        
        hienthi["show"]="headings"
        
        hienthi.column("Mamonhoc",width=145)
        hienthi.column("Tenmonhoc",width=145)
        hienthi.column("sotiet",width=145)
        hienthi.column("heso",width=145)

        hienthi.place(x=0,y=30,width=600)
        
        
        self.chucnang=Label(self.congcu,bg="white")
        self.chucnang.grid(row=0,column=0)
        them=Button(self.chucnang,image=self.them,relief=FLAT,bg="white")
        them.grid(column=0,row=0,padx=1)
        luu=Button(self.chucnang,image=self.luu,relief=FLAT,bg="white")
        luu.grid(column=1,row=0,padx=1)
        xoa=Button(self.chucnang,image=self.xoa,relief=FLAT,bg="white")
        xoa.grid(column=2,row=0,padx=1)
        thoat=Button(self.chucnang,image=self.thoat,relief=FLAT,command=self.thoat_khoi)
        thoat.grid(column=3,row=0,padx=1)
#
        nhap_thongtin=Frame(nhapthongtin,highlightbackground="black",highlightthickness=1,bg="white")
        nhap_thongtin.place(x=0,y=0,width=240,height=520)

        thongtin=Frame(nhap_thongtin,bg="white")
        thongtin.place(x=0,y=0,width=240,height=460)
            
        Label(thongtin,text="Nhập liệu thông tin",font=("arial",13,"bold"),width=22,bg="White").grid(row=0,column=0)
        Label(thongtin,text="Mã môn học:",font=("arial",10),bg="White",anchor="w").grid(row=1,column=0,sticky="W",padx=20)
        mamonhoc=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        mamonhoc.grid(row=2,column=0,sticky="W",padx=20)
            
        Label(thongtin,text="Tên môn học:",font=("arial",10),bg="White",anchor="w").grid(row=3,column=0,sticky="W",padx=20)
        tenmonhoc=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        tenmonhoc.grid(row=4,column=0,sticky="W",padx=20)
        
        Label(thongtin,text="Số Tiết:",font=("arial",10),bg="White",anchor="w").grid(row=5,column=0,sticky="W",padx=20)
        sotiey=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        sotiey.grid(row=6,column=0,sticky="W",padx=20)
            
        Label(thongtin,text="Hệ số:",font=("arial",10),bg="White",anchor="w").grid(row=7,column=0,sticky="W",padx=20)
        heso=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        heso.grid(row=8,column=0,sticky="W",padx=20)
        
        luu_thongtin=Button(thongtin,text="Lưu vào danh sách",font=("arial",8),width=29,relief=FLAT)
        luu_thongtin.grid(row=9,pady=10,sticky="W",padx=20)
            
    def thoat_khoi(self):
        
        self.notebook_tab.forget(self.notebook_tab.index(self.notebook_tab.select()))