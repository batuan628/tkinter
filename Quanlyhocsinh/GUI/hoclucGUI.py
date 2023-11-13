from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class hoc_lucGUI:
    def __init__(self,root,hocluc,notebook_tab,them,xoa,thoat,luu):
        self.root=root
        self.hocluc=hocluc
        self.notebook_tab=notebook_tab
        self.them=them
        self.xoa=xoa
        self.thoat=thoat
        self.luu=luu
        
    def hoc_luc(self):
        global nhap_thongtin,note_frame
        self.trunglap()
        note_frame=Frame(self.notebook_tab)
        self.notebook_tab.add(note_frame,text="Học Lực")
        self.notebook_tab.select(note_frame)
        
        hienthi_hocluc=LabelFrame(note_frame,width=950,height=530,text="Danh sách học lực")
        hienthi_hocluc.grid(column=0,row=0,padx=1)
        nhapthongtin = Label(note_frame,bg="white",width=35,height=35)
        nhapthongtin.grid(column=1,row=0)
        #
        
        self.congcu=Frame(hienthi_hocluc,bg="white",width=123)
        self.congcu.place(x=0,y=0,width=123,height=30)
        hienthi=ttk.Treeview(hienthi_hocluc,columns=("Mahocluc","Tenhocluc","diemcantren","diemcanduoi","diemkhongche"))
        
        hienthi.heading("Mahocluc",text="Mã học lực")
        hienthi.heading("Tenhocluc",text="Tên học lực")
        hienthi.heading("diemcantren",text="Điểm cần trên")
        hienthi.heading("diemcanduoi",text="Điểm cần dưới")
        hienthi.heading("diemkhongche",text="Điểm khống chế")
        
        hienthi["show"]="headings"
        
        hienthi.column("Mahocluc",width=145)
        hienthi.column("Tenhocluc",width=145)
        hienthi.column("diemcantren",width=145)
        hienthi.column("diemcanduoi",width=145)
        hienthi.column("diemkhongche",width=145)

        hienthi.place(x=0,y=30)
        
        
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
        Label(thongtin,text="Mã học lực:",font=("arial",10),bg="White",anchor="w").grid(row=1,column=0,sticky="W",padx=20)
        mahocluc=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        mahocluc.grid(row=2,column=0,sticky="W",padx=20)
            
        Label(thongtin,text="Tên học lực:",font=("arial",10),bg="White",anchor="w").grid(row=3,column=0,sticky="W",padx=20)
        tenhocluc=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        tenhocluc.grid(row=4,column=0,sticky="W",padx=20)
        
        Label(thongtin,text="Điểm cần trên:",font=("arial",10),bg="White",anchor="w").grid(row=5,column=0,sticky="W",padx=20)
        diemcantren=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        diemcantren.grid(row=6,column=0,sticky="W",padx=20)
            
        Label(thongtin,text="Điểm cần dưới:",font=("arial",10),bg="White",anchor="w").grid(row=7,column=0,sticky="W",padx=20)
        diemcanduoi=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        diemcanduoi.grid(row=8,column=0,sticky="W",padx=20)
        
        Label(thongtin,text="Điểm khống chế:",font=("arial",10),bg="White",anchor="w").grid(row=9,column=0,sticky="W",padx=20)
        diemkhongche=Entry(thongtin,font=("arial",10),highlightbackground="black",highlightthickness=1,width=25)
        diemkhongche.grid(row=10,column=0,sticky="W",padx=20)
        
        luu_thongtin=Button(thongtin,text="Lưu vào danh sách",font=("arial",8),width=29,relief=FLAT)
        luu_thongtin.grid(row=11,pady=10,sticky="W",padx=20)
            
    def thoat_khoi(self):
        
        self.notebook_tab.forget(self.notebook_tab.index(self.notebook_tab.select()))
    
    def trunglap(self):
        kq=[]
        for i in self.notebook_tab.tabs():
            kq.append(self.notebook_tab.tab(i,"text"))
        for j in kq:
            if j =="Học Lực":
                self.notebook_tab.forget(note_frame)