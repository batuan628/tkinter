from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class nam_hocGUI:
    def __init__(self,root,namhoc,notebook_tab,them,xoa,thoat,luu):
        self.root=root
        self.namhoc=namhoc
        self.notebook_tab=notebook_tab
        self.them=them
        self.xoa=xoa
        self.thoat=thoat
        self.luu=luu
        
    def nam_hoc(self):
        global nhap_thongtin
        
        note_frame=Frame(self.notebook_tab)
        self.notebook_tab.add(note_frame,text="Năm học")
        hienthi_namhoc=LabelFrame(note_frame,width=950,height=530,text="Danh sách năm học")
        hienthi_namhoc.grid(column=0,row=0,padx=1)
        nhapthongtin = Label(note_frame,bg="white",width=35,height=35)
        nhapthongtin.grid(column=1,row=0)
        #
        
        self.congcu=Frame(hienthi_namhoc,bg="white",width=123)
        self.congcu.place(x=0,y=0,width=123,height=30)
        hienthi=ttk.Treeview(hienthi_namhoc,columns=("Manamhoc","Tennamhoc"))
        
        hienthi.heading("Manamhoc",text="Mã năm học")
        hienthi.heading("Tennamhoc",text="Tên năm học")
        
        hienthi["show"]="headings"
        
        hienthi.column("Manamhoc",width=145)
        hienthi.column("Tennamhoc",width=145)

        hienthi.place(x=0,y=30,width=400)
        
        
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
        Label(thongtin,text="Mã năm học:",font=("arial",10),bg="White",anchor="w").grid(row=1,column=0,sticky="W",padx=20)
        manamhoc=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        manamhoc.grid(row=2,column=0,sticky="W",padx=20)
            
        Label(thongtin,text="Tên năm học:",font=("arial",10),bg="White",anchor="w").grid(row=3,column=0,sticky="W",padx=20)
        tennamhoc=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        tennamhoc.grid(row=4,column=0,sticky="W",padx=20)
        
        luu_thongtin=Button(thongtin,text="Lưu vào danh sách",font=("arial",8),width=29,relief=FLAT)
        luu_thongtin.grid(row=5,pady=10,sticky="W",padx=20)
            
    def thoat_khoi(self):
        
        self.notebook_tab.forget(self.notebook_tab.index(self.notebook_tab.select()))