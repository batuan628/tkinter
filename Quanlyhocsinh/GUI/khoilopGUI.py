from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class khoi_lopGUI:
    def __init__(self,root,khoilop,notebook_tab,them,xoa,thoat,reset,luu):
        self.root=root
        self.khoilop=khoilop
        self.notebook_tab=notebook_tab
        self.them=them
        self.xoa=xoa
        self.thoat=thoat
        self.reset=reset
        self.luu=luu
        
    def khoi_lop(self):
        global nhap_thongtin,thanhcongcu
        
        note_frame=Frame(self.notebook_tab)
        self.notebook_tab.add(note_frame,text="Khối lớp")
        hienthi_lop=LabelFrame(note_frame,width=950,height=530,text="Danh sách lớp")
        hienthi_lop.grid(column=0,row=0,padx=1)
        nhapthongtin = Label(note_frame,bg="white",width=35,height=35)
        nhapthongtin.grid(column=1,row=0)
        #
        
        self.congcu=Frame(hienthi_lop,bg="white",width=123)
        self.congcu.place(x=0,y=0,width=123,height=30)
        hienthi=ttk.Treeview(hienthi_lop,columns=("MaKhoiLop","Tenkhoilop"))
        
        hienthi.heading("MaKhoiLop",text="Mã lớp")
        hienthi.heading("Tenkhoilop",text="Tên lớp")
        
        hienthi["show"]="headings"
        
        hienthi.column("MaKhoiLop",width=145)
        hienthi.column("Tenkhoilop",width=145)

        hienthi.place(x=0,y=30,height=480,width=940)
        
        
        self.chucnang=Label(self.congcu,bg="white")
        self.chucnang.grid(row=0,column=0)
        them=Button(self.chucnang,image=self.them,relief=FLAT,bg="white")
        them.grid(column=0,row=0,padx=1)
        luu=Button(self.chucnang,image=self.luu,relief=FLAT,bg="white")
        luu.grid(column=1,row=0,padx=1)
        xoa=Button(self.chucnang,image=self.xoa,relief=FLAT,bg="white")
        xoa.grid(column=2,row=0,padx=1)
        reset=Button(self.chucnang,image=self.reset,relief=FLAT,bg="white")
        reset.grid(column=3,row=0,padx=1)
        thoat=Button(self.chucnang,image=self.thoat,relief=FLAT,command=self.thoat_khoi)
        thoat.grid(column=4,row=0,padx=1)
#
        nhap_thongtin=Frame(nhapthongtin,highlightbackground="black",highlightthickness=1,bg="white")
        nhap_thongtin.place(x=0,y=0,width=240,height=460)
        thanhcongcu=Frame(nhapthongtin,highlightbackground="black",highlightthickness=1,bg="white")
        thanhcongcu.place(x=0,y=465,width=240,height=60)

        
    def thoat_khoi(self):
        
        self.notebook_tab.forget(self.notebook_tab.index(self.notebook_tab.select()))