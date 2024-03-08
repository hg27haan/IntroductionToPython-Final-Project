import tkinter as tk_27hghan
from tkinter import filedialog
from tkinter import messagebox
from tkinter import * 
import cv2

class App(tk_27hghan.Tk):
    def __init__(self):
        super().__init__()
        self.title("(27_HuynhGiaHan_21133031) XỬ LÝ FRAMES ẢNH TỪ VIDEO")
        self.geometry("730x330")
        self.resizable(tk_27hghan.FALSE,tk_27hghan.FALSE)

        self.btnOpenFile = tk_27hghan.Button(self,text="Mở File", width=10, bg= "#6b6b83",foreground="white", command=self.hghan27_OpenFile)
        self.btnOpenFile.place(x=30, y = 50) 

        self.btnCatanh = tk_27hghan.Button(self,text="Cắt Ảnh", width = 10, bg= "#6b6b83",foreground="white", command=self.hghan27_CatAnh)
        self.btnCatanh.place(x=180, y = 50) 

        self.lblfile = tk_27hghan.Label(self, text="", relief= tk_27hghan.SUNKEN ,width = 70, border=3)
        self.lblfile.place(x = 30, y= 90)

        self.lblStart = tk_27hghan.Label(self, text="Bắt đầu(giây):", bg='#CCFFCC')
        self.lblStart.place(x=5, y=150)
        self.hghan27_start_time = tk_27hghan.Entry(self)
        self.hghan27_start_time.place(x=100, y=150)

        self.lblEnd = tk_27hghan.Label(self, text="Kết thúc(giây):", bg='#CCFFCC')
        self.lblEnd.place(x=5, y=180)
        self.hghan27_end_time = tk_27hghan.Entry(self)
        self.hghan27_end_time.place(x=100, y=180)

        self.btnCatanhYC5 = tk_27hghan.Button(self,text="Cắt Ảnh (Chọn thời điểm bắt đầu và kết thúc)", bg= "#659999",foreground="white", command=self.hghan27_YC5)
        self.btnCatanhYC5 .place(x=250, y = 155) 

        self.btnXuLyAnh = tk_27hghan.Button(self,text="Xử lý ảnh", width = 20, bg= "#99f2c8",foreground="black", command=self.hghan27_XuLyAnh)
        self.btnXuLyAnh .place(x=100, y = 250) 
        
    def hghan27_OpenFile(self):
        global hghan27_filepath #bien toan cuc
        #Hop thoai Mo thu muc
        hghan27_filepath = filedialog.askopenfilename(title="27_HuynhGiaHan_21133031_Mở file video",initialdir = "/",filetypes=(("MP4 file (.mp4)","*.mp4"),("MOV file (.mov)","*.mov")))
        if hghan27_filepath == '':
            return
        self.lblfile.configure(text= 'File Opened: %s' %hghan27_filepath,background="#12c2e9",fg="#2C5364")
        
    def hghan27_SaveFile(self):
        global hghan27_filesave 
        hghan27_filesave = filedialog.asksaveasfilename(title="27_HuynhGiaHan_21133031_Chọn folder và đặt tên frames đã cắt",initialdir = "/",filetypes = (("JPEG files","*.jpg"),("all files","*.*")),defaultextension='.jpg')
        if hghan27_filesave == '':
            return    
        
    def hghan27_CatAnh(self):
        self.hghan27_SaveFile()
        cap = cv2.VideoCapture(hghan27_filepath)
        hghan27_count =  0
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        hghan27_cut_time = None
        if messagebox.askyesno("Cắt ảnh tại thời điểm theo ý muốn", "Bạn có muốn chọn thời điểm cắt frame không?"):
            dl = Toplevel()
            dl.geometry("300x100")
            dl.title("Chọn thời điểm cắt ảnh")

            frame = Frame(dl)
            frame.pack(side=TOP)

            label = Label(frame, text="Nhập thời điểm (giây): ")
            label.pack(side=LEFT)

            entry = Entry(frame)
            entry.pack(side=LEFT)

            def hghan27_submit():
                nonlocal hghan27_cut_time
                hghan27_cut_time = float(entry.get())
                dl.destroy()

            hghan27_button = Button(dl, text="OK", command=hghan27_submit)
            hghan27_button.place(x=125,y=50)

            dl.grab_set()
            dl.wait_window()
            
        while cap.isOpened():
            if hghan27_cut_time is not None:
                cap.set(cv2.CAP_PROP_POS_MSEC, hghan27_cut_time * 1000)
                hghan27_cut_time = None
                
            ret,frame = cap.read()
            if not ret:
                break
            if frame.shape[0] == 0 or frame.shape[1] == 0:
                continue
            cv2.imshow('Khung Hinh', frame)
            
            filename = f"{hghan27_filesave}{hghan27_count}.jpg"
            cv2.imwrite(filename, frame)
            hghan27_count += 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

        messagebox.showinfo("Thông báo", "Đã cắt Frames thành công")
        self.lblfile.configure(text=f'Tổng số frames: {hghan27_count}\nLưu tại: {hghan27_filesave}')
    
    def hghan27_YC5(self):
        self.hghan27_SaveFile()
        cap = cv2.VideoCapture(hghan27_filepath)
        count = 0
        fps = cap.get(cv2.CAP_PROP_FPS)
        hghan27_start = float(self.hghan27_start_time.get()) if self.hghan27_start_time.get() else 0
        hghan27_end = float(self.hghan27_end_time.get()) if self.hghan27_end_time.get() else cap.get(cv2.CAP_PROP_FRAME_COUNT)/fps
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame.shape[0] == 0 or frame.shape[1] == 0:
                continue
            current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
            if current_time < hghan27_start:
                continue
            if current_time > hghan27_end:
                break
            cv2.imshow('Khung Hinh', frame)
            filename = f"{hghan27_filesave}{count}.jpg"
            cv2.imwrite(filename, frame)
            
            count += 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        
        messagebox.showinfo("Thông báo", "Đã cắt Frames thành công")
        self.lblfile.configure(text=f'Tổng số frames: {count}\nLưu tại: {hghan27_filesave}')

    def hghan27_XuLyAnh(self):
        global hghan27_openfileAnh
        hghan27_openfileAnh = filedialog.askopenfilename(title="27_HuynhGiaHan_21133031_Mở file Ảnh",initialdir = "/",filetypes = (("JPEG files","*.jpg"),("all files","*.*")),defaultextension='.jpg')
        if hghan27_openfileAnh == '':
            return
        #CHUYỂN ẢNH => ẢNH XÁM img
        hghan27_img = cv2.imread(hghan27_openfileAnh,cv2.IMREAD_GRAYSCALE)
        cv2.imshow('image xam',hghan27_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #LẤY SIZE ẢNH XÁM (2 D)
        (h,w) = hghan27_img.shape
        print("width={}, height={}".format(w,h))
        
        #ĐỌC ẢNH MÀU
        hghan27_img2 = cv2.imread(hghan27_openfileAnh) #đọc ảnh gốc
        cv2.imshow('Anh Mau',hghan27_img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Lấy SIZE Ảnh màu (3D) img2
        (h,w,d) = hghan27_img2.shape
        print('width={},height={},depth={}'.format(w,h,d))

        #LẤY ẢNH GIÁ TRỊ MÀU CỦA ĐIỂM ẢNH (Pixel) VỚI HỆ MÀU RGB
        (B,G,R) = hghan27_img2[200,200] #góc tọa độ gốc của ảnh: dưới_trái (0,0)
        print('Red={},Green={},Blue={}'.format(R,G,B))

        #CẮT ẢNH
        p = hghan27_img2[50:600, 60:600]
        cv2.imshow('Phan anh tu 50-350 x 60-360',p)
        cv2.waitKey(0)

        #ROTATE
        (h,w,d)=hghan27_img2.shape
        center = (w//2,h//2)
        M=cv2.getRotationMatrix2D(center,45,1.0)
        hghan27_rotated = cv2.warpAffine(hghan27_img2,M,(w,h))
        cv2.imshow('sau quay',hghan27_rotated)
        cv2.waitKey(0)

        #RESIZE 
        (h,w,d) = hghan27_img2.shape
        r = 200.0/w
        dim = (200,int(h*r))
        hghan27_rd=cv2.resize(hghan27_img2,dim)
        cv2.imshow('Sau resize',hghan27_rd)
        cv2.waitKey(0)
        
        hghan27_filesaveAnhXam = filedialog.asksaveasfilename(title="27_HuynhGiaHan_21133031_Chọn folder và lưu ảnh xám",initialdir = "/",filetypes = (("JPEG files","*.jpg"),("all files","*.*")),defaultextension='.jpg')
        if hghan27_filesaveAnhXam == '':
            return
        hghan27_filename = f"{hghan27_filesaveAnhXam} Anh xam.jpg"
        cv2.imwrite(hghan27_filename,hghan27_img)

if __name__=="__main__":
    hghan27_app=App()
    hghan27_app.mainloop()