import tkinter as tk_hghan27
from tkinter import messagebox
import G427HuynhGiaHan_Customers_CatFrameAnh
import G427HuynhGiaHan_Customers_EDA
import G427HuynhGiaHan_Customers_Game
import G427HuynhGiaHan_Customers_VoiceAssistant
import G427HuynhGiaHan_Customers_GUI
import G427HuynhGiaHan_Customers_NullAttributes
import G427HuynhGiaHan_Customers_Plot

class MainForm(tk_hghan27.Tk):
    def __init__(self):
        super().__init__()
    # self.geometry('400x300')
        self.title("27 HUYNH GIA HAN, G4_HCMUTE, ĐỒ ÁN HỌC PHẦN: LẬP TRÌNH PYTHON, T5.2023")
        self.configure(bg='#FFFFCC')
        hgh27_screen_width = self.winfo_screenwidth()
        hgh27_screen_height = self.winfo_screenheight()
        # Tính toán vị trí hiển thị form
        x = (hgh27_screen_width/2) - (400/2)
        y = (hgh27_screen_height/2) - (300/2)

        self.geometry('%dx%d+%d+%d' % (400, 300, x, y))

        panel = tk_hghan27.Label(self, text="27 HUYNH GIA HAN, G4_HCMUTE, ĐỒ ÁN HỌC PHẦN: LẬP TRÌNH PYTHON, T5.2023",font=("Times New Roman", 10),bg='#FFFF33',fg='#333333')
        panel.pack()
        
        def hgh27_move_text():
            x, y = panel.winfo_x(), panel.winfo_y()
            panel.place(x=x-10, y=y)
            if x <= -panel.winfo_width():
                panel.place(x=self.winfo_width(), y=y)
            self.after(50, hgh27_move_text)
            
        hgh27_move_text()

        btn_hgh27_voice = tk_hghan27.Button(self, text="Trợ lý Ảo", command=self.hgh27_Open_Voice_Assistance,bg="#CCCC99")
        btn_hgh27_voice.place(x = 150, y = 200)

        btn_hgh27_Frame = tk_hghan27.Button(self, text="Cắt Frames và xử lý ảnh ", command=self.hgh27_Frame,bg="#CCCC99")
        btn_hgh27_Frame.place(x = 50, y = 100)

        btn_hgh27_EDA = tk_hghan27.Button(self, text="EDA", command=self.hgh27_EDA,bg="#CCCC99")
        btn_hgh27_EDA.place(x = 50, y = 150)
        
        btn_hgh27_Gui = tk_hghan27.Button(self, text="GUI", command=self.hgh27_Gui,bg="#CCCC99")
        btn_hgh27_Gui.place(x = 50, y = 200)

        btn_hgh27_game = tk_hghan27.Button(self, text="Game", command=self.hgh27_Open_Game,bg="#CCCC99")
        btn_hgh27_game.place(x = 250, y = 100)
        
        btn_hgh27_Null = tk_hghan27.Button(self, text="Null Attributes", command=self.hgh27_NullAttributes,bg="#CCCC99")
        btn_hgh27_Null.place(x = 300, y = 100)
        
        btn_hgh27_Plot = tk_hghan27.Button(self, text="Plot", command=self.hgh27_Plot,bg="#CCCC99")
        btn_hgh27_Plot.place(x = 250, y = 150)

        btn_hgh27_Thoat = tk_hghan27.Button(self,text="Thoát",command=self.hgh27_Thoat)
        btn_hgh27_Thoat.place(x=300,y=250)


    
    def hgh27_Thoat(self):
        hghan27_traloi = messagebox.askquestion("Xác nhận", "Bạn có thật sự muốn thoát chương trình (Y/N)?")
        if hghan27_traloi == "yes": self.destroy()
        
    def hgh27_Open_Voice_Assistance(self):
        form = G427HuynhGiaHan_Customers_VoiceAssistant.App()
        form.mainloop()
        
    def hgh27_Frame(self):
        form = G427HuynhGiaHan_Customers_CatFrameAnh.App()
        form.mainloop()

    def hgh27_EDA(self):
        form = G427HuynhGiaHan_Customers_EDA.App()
        form.mainloop()
        
    def hgh27_Gui(self):
        form = G427HuynhGiaHan_Customers_GUI.App()
        form.mainloop()
        
    def hgh27_NullAttributes(self):
        form = G427HuynhGiaHan_Customers_NullAttributes.App()
        form.mainloop()
        
    def hgh27_Plot(self):
        form = G427HuynhGiaHan_Customers_Plot.App()
        form.mainloop()
        
    def hgh27_Open_Game(self):
        G427HuynhGiaHan_Customers_Game.Load_Form_Car()

hgh27_main_form_instance = MainForm()
hgh27_main_form_instance.mainloop()
