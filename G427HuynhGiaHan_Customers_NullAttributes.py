import tkinter as tk_27hghan

class App(tk_27hghan.Tk):
    def __init__(self):
        super().__init__()
        self.title("G4_27_Huỳnh Gia Hân_21133031_Bước 3: XỬ LÝ CỘT NULL = NẠP & CHỌN CÁC CỘT NULL CẦN XỬ LÝ")
        self.geometry("1000x650")
        self.resizable(tk_27hghan.FALSE,tk_27hghan.FALSE)
        self.configure(bg='#99FFCC')
        
        #Thiet lap label
        tk_27hghan.Label(self,text="Các thuộc tính").place(x=15,y=15)
        
        #thiet lap textbox (Khu apply = dung for nap cac thuoc tinh vao thay vi nhap tu textbox)
        self.txtSource = tk_27hghan.Entry(self,width=30)
        self.txtSource.place(x=120,y=15)
        
        self.var = tk_27hghan.IntVar()
        self.chkReversed = tk_27hghan.Checkbutton(self,text="Reversed",variable=self.var)
        self.chkReversed.place(x=500,y=20)
        
        #btnAdd
        self.btnAdd = tk_27hghan.Button(self,text="Add",width=10,command=self.InsertData_27hghan)
        self.btnAdd.place(x=310,y=10)
        
        #Listbox1
        self.listbox1 = tk_27hghan.Listbox(self,height=25,width=40, font ="Consolas 8",selectmode=tk_27hghan.EXTENDED)
        self.listbox1.bind("<Button-3>",self.ShowPopupMenu1_27hghan)
        self.listbox1.place(x=15,y=50)
        
        #Listbox2
        self.listbox2=tk_27hghan.Listbox(self,height=25,width=40,font ="Consolas 8",selectmode=tk_27hghan.EXTENDED)
        self.listbox2.bind("<Button-3>",self.ShowPopupMenu2_27hghan)
        self.listbox2.place(x=550,y=50)
        
        #lblsoluong
        tk_27hghan.Label(self,text="Số lượng").place(x=15,y=570)
        self.lblSoLuong=tk_27hghan.Label(self,relief =tk_27hghan.SUNKEN, font="Times 8",borderwidth=3 ,width=15,height=1)
        self.lblSoLuong.place(x=100,y=570)
        
        #btnMoveToRight
        self.btnMTR = tk_27hghan.Button(self, text = ">", width = 5, command = self.MoveToRight_27hghan)
        self.btnMTR.place(x = 425, y = 100)
        
        #btnMoveToLeft
        self.btnMTL = tk_27hghan.Button(self, text = "<", width = 5, command = self.MoveToLeft_27hghan)
        self.btnMTL.place(x = 425, y = 150)
        
        #Thiết lập btnMoveAllToRight
        self.btnMATR = tk_27hghan.Button(self, text = ">>", width = 5, command = self.MoveAllToRight_27hghan)
        self.btnMATR.place(x = 425, y = 200)

        #Thiết lập btnMoveAllToLeft
        self.btnMATL = tk_27hghan.Button(self, text = "<<", width = 5, command = self.MoveAllToLeft_27hghan)
        self.btnMATL.place(x = 425, y = 250)

        #btnClearListBox
        self.btnClearListBox = tk_27hghan.Button(self, text = "ClearListBoxs", width = 13, command = self.clearListbox_27hghan)
        self.btnClearListBox.place(x = 395, y = 350)

        #btnCurSelects
        self.btnClearCurSelect = tk_27hghan.Button(self, text = "ClearCurSelects", width = 15, command = self.DeleteSelected_27hghan)
        self.btnClearCurSelect.place(x = 390, y = 300)
        
        #Hàm xử lý btnAdd
    def InsertData_27hghan(self):
        hghan27_dem = 0
        hghan27_a = self.txtSource.get().strip()
        hghan27_kq = hghan27_a.ljust(20)
            #kq = chuỗi <- từ - chuỗi a = canh chỉnh left & bên right là fillchar(space) -> chiều dài width
        if(hghan27_a != ""):
            self.listbox1.insert(tk_27hghan.END,hghan27_kq)
        #Đếm số dòng trong listbox
        hghan27_dem = self.listbox1.size()
        #Điền thông tin vào label
        self.lblSoLuong.configure(text = hghan27_dem)
        self.txtSource.delete(0,tk_27hghan.END) #xóa trống text -> để nhập mới
    #hàm CopyToRight từ listbox1 sang listbox2 (cho phép chọn nhiều)
                                    #= có thể viết theo nhiều cách khác nhau
    
    def CopyToRight_27hghan(self):
        # i = 0
        # while i < hghan27_listbox1.size(): #Duyệt listbox1 -> đến từng vị trí chọn
        #     if(hghan27_listbox1.select_includes(i)==1):
        #         #sự kiện xác định 1pt tại vị trí i trong listbox 1 đang chọn hoặc not
        #         hghan27_listbox2.insert(hghan27_tk.END,hghan27_listbox1.get(i))
        #     i = i+1
        # #Clear selecitem listbox1
        # hghan27_listbox1.select_clear(0,hghan27_tk.END)
        
        selection = self.listbox1.curselection()
        if not selection:
            return
        if self.var.get():
            selected_items = reversed(selection)
        else:
            selected_items = selection
        copied_items = set()
        for i in selected_items:
            item = self.listbox1.get(i)
            if item not in copied_items:
                self.listbox2.insert(tk_27hghan.END, item)
                copied_items.add(item)

    #Hàm MoveToRight: di chuyển các thuộc tính từ listbox1 sang listbox2 (xóa các thuộc tính đã chuyển listbox1 ->)
    def MoveToRight_27hghan(self):
        # i = 0
        # selection = hghan27_listbox1.curselection() #lấy danh sách các vị trí chọn
        # for i in reversed(selection): #duyệt ngược 
        #     hghan27_listbox2.insert(hghan27_tk.END,hghan27_listbox1.get(i))
        #     hghan27_listbox1.delete(i)
        
        # #Đếm lại số dòng trong listbox1
        # hghan27_dem = hghan27_listbox1.size()
        # #Cập nhật vào label
        # hghan27_lblSoLuong.configure(text = hghan27_dem)
        selection = self.listbox1.curselection()
        if not selection:
            return
        if self.var.get():
            selected_items = reversed(selection)
        else:
            selected_items = selection
        moved_items = set()
        for i in selected_items:
            item = self.listbox1.get(i)
            if item not in moved_items:
                self.listbox2.insert(tk_27hghan.END, item)
                moved_items.add(item)
        for i in reversed(selection):
            self.listbox1.delete(i)
        self.listbox1.select_clear(0, tk_27hghan.END)
        dem = self.listbox1.size()
        self.lblSoLuong.configure(text=dem)
    
    #Hàm Delete thuộc tính 
    def DeleteLeft_27hghan(self):
        i=0
        selection = self.listbox1.curselection()
        for i in reversed(selection): 
            self.listbox1.delete(i)
        #Đếm lại dòng trong listbox1
        hghan27_dem=self.listbox1.size()
        #Cập nhật vào label
        self.lblSoLuong.configure(text=hghan27_dem)
        #Clear selecitem listbox1
        self.listbox1.select_clear(0,tk_27hghan.END)
        
    #Lập Menu cho listbox1
    def ShowPopupMenu1_27hghan(self,e):
        if self.listbox1.size()>0:
            hghan27_PopMenu = tk_27hghan.Menu(self.listbox1,tearoff=tk_27hghan.FALSE)
            hghan27_PopMenu.add_command(label="Copy To Right", command=self.CopyToRight_27hghan)
            hghan27_PopMenu.add_command(label="Move To Right",command=self.MoveToRight_27hghan)
            hghan27_PopMenu.add_command(label="Delete", command =self.DeleteLeft_27hghan)
            hghan27_PopMenu.tk_popup(e.x_root, e.y_root) #phải thiết lập x_root, y_root để showpopup

    def CopyToLeft_27hghan(self):
        selection = self.listbox2.curselection()
        if not selection:
            return
        if self.var.get():
            selected_items = reversed(selection)
        else:
            selected_items = selection
        copied_items = set()
        for i in selected_items:
            item = self.listbox2.get(i)
            if item not in copied_items:
                self.listbox1.insert(tk_27hghan.END, item)
                copied_items.add(item)
                
    def MoveToLeft_27hghan(self):
        i = 0
        selection = self.listbox2.curselection() 
        if(self.var.get()):
            for i in reversed(selection):
                self.listbox1.insert(tk_27hghan.END, self.listbox2.get(i))    
        else:
            for i in (selection):
                self.listbox1.insert(tk_27hghan.END, self.listbox2.get(i))
                
        i=self.listbox2.size()-1
        while(i>=0):
            if(self.listbox2.select_includes(i) ):
                self.listbox2.delete(i)
            i-=1
        hghan27_dem = self.listbox1.size()
        self.lblSoLuong.configure(text = hghan27_dem)
    
    def DeleteRight_27hghan(self):
        selected_items = self.listbox2.curselection()
        for item in selected_items:
            self.listbox2.delete(item)
            
    def ShowPopupMenu2_27hghan(self,event):
        hghan27_PopMenu = tk_27hghan.Menu(self.listbox1,tearoff=tk_27hghan.FALSE)
        hghan27_PopMenu.add_command(label="Copy To Left", command=self.CopyToLeft_27hghan)
        hghan27_PopMenu.add_command(label="Move To Left",command=self.MoveToLeft_27hghan)
        hghan27_PopMenu.add_command(label="Delete", command =self.DeleteRight_27hghan)
        hghan27_PopMenu.tk_popup(event.x_root, event.y_root) #phải thiết lập x_root, y_root để showpopup
    
    def clearListbox_27hghan(self):
        self.listbox1.delete(0, tk_27hghan.END)
        self.listbox2.delete(0, tk_27hghan.END)

    def MoveAllToRight_27hghan(self):
        self.listbox1.select_set(0, tk_27hghan.END)
        self.MoveToRight_27hghan()
        
    def MoveAllToLeft_27hghan(self):
        self.listbox2.select_set(0, tk_27hghan.END)
        self.MoveToLeft_27hghan()
        
    def DeleteSelected_27hghan(self):
        selected_items1 = self.listbox1.curselection()
        selected_items2 = self.listbox2.curselection()
        # xóa các phần tử được chọn trong listbox1
        for item in reversed(selected_items1):
            self.listbox1.delete(item)
        # xóa các phần tử được chọn trong listbox2
        for item in reversed(selected_items2):
            self.listbox2.delete(item)
        #Đếm lại dòng trong listbox1
        hghan27_dem = self.listbox1.size()
        #Cập nhật vào label
        self.lblSoLuong.configure(text = hghan27_dem)

if __name__=="__main__":
    app=App()
    app.mainloop()
