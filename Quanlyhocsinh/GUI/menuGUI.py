from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class MenuGUI:
        def __init__(self,root,home_button):
             self.root = root
             self.home_button=home_button
             
        def mo_menu(self):
            self.bgdangnhap=ImageTk.PhotoImage(file=r"hinhanh\dang nhap.png")
            self.bgdangxuat=ImageTk.PhotoImage(file=r"hinhanh\dang xuat.png")
            self.bgdoimatkhau=ImageTk.PhotoImage(file=r"hinhanh\doi mat khau.png")
            self.bgquanly=ImageTk.PhotoImage(file=r"hinhanh\quan ly nguoi dung.png")
            self.bgsaoluu=ImageTk.PhotoImage(file=r"hinhanh\sao luu du lieu.png")
            self.bgphuchoi=ImageTk.PhotoImage(file=r"hinhanh\phuc hoi du lieu.png")
            self.bgthoat=ImageTk.PhotoImage(file=r"hinhanh\thoat phan mem.png")
            self.menu_fm = Label(self.root,highlightbackground="#9CAACA",highlightthickness=3,bg="white")
            self.menu_fm.place(x=0,y=30,width=160,height=290)
            #
            
            self.dangnhap = Button(self.menu_fm,relief=FLAT,font=("arial",8),compound=LEFT,text="Đăng Nhập",image=self.bgdangnhap,width=130,anchor='w',bg="white")
            self.dangnhap.grid(row=0,column=0)
            
            self.dangxuat = Button(self.menu_fm,relief=FLAT,font=("arial",8),compound=LEFT,text="Đăng Xuất",image=self.bgdangxuat,width=130,anchor='w',bg="white")
            self.dangxuat.grid(row=1,column=0)
                
            self.doimatkhau = Button(self.menu_fm,relief=FLAT,font=("arial",8),compound=LEFT,text="Đổi mật khẩu",image=self.bgdoimatkhau,width=130,anchor='w',bg="white")
            self.doimatkhau.grid(row=2,column=0)
            
            self.quanlynguoidung = Button(self.menu_fm,relief=FLAT,font=("arial",8),compound=LEFT,text="Quản Lý người dùng",image=self.bgquanly,width=130,anchor='w',bg="white")
            self.quanlynguoidung.grid(row=3,column=0)
            
            self.saoluu = Button(self.menu_fm,relief=FLAT,font=("arial",8),compound=LEFT,text="Sao lưu dữ liệu",image=self.bgsaoluu,width=130,anchor='w',bg="white")
            self.saoluu.grid(row=4,column=0)
            
            self.phuchoi = Button(self.menu_fm,relief=FLAT,font=("arial",8),compound=LEFT,text="Phục hồi dữ liệu",image=self.bgphuchoi,width=130,anchor='w',bg="white")
            self.phuchoi.grid(row=5,column=0)
            
            self.thoat = Button(self.menu_fm,relief=FLAT,font=("arial",8),compound=LEFT,text="Thoát",image=self.bgthoat,width=130,anchor='w',bg="white")
            self.thoat.grid(row=6,column=0)
            def dong_menu():
                self.menu_fm.destroy()
                self.home_button.config(command=self.mo_menu)
            
            self.home_button.config(command=dong_menu)   
            self.menu_fm.bind("<Leave>",self.dongmenu)
            
        def dongmenu(self,event):
            self.menu_fm.destroy()
            self.home_button.config(command=self.mo_menu) 
    