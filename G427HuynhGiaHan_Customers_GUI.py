#B1: Nap thu vien
import tkinter as tk_27hghan
from tkinter import *
from tkinter import filedialog #thu vien SUB-LIB tkinter = Hop thoai ho tro Mo file
from tkinter import messagebox as msg #thue vien SUB-LIB tkinter = hop thong bao = messagebox

class App(tk_27hghan.Tk):
    def __init__(self):
        super().__init__()

        #B2: Thiet lap va khoi tao doi tuong form
        self.title("G4_27 Huynh Gia Han_ 21133031_BÀI TẬP XỬ LÝ DỮ LIỆU THĂM DÒ")
        self.geometry("900x500")
        self.resizable(tk_27hghan.FALSE, tk_27hghan.FALSE)
        self.configure(bg="#99FFCC")
        
        #Thiet lap button
        self.btnOpenTextFile = tk_27hghan.Button(
            self, text="Open File", command=self.OpenTextFile, background='#33CCFF')
        self.btnOpenTextFile.place(x=5, y=5)

        ##Thiết lập 1 frame chứa thông tin của text
        self.frame = tk_27hghan.Frame(self, width=380, height=300,relief=tk_27hghan.SUNKEN, borderwidth=3)
        self.frame.place(x=5, y=40)
        
        #Thiết kế label để đọc file text có chứa scroll
        self.lblFileText = tk_27hghan.Text(self.frame, width=50, state=tk_27hghan.DISABLED, bg='#33CCFF', fg='#8B0000')
        self.scroll_y = tk_27hghan.Scrollbar(self.frame, command=self.lblFileText.yview, orient=tk_27hghan.VERTICAL)
        self.lblFileText.configure(yscrollcommand=self.scroll_y.set)
        
        #Thiết lập vị trí cho scroll
        self.scroll_y.pack(side=tk_27hghan.RIGHT, fill=tk_27hghan.Y)
        
        # Thiết lập vị trì cho fileText. i thiết lập cho scroll ms thiết lập sau cho label
        self.lblFileText.pack(side=tk_27hghan.LEFT, fill=tk_27hghan.BOTH)
        
        #Thiết lập 1 button xử lý
        self.btnXuLy = tk_27hghan.Button(self, text="Xử lý", command=self.XuLy, background='#33CCFF')
        self.btnXuLy.place(x=450, y=5)
        
        #Thiết lập 1 frame2 chứa thông tin của text
        self.frame2 = tk_27hghan.Frame(self, width=380, height=300,relief=tk_27hghan.SUNKEN, borderwidth=3)
        self.frame2.place(x=450, y=40)
        
        # Thiết kế label để đọc file text có chứa scroll
        self.lblXuLy = tk_27hghan.Text(self.frame2, width=50, state=tk_27hghan.DISABLED, bg='#33CCFF', fg='#8B0000')
        self.scroll_y = tk_27hghan.Scrollbar(self.frame2, command=self.lblXuLy.yview, orient=tk_27hghan.VERTICAL)
        self.lblXuLy.configure(yscrollcommand=self.scroll_y.set)
        
        # Thiết lập vị trí cho scroll
        self.scroll_y.pack(side=tk_27hghan.RIGHT, fill=tk_27hghan.Y)
        
        # Thiết lập vị trì cho fileText. i thiết lập cho scroll ms thiết lập sau cho label
        self.lblXuLy.pack(side=tk_27hghan.LEFT, fill=tk_27hghan.BOTH)

        # Thiết lập label đếm số lượng sv
        self.lblCount = tk_27hghan.Label(self, text="Số lượng SV: 0",relief=tk_27hghan.SUNKEN, width=25, background='#33CCFF')
        self.lblCount.place(x=700, y=470)

        #Thiết lập button xóa text
        self.btnXoa = tk_27hghan.Button(self,text = "Xóa", command = self.Xoa,background='#33CCFF')
        self.btnXoa.place(x=600, y=466)
        
        #Thiết lập button Thoát
        self.btnThoat = tk_27hghan.Button(self,text = "Thoát", command = self.Thoat,background='#33CCFF')
        self.btnThoat.place(x=640, y=466)

    #B3: Lap ham ClearText = xoa van ban cu
    def ClearText(self):
        # Dùng delete cho Text
            print("ClearText function called")
            self.lblFileText.delete("1.0", tk_27hghan.END)
            self.scroll_y.set(0.0, 1.0)
        # B4: HAM DOC file txt

    #B4: Ham doc file txt
    def OpenTextFile(self):
        global filepath_27hghan  # bien toan cuc
        #Hop thoai Mo thu muc
        filepath_27hghan = filedialog.askopenfilename(title="G4_02NTLanh_text", filetypes=(("Text File (.txt)", "*.txt"), ("CSV File (.csv)", "*.csv")))
        #Mo file co dau TV encoding="utf-8"
        f1_27hghan = open(filepath_27hghan, "r", encoding="utf-8")
        data_27hghan = f1_27hghan.read()
        #ClearText
        self.ClearText()
        #Nap noi dung file vao label text
        #set normal = cho phep sua text
        self.lblFileText.configure(state=tk_27hghan.NORMAL)
        self.lblFileText.insert(tk_27hghan.END, data_27hghan)
        # .. chon KO cho chinh sua nua = readonly
        self.lblFileText.configure(state=tk_27hghan.DISABLED)
        # dong doi tuong file
        f1_27hghan.close()
        

    def clear_data_27hghan(self):
            self.lblFileText.delete("1.0", "end")

    #B5: Ham thuc hien cac xu ly doc File - sua File lien quan
    def XuLy(self):
        #Mo file text co dau TV = encoding="utf-8"
        f1_27hghan = open(filepath_27hghan, "r", encoding="utf-8")
        s = ""
        list_27hghan = []
        #doc tung line_27hghan
        for line_27hghan in f1_27hghan:
            #Cắt toàn bộ kí tự khoảng trắng của mỗi dòng
            line_27hghan = line_27hghan.strip()
            #Kiểm tra dòng tiep theo có khác rỗng không = Nếu không thì đọc từng dòng đã bỏ khoảng trắng
            if line_27hghan != "":
                kytu = line_27hghan[0]  # Lấy ký tự đầu tiên
                if (kytu >= "0" and kytu <= "9"):
                    vitri = line_27hghan.find(":", 0, -1)
                    if (vitri == -1):
                        # kytu = line_27hghan[:vitri] #test thử
                        # lấy vị trí từ 0 đến ký tự \n
                        line_27hghan = line_27hghan[0:]
                        list_27hghan.append(line_27hghan)  # add phần tử vào mảng
                        s = s+line_27hghan+"\n"""
            # nếu ký tự đầu không phải chữ = bỏ qua
        # Sắp xếp phần từ trong mảng list_27hghan
        list_27hghan.sort()
            
        # Đọc phần tử trong mảng
        s = ""
        s = list_27hghan[0]
        key_27hghan = list_27hghan[0]
        dem_27hghan = 1
        for i in list_27hghan:
            # Kiểm tra nếu phần tử trùng thì bỏ qua không cộng vào s
            if i == key_27hghan:
                s = s+""
            else:
                key_27hghan = i
                s = s+i+"\n"
                dem_27hghan = dem_27hghan + 1
        # Thiết lập đóng file
        f1_27hghan.close()
        # ClearText
        self.ClearText()

        # Thiết lập nội dung vào label text
        # set normal để cho chỉnh sửa text
        self.lblXuLy.configure(state=tk_27hghan.NORMAL)
        self.lblXuLy.insert(tk_27hghan.END, s)
        # sau khi chỉnh sửa text thì không cho chỉnh sửa chỉ cho đọc readonly
        self.lblXuLy.configure(state=tk_27hghan.DISABLED)
        # Thiết lập biến đếm
        self.lblCount.configure(text="Số lượng SV: %d" % dem_27hghan)
        # Sau khi đọc file xong thì thực hiện lưu file
        f_new = open("KetQua.txt", "w+", encoding="utf-8")
        f_new.write(s+"\n"+"Số lượng SV: %d" % dem_27hghan)
    
    #Hàm xóa
    def Xoa(self):
        self.lblFileText.configure(state=tk_27hghan.NORMAL)
        self.lblFileText.delete("1.0", tk_27hghan.END)
        self.lblFileText.configure(state=tk_27hghan.DISABLED)
        self.lblXuLy.configure(state=tk_27hghan.NORMAL)
        self.lblXuLy.delete("1.0", tk_27hghan.END)
        self.lblXuLy.configure(state=tk_27hghan.DISABLED)
    #Hàm thoát
    def Thoat(self):
            self.destroy()

if __name__=="__main__":
    app=App()
    app.mainloop()
