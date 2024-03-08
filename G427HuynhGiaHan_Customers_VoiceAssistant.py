import tkinter as tk_27hghan # import thư viện tkinter để tạo giao diện
from tkinter import messagebox # import messagebox để hiển thị hộp thoại thông báo
import speech_recognition as sr # import thư viện speech_recognition để nhận dạng giọng nói
from gtts import gTTS # import thư viện gTTS để tạo file âm thanh
import playsound  # import thư viện playsound để phát file âm thanh
import os  # import thư viện os để tạo thư mục
from tkinter import scrolledtext


class App(tk_27hghan.Tk):
    def __init__(self):
        super().__init__()
        self.title('27_Huỳnh Gia Hân_21133031_Ứng dụng nhận diện giọng nói')
        self.geometry('650x550')
        self.configure(bg='#6699FF')
        self.resizable(tk_27hghan.FALSE, tk_27hghan.FALSE)
    
        self.button_Thoat = tk_27hghan.Button(self, text="Thoát",font=("Times New Roman", 16),background="#CCCC66", command=self.Thoat_Form) # Tạo nút Thoát
        self.button_Thoat.place(x=575, y=450)  
        
        self.language_choice = tk_27hghan.StringVar(value='')
        self.duration_choice = tk_27hghan.IntVar(value=0)
        
        self.language_label = tk_27hghan.Label(self, text="Ngôn ngữ:",font=("Times New Roman", 16))
        self.language_label.place(x=130, y=30)

        self.language_input = tk_27hghan.Entry(self, textvariable=self.language_choice) # Tạo ô nhập liệu cho người dùng chọn ngôn ngữ
        self.language_input.place(x=300, y=35)

        self.duration_label = tk_27hghan.Label(self, text="Thời gian ghi âm:",font=("Times New Roman", 16))
        self.duration_label.place(x=130, y=70)

        self.duration_input = tk_27hghan.Entry(self, textvariable=self.duration_choice) # Tạo ô nhập liệu cho người dùng nhập thời gian ghi âm
        self.duration_input.place(x=300, y=75)
        
        self.result_label1=tk_27hghan.Label(self,text="Bạn đã nói: ",font=("Times New Roman", 16))
        self.result_label1.place(x=130, y=160)
        
        self.button_GhiAm = tk_27hghan.Button(self, text="Ghi âm",font=("Times New Roman", 16),background="#CCCC66", command=self.GhiAm) # Tạo nút Ghi âm
        self.button_GhiAm.place(x=450, y=50)
        
        self.filename_label = tk_27hghan.Label(self, text="Nhập tên file mp3 muốn lưu", font='calibri 14')
        self.filename_label.place(x=130, y=400)
        self.filename_entry = tk_27hghan.Entry(self, font='calibri 14')
        self.filename_entry.place(x=130,y=440)
        self.save_button = tk_27hghan.Button(self, text="Lưu file mp3", command=self.ChonThuMucLuu)
        self.save_button.place(x=350,y=440)
    def GhiAm(self):
        kq_voice=self.HGHan27_Lenh(language_choice=self.language_choice,duration_choice=self.duration_choice)

        # Tạo Frame để chứa TextBox
        self.frame = tk_27hghan.Frame(self)
        self.frame.pack()
        self.frame.place(x=130,y=200)

        # Tạo TextBox
        self.textbox = scrolledtext.ScrolledText(self.frame, width=30, height=10)
        self.textbox.pack()

        # Xóa nội dung của TextBox
        self.textbox.delete(1.0, tk_27hghan.END)

        # Thêm nội dung mới vào TextBox
        self.textbox.insert(tk_27hghan.INSERT, kq_voice)
        
    def HGHan27_Lenh(self,language_choice,duration_choice): # Hàm ghi âm và nhận dạng giọng nói
        r = sr.Recognizer() # khởi tạo đối tượng Recognizer để nhận dạng giọng nói
        with sr.Microphone() as Source: # mở microphone để ghi âm
            messagebox.showinfo("Nhắc nhở", "Hiệu chỉnh nhiễu trước khi nói!") # hiển thị thông báo
            r.adjust_for_ambient_noise(Source, duration=1) # hiệu chỉnh để loại bỏ nhiễu
        
            language = language_choice.get() # lấy ngôn ngữ lựa chọn
            if language not in ['vi', 'en-US']: # kiểm tra xem ngôn ngữ lựa chọn có hỗ trợ hay không
                messagebox.showwarning("Cảnh báo", "Ngôn ngữ bạn chọn không được hỗ trợ, chương trình chỉ chạy 2 ngôn ngữ Tiếng Việt (vi) và English (en_US)")
                return # thoát hàm
            else:
                messagebox.showinfo("Cảnh báo", "Bấm OK để bắt đầu ghi âm bằng ngôn ngữ đã chọn, trong thời gian bạn muốn")
            audio_data = r.record(Source, duration=duration_choice.get()) # ghi âm trong khoảng thời gian lựa chọn
            try:
                vlenh = r.recognize_google(audio_data, language=language) # nhận dạng giọng nói bằng Google
            except:
                vlenh = "Không nhận diện được âm thanh, hãy thử lại." # Thông báo không nhận diện được âm thanh
            #messagebox.showinfo("Quý vị đã nói là", vlenh) #hiển thị lời vừa nói
            return vlenh    
    
    def ChonThuMucLuu(self):
        text = self.textbox.get("1.0", "end-1c")
        if text != "":
            filename = self.filename_entry.get()
            if filename == "":
                filename = "speech_output"
            Ten = gTTS(text=text, lang=self.language_input.get())
            Ten.save(f"{filename}.mp3")
            os.startfile(f"{filename}.mp3")
        else:
            self.label2.config(text="Bạn chưa nhận dạng bất kỳ âm thanh nào")
    
    def Thoat_Form(self):
        hghan27_traloi = messagebox.askquestion("Xác nhận", "Bạn có thật sự muốn thoát chương trình (Y/N)?")
        if hghan27_traloi == "yes": self.destroy()


if __name__=="__main__":
    app=App()
    app.mainloop()