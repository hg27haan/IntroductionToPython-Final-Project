import numpy as np
from scipy.stats import zscore
import tkinter as tk_27hghan
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from scipy import stats
from tkinter import filedialog

graphs_hghan27 = ['Đường thẳng', 'Đồ thị hàm số', 'Đồ thị đường', 'Đồ thị phân tán', 'Đồ thị hình khối']


class App(tk_27hghan.Tk):
    def __init__(self):
        super().__init__()
        self.title("(27_HuynhGiaHan_21133031) VẼ ĐỒ THỊ TRÊN MATPLOTLIB")
        self.geometry("400x200")
        self.resizable(tk_27hghan.FALSE,tk_27hghan.FALSE)
        
        #btnOpenFile
        self.btnOpenFile = tk_27hghan.Button(self,text="Open File",command=self.hghan27_OpenFile)
        self.btnOpenFile.place(x=10,y=10)
    
        self.btn1_hghan27 = tk_27hghan.Button(self,text="Vẽ hình",command=self.Ex1,width=25)
        self.btn1_hghan27.pack(side=tk_27hghan.RIGHT,padx=10,pady=5)
        
        self.selected_graph_hghan27 = tk_27hghan.StringVar(self)
        self.selected_graph_hghan27.set(graphs_hghan27[0])  
        self.selected_graph_hghan27.trace('w', lambda *args: self.graph_selected())
        graph_menu_hghan27 = tk_27hghan.OptionMenu(self, self.selected_graph_hghan27, *graphs_hghan27)
        graph_menu_hghan27.pack(side=tk_27hghan.LEFT, padx=10, pady=5)
    
    def graph_selected(self):
        graph_name_hghan27 = self.selected_graph_hghan27.get()
        if graph_name_hghan27 == 'Đường thẳng':
            self.btn1_hghan27.config(command=self.Ex1)
            return 1
        elif graph_name_hghan27 == 'Đồ thị hàm số':
            self.btn1_hghan27.config(command=self.Ex2)
            return 2
        elif graph_name_hghan27 == 'Đồ thị đường':
            self.btn1_hghan27.config(command=self.Ex3)
            return 3
        elif graph_name_hghan27 == 'Đồ thị phân tán':
            self.btn1_hghan27.config(command=self.Ex4)
            return 4
        elif graph_name_hghan27 == 'Đồ thị hình khối':
            self.btn1_hghan27.config(command=self.Ex5)
            return 5

    def hghan27_OpenFile(self):
        global hghan27_filepath #bien toan cuc
        #Hop thoai Mo thu muc
        hghan27_filepath = filedialog.askopenfilename(title="27_HuynhGiaHan_21133031_Mở file cần xử lý",initialdir = "/")
        if hghan27_filepath == '':
            return
        global df_hghan27
        df_hghan27 = pd.read_csv(hghan27_filepath)
        global z_hghan27
        z_hghan27=np.abs(stats.zscore(df_hghan27._get_numeric_data()))
    
    def Ex1(self):
        if self.graph_selected() != 1:
            return
        plt.clf()
        x_list_hghan27 = np.arange(0, 4, 0.1)
        y_list_hghan27  = np.zeros(40)
        for i in range (0, 40):
                        result = df_hghan27.copy()
                        result = result[(z_hghan27 < x_list_hghan27 [i]).all(axis=1)]
                        y_list_hghan27 [i] = result.shape[0]
        plt.ylim(0, 3.0)
        plt.plot(x_list_hghan27 , y_list_hghan27)
        plt.title("Ex1")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.subplots_adjust(wspace=0.5)
        plt.show()

    def Ex2(self):
            if self.graph_selected() != 2:
                return

            plt.clf()
            def f(x):
                return x**2 + x + 1
            x1_hghan27  = np.linspace(start=-3, stop=3, num=100)
            y1_hghan27 = f(x1_hghan27 )
            plt.plot(x1_hghan27 , y1_hghan27 )
            plt.title("Ex2")
            plt.xlabel("X")
            plt.ylabel("f(x)")
            
            plt.xlim(-3, 3)
            plt.ylim(0, 8)
            plt.subplots_adjust(wspace=0.5)
            plt.show()

    def Ex3(self):
        if self.graph_selected() != 3:
            return
        plt.clf()
        plt.plot([0, 1, 2, 3, 4], [1, 2, 3, 4, 10], 'go-', label='Python')
        plt.plot([0, 1, 2, 3, 4], [10, 4, 3, 2, 1], 'ro-', label='C#')
        plt.plot([2.5, 2.5, 2.5, 1.5, 0.5], [1, 3, 5, 7, 10], 'bo-', label='Java')
        plt.title("Ex3")
        plt.xlabel("X")
        plt.xticks(np.arange(5), ('0', '1', '2', '3', '4'))
        plt.ylabel("Y")
        plt.legend(loc='best')
        plt.subplots_adjust(wspace=0.5)
        plt.show()

    def Ex4(self):
        if self.graph_selected() != 4:
            return
        plt.clf()
        xlim_hghan27 = (140, 200)
        ylim_hghan27= (60, 100)
        height_hghan27= np.array([167, 170, 149, 165, 155, 180, 166, 146, 159, 
                        185, 145, 168, 172, 181, 169])
        weight_hghan27 = np.array([86, 74, 66, 78, 68, 79, 90, 73, 70, 88, 66, 84, 
                        67, 84, 77])
        colors_hghan27 = np.random.rand(15)
        area_hghan27 = (30 * np.random.rand(15)) ** 2
        plt.plot(1, 10)
        plt.scatter(height_hghan27, weight_hghan27, s=area_hghan27, c=colors_hghan27)
        plt.title("Ex4")
        plt.xlabel("Chiều cao - cm")
        plt.ylabel("Cân nặng - kg")
        plt.xlim(*xlim_hghan27)
        plt.ylim(*ylim_hghan27)
        plt.show()

    def Ex5(self):
        if self.graph_selected() != 5:
            return
        plt.clf()
        h_hghan27 = np.array([167, 170, 149, 165, 155, 180, 166, 146, 159, 185, 145, 168, 172, 181, 189])
        w_hghan27 = np.array([86, 74, 66, 78, 68, 79, 90, 73, 70, 88, 66, 84, 67, 84, 77])
        ax_hghan27 = plt.axes(projection='3d')
        ax_hghan27.scatter3D(h_hghan27, w_hghan27)
        ax_hghan27.set_xlabel("Chiều cao")
        ax_hghan27.set_ylabel("Cân nặng")
        ax_hghan27.set_zlabel("Tần số")
        ax_hghan27.set_title("Ex5")
        plt.subplots_adjust()
        plt.show()

if __name__=="__main__":
    app=App()
    app.mainloop()
