#Bước 1: Nạp các thư viện cần thiết
from tkinter import messagebox
import numpy as np_hghan27
import pandas as pd_hghan27
import tkinter as tk_27hghan
from tkinter import ttk
from scipy import stats
from tkinter import filedialog
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns


class App(tk_27hghan.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('1500x650')
        self.title("27_Huỳnh Gia Hân_21133031_Phân tích dữ liệu thăm dò")
        self.configure(bg='#6699FF')
        self.resizable(tk_27hghan.FALSE, tk_27hghan.FALSE)

        self.btnOpenFile = tk_27hghan.Button(self,text="Mở File", width=10, bg= "#6b6b83",foreground="white", command=self.hghan27_OpenFile)
        self.btnOpenFile.grid(row = 0,column=1,padx=20,pady=20)
        
        self.btnTaiTapDuLieu = tk_27hghan.Button(self,text="Tải tập dữ liệu",width=10,bg= "#6b6b83",foreground="white", command=self.hghan27_TaiTapDuLieu)
        self.btnTaiTapDuLieu.grid(row = 0,column=2,padx=20,pady=20)
        
        self.panelTienXuLy = ttk.Frame(self,padding=20)
        self.panelTienXuLy.grid(row=1,column=2)
        
        self.label = ttk.Label(self.panelTienXuLy, text="TIỀN XỬ LÝ")
        self.label.pack()
        self.radio_var = tk_27hghan.StringVar()
        self.radio1 = ttk.Radiobutton(self.panelTienXuLy, text="Xử lý cột", variable=self.radio_var, value="option1",command=self.hghan27_TienXuLyCot)
        self.radio1.pack(anchor="w")
        
        self.radio2 = ttk.Radiobutton(self.panelTienXuLy, text="Xử lý dòng", variable=self.radio_var, value="option2",command=self.hghan27_TienXuLyDong)
        self.radio2.pack(anchor="w")
        
        self.radio3 = ttk.Radiobutton(self.panelTienXuLy, text="Xử lý cá biệt", variable=self.radio_var, value="option3",command=self.hghan27_TienXuLyCaBiet)
        self.radio3.pack(anchor="w")
        
        self.radio4 = ttk.Radiobutton(self.panelTienXuLy, text="Số hóa giá trị", variable=self.radio_var, value="option4",command=self.hghan27_TienXuLyThayTheViTri)
        self.radio4.pack(anchor="w")
        
        self.radio5 = ttk.Radiobutton(self.panelTienXuLy, text="Chuẩn hóa dữ liệu", variable=self.radio_var, value="option5",command=self.hghan27_TienXuLyChuanHoaDuLieu)
        self.radio5.pack(anchor="w")
        
        self.output_text = tk_27hghan.Text(self, bg='white', fg='#8B0000', height=35, width=120)
        self.output_text.place(x = 510, y =20)
        self.output_text.tag_configure("left", justify='left')
        
        self.BieuDoZ  = tk_27hghan.Label(self, text='VẼ BIỂU ĐỒ Z-SCORE',bg="#00CED1")
        self.BieuDoZ.place(x = 320, y = 50)
        self.LuuY  = tk_27hghan.Label(self, text='VUI LÒNG CHỌN XỬ LÝ CÁ BIỆT',bg="#00CED1")
        self.LuuY.place(x = 320, y = 75)
        self.ListZ = ['Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
        self.Z=ttk.Combobox(self, values=self.ListZ, state='readonly')
        self.Z.place(x=320,y=100)
        self.BieuDo = ['line','bar','heatmap']
        self.BD=ttk.Combobox(self, values=self.BieuDo, state='readonly')
        self.BD.place(x=320,y=130)
        self.btnBieuDoZ = tk_27hghan.Button(self,text="Vẽ biểu đồ Z-score",bg= "#6b6b83",foreground="white",command=self.hghan27_BieuDoZScore)
        self.btnBieuDoZ.place(x=320,y=155)
        
        self.method_label = tk_27hghan.Label(self, text='Chọn phương pháp:',bg="#00CED1")
        self.method_label.place( x = 120, y = 250)
        self.method_list = ['Chi2' , 'f_classif']
        self.method = ttk.Combobox(self, values=self.method_list, state='readonly')
        self.method.place(x =120 ,y = 280)
        self.method.current(0)
        
        self.k_label = tk_27hghan.Label(self, text = "Chọn k (1<=k<=5): ",bg="#00CED1")
        self.k_label.place (x = 120, y= 310)
        self.k = tk_27hghan.Entry(self, width=10)
        self.k.place(x = 120, y= 340)
    
        self.method_button = tk_27hghan.Button(self, text='Xuất dữ liệu',bg="#008B8B",fg="#fff",command=self.hghan27_PhanTichDuLieuThamDo)
        self.method_button.place(x= 270 , y = 290)
        
        self.BieuDoDoc_lable = tk_27hghan.Label(self,text="Biểu đồ cột dọc",bg="#00CED1")
        self.BieuDoDoc_lable.place(x=120,y=460)
        self.BieuDoDoc_list=['Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
        self.BieuDoDoc = ttk.Combobox(self, values=self.BieuDoDoc_list, state='readonly')
        self.BieuDoDoc.place(x=230,y=460)
        self.btnBieuDoDoc = tk_27hghan.Button(self,text="Vẽ biểu đồ cột dọc",command=self.hghan27_VeBieuDoDoc)
        self.btnBieuDoDoc.place(x=385,y=460)
        
        self.BieuDoNgang_lable = tk_27hghan.Label(self,text="Biểu đồ cột ngang",bg="#00CED1")
        self.BieuDoNgang_lable.place(x=120,y=490)
        self.BieuDoNgang_list=['Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
        self.BieuDoNgang = ttk.Combobox(self, values=self.BieuDoDoc_list, state='readonly')
        self.BieuDoNgang.place(x=230,y=490)
        self.btnBieuDoNgang = tk_27hghan.Button(self,text="Vẽ biểu đồ cột ngang",command=self.hghan27_VeBieuDoNgang)
        self.btnBieuDoNgang.place(x=385,y=490)
        
        self.DoThiHaiCot_lable = tk_27hghan.Label(self,text="Lựa chọn 2 cột",bg="#00CED1")
        self.DoThiHaiCot_lable.place(x=120,y=530)
        self.DoThiHaiCot_list=['Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
        self.DoThiHaiCotX = ttk.Combobox(self, values=self.DoThiHaiCot_list, state='readonly')
        self.DoThiHaiCotX.place(x=230,y=530)
        self.DoThiHaiCotY = ttk.Combobox(self, values=self.DoThiHaiCot_list, state='readonly')
        self.DoThiHaiCotY.place(x=230,y=560)
        self.btnDoThiHaiCot = tk_27hghan.Button(self,text="Vẽ biểu đồ Hai cột",command=self.hghan27_DoThiHaiCot)
        self.btnDoThiHaiCot.place(x=385,y=540)

        self.btnThoat=tk_27hghan.Button(self,text="Thoát",command=self.hghan27_Thoat)
        self.btnThoat.place(x=50,y=600)

    def hghan27_OpenFile(self):
        global hgh27_filepath
        
        hgh27_filepath = filedialog.askopenfilename(title="27_HuynhGiaHan_21133031_Mở file csv",initialdir = "/",filetypes=(("Text File (.txt)", "*.txt"), ("CSV File (.csv)", "*.csv")))
        if hgh27_filepath == '':
            return
        
    def hghan27_LayDuLieu(self):
        self.df_hghan27= pd_hghan27.read_csv(hgh27_filepath)
        self.data_hghan27= self.df_hghan27.copy()
    
    def hghan27_TaiTapDuLieu(self):
        #Bước 2: Tải tập dữ liệu
        self.hghan27_LayDuLieu()
        NTtk_27hghan = self.data_hghan27
        x =self.data_hghan27.shape
        self.output_text.insert(tk_27hghan.END, NTtk_27hghan)
        self.output_text.insert(tk_27hghan.END, '\n' + x)
        
    
    def hghan27_TienXuLyCot(self):
        #Bước 3: Xử lý CỘT dữ liệu null 
        self.hghan27_LayDuLieu()
        self.output_text.delete('1.0', tk_27hghan.END)
        NTtk_27hghan = self.data_hghan27.drop(columns =['CustomerID','Profession'],axis=1)
        
        self.output_text.insert(tk_27hghan.END, NTtk_27hghan)

    def hghan27_TienXuLyDong(self):
        #Bước 4: Xử lý DÒNG dử liệu Null
        self.hghan27_LayDuLieu()
        self.data_hghan27 = self.data_hghan27.drop(columns=['CustomerID', 'Profession'], axis=1)
        self.output_text.delete('1.0', tk_27hghan.END)
        # Kiểm tra xem có dòng nào bị thiếu giá trị hay không
        rows_with_missing_values = self.data_hghan27.isnull().any(axis=1)
    
        if rows_with_missing_values.any():
        # Nếu có dòng bị thiếu giá trị, thực hiện drop
            data = self.data_hghan27.dropna()
            self.output_text.insert(tk_27hghan.END, data)
        else:
        # Nếu không có dòng nào bị thiếu giá trị, thông báo tới người dùng
            data = self.data_hghan27.dropna()
            self.output_text.insert(tk_27hghan.END, "Không có dòng nào bị thiếu giá trị.\n\n")
            self.output_text.insert(tk_27hghan.END, data)

    def hghan27_TienXuLyCaBiet(self):
        #Bước 5: Xử lý loại bỏ các giá trị ngoại lệ (cá biệt)
        self.hghan27_LayDuLieu()
        self.data_hghan27 = self.data_hghan27.drop(columns=['CustomerID', 'Profession'], axis=1).dropna(how="any")
        self.output_text.delete('1.0', tk_27hghan.END)
        z = np_hghan27.abs(stats.zscore(self.data_hghan27._get_numeric_data()))
        NTtk_27hghan = self.data_hghan27[(z<1.7).all(axis=1)]
        self.output_text.insert(tk_27hghan.END, "MA TRAN Z-SCORE:\n")
        self.output_text.insert(tk_27hghan.END, str(z) + "\n\n")
        self.output_text.insert(tk_27hghan.END, str(NTtk_27hghan) + "\n")  

    def hghan27_TienXuLyThayTheViTri(self):
        #Bước 6: Thay thế các vị trí giá trị 0 và 1 bởi Male và Female 
        self.hghan27_TienXuLyCaBiet()
        z = np_hghan27.abs(stats.zscore(self.data_hghan27._get_numeric_data()))
        NTtk_27hghan = self.data_hghan27[(z<1.7).all(axis=1)]
        self.NTtk_27hghan['Gender'].replace({'Male': '0', 'Female': '1'},inplace = True)
        self.output_text.insert(tk_27hghan.END, self.NTtk_27hghan)

    def hghan27_TienXuLyChuanHoaDuLieu(self):
        self.hghan27_LayDuLieu()  # Thay vì self.df_hghan27= pd_hghan27.read_csv(hgh27_filepath), sử dụng self.LayDuLieu()
        self.output_text.delete('1.0', tk_27hghan.END)
        
        select_cols=['Gender','Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
        data_selected = self.df_hghan27.loc[:, select_cols]  # Thay vì df_hghan27.loc[:, select_cols], sử dụng self.df_hghan27
        data_selected['Gender'].replace({'Male': '0', 'Female': '1'},inplace = True)
        
        self.output_text.insert(tk_27hghan.END, "Các cột được chọn để chuẩn hóa dữ liệu: \n")
        self.output_text.insert(tk_27hghan.END, data_selected) 
        #Bước 7: Chuẩn hóa (rời rạc hóa) tập dữ liệu Input dùng MaxMin
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(data_selected)
        normalized_data = pd_hghan27.DataFrame(scaler.transform(data_selected), index=data_selected.index, columns=data_selected.columns)  # Thay df_hghan27 bằng normalized_data
        
        self.output_text.insert(tk_27hghan.END, "\n")
        self.output_text.insert(tk_27hghan.END, normalized_data.iloc[4:10])
        self.output_text.insert(tk_27hghan.END, "\n")
    
    def hghan27_PhanTichDuLieuThamDo(self):
        select_cols=['Gender','Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
        data_selected = self.df_hghan27.loc[:, select_cols]  # Thay vì df_hghan27.loc[:, select_cols], sử dụng self.df_hghan27
        data_selected['Gender'].replace({'Male': '0', 'Female': '1'},inplace = True)
        self.output_text.insert(tk_27hghan.END, "Các cột được chọn để chuẩn hóa dữ liệu: \n")
        self.output_text.insert(tk_27hghan.END, data_selected) 
        #Bước 7: Chuẩn hóa (rời rạc hóa) tập dữ liệu Input dùng MaxMin
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(data_selected)
        normalized_data = pd_hghan27.DataFrame(scaler.transform(data_selected), index=data_selected.index, columns=data_selected.columns)  # Thay df_hghan27 bằng normalized_data
        #bước 8: Xác định mô hình trích lọc các thuộc tính đặc trưng: EDA
        selected = self.method.get()
        num_k = int(self.k.get())
        self.output_text.delete('1.0', tk_27hghan.END)
        lbd = normalized_data[['Gender','Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']]
        lbd['Gender'].replace({'Male': '0', 'Female': '1'},inplace = True)
        a = lbd.loc[:, lbd.columns != 'Spending Score (1-100)']
        if selected == 'Chi2':
        
            b = lbd[['Spending Score (1-100)']]
            
            le = LabelEncoder()
            b = le.fit_transform(b)
            selector = SelectKBest(chi2, k = num_k)
        elif selected == 'f_classif':
            b = lbd['Spending Score (1-100)'].ravel()
            selector = SelectKBest(f_classif, k = num_k)
        selector.fit(a,b)
        a_new = selector.transform(a)
        selected_columns = a.columns[selector.get_support(indices=True)]
        self.output_text.insert('end', 'Các đặc trưng quan trọng: \n' )
        for col in selected_columns:
            self.output_text.insert('end', '-{}\n'.format(col))
        self.output_text.insert(tk_27hghan.END, str(a_new))
        self.output_text.insert(tk_27hghan.END, "\n")
        #Bước 9: Xác định mô hình trích lọc các thuộc tính đặc trưng
        self.XacDinhMoHinhTrichLoc_lable = tk_27hghan.Label(self,text="Xác định mô hình trích lọc các thuộc tính đặc trưng")
        self.XacDinhMoHinhTrichLoc_lable.place(x=120, y = 390)
        self.TrichLocDacTrung = selected_columns.tolist()
        self.TrichLoc = ttk.Combobox(self, values=self.TrichLocDacTrung, state='readonly')
        self.TrichLoc.place(x =120 ,y = 420)
        self.TrichLoc.current(0)
        #Bước 10: EDA theo nhu cầu thực tế
        a = selected_columns.tolist()
        self.EDATheoNhuCauX = normalized_data[a]
        self.EDATheoNhuCauY = normalized_data[['Spending Score (1-100)']]
        self.output_text.insert(tk_27hghan.END, "\n\n Bước 10: EDA theo nhu cầu thực tế\n")
        self.output_text.insert(tk_27hghan.END, self.EDATheoNhuCauX)
        self.output_text.insert(tk_27hghan.END, "\n")
        self.output_text.insert(tk_27hghan.END, self.EDATheoNhuCauY)

    def hghan27_BieuDoZScore(self):
        self.zscore = np_hghan27.abs(stats.zscore(self.data_hghan27._get_numeric_data()))
        selected_bar_output = self.Z.get()
        BieuDo = self.BD.get()
        if BieuDo in ['heatmap']:
            if selected_bar_output in ['Age']:
                sns.heatmap(self.zscore['Age'].value_counts().to_frame(), cmap='YlGnBu', annot=True, fmt='g')
                plt.title('Độ tuổi của khách hàng')
                plt.xlabel('Độ tuổi')
                plt.ylabel('Số lượng')
                plt.show()
            elif selected_bar_output in ['Annual Income ($)']:
                sns.heatmap(self.zscore['Annual Income ($)'].value_counts().to_frame(), cmap='YlGnBu', annot=True, fmt='g')
                plt.title('Thu nhập hàng năm của khách hàng')
                plt.xlabel('Thu nhập hàng năm ($)')
                plt.ylabel('Số lượng')
                plt.show()
            elif selected_bar_output in ['Spending Score (1-100)']:
                sns.heatmap(self.zscore['Spending Score (1-100)'].value_counts().to_frame(), cmap='YlGnBu', annot=True, fmt='g')
                plt.title('Tích điểm của khách hàng (thang điểm từ 0 - 100)')
                plt.xlabel('Số điểm')
                plt.ylabel('Số lượng')
                plt.show()
            elif selected_bar_output in ['Work Experience']:
                sns.heatmap(self.zscore['Work Experience'].value_counts().to_frame(), cmap='YlGnBu', annot=True, fmt='g')
                plt.title('Kinh nghiệm làm việc của khách hàng')
                plt.xlabel('Kinh nghiệm')
                plt.ylabel('Số lượng')
                plt.show()
            else:
                sns.heatmap(self.zscore['Family Size'].value_counts().to_frame(), cmap='YlGnBu', annot=True, fmt='g')
                plt.title('Thành viên trong gia đình của khách hàng')
                plt.xlabel('Số lượng thành viên')
                plt.ylabel('Số lượng')
                plt.show()
        else:  
            if selected_bar_output in ['Age']:
                self.zscore['Age'].value_counts().plot(kind=BieuDo, figsize=(10,5), title='Độ tuổi của khách hàng', xlabel='Độ tuổi', ylabel='Số lượng' )
                plt.show()
            elif selected_bar_output in ['Annual Income ($)']:
                self.zscore['Annual Income ($)'].value_counts().plot(kind=BieuDo, figsize=(10,5), title='Thu nhập hàng năm của khách hàng', xlabel='Thu nhập hàng năm ($)', ylabel='Số lượng' )
                plt.show()
            elif selected_bar_output in ['Spending Score (1-100)']:
                self.zscore['Spending Score (1-100)'].value_counts().plot(kind=BieuDo, figsize=(10,5), ttitle='Tích điểm của khách hàng (thang điểm từ 0 - 100)', xlabel='Số điểm', ylabel='Số lượng' )
                plt.show()
            elif selected_bar_output in ['Work Experience']:
                self.zscore['Work Experience'].value_counts().plot(kind=BieuDo, figsize=(10,5), title='Kinh nghiệm làm việc của khách hàng',xlabel='kinh nghiệm', ylabel='Số lượng' )
                plt.show()
            else:
                self.zscore['Family Size'].value_counts().plot(kind=BieuDo, figsize=(10,5), title='Thành viên trong gia đình của khách hàng',xlabel='Số lượng thành viên', ylabel='Số lượng' )
                plt.show()
    
    def hghan27_VeBieuDoDoc(self):
        selected_bar_output = self.BieuDoDoc.get()
        if selected_bar_output in ['Age']:
            bins_Age = [0,10,20,30,40,50,60,70,80,90,100]
            df_Age = pd_hghan27.cut(self.data_hghan27['Age'],bins_Age).value_counts().sort_index(ascending=True)
            df_Age.plot(kind='bar', figsize=(10, 5), title='Độ tuổi của khách hàng', xlabel='Độ tuổi', ylabel='Số lượng')
            plt.show()
        elif selected_bar_output in ['Annual Income ($)']:
            bins_ThuNhap = [0,20000,40000,60000,80000,100000,150000,200000,300000]
            df_ThuNhap = pd_hghan27.cut(self.data_hghan27['Annual Income ($)'],bins_ThuNhap).value_counts().sort_index(ascending=True)
            df_ThuNhap.plot(kind='bar', figsize=(10, 5), title='Thu nhập hàng năm của khách hàng', xlabel='Thu nhập hàng năm ($)', ylabel='Số lượng')
            plt.show()
        elif selected_bar_output in ['Spending Score (1-100)']:
            bins_diem = [0,10,20,30,40,50,60,70,80,90,100]
            df_diem = pd_hghan27.cut(self.data_hghan27['Spending Score (1-100)'],bins_diem).value_counts().sort_index(ascending=True)
            df_diem.plot(kind='bar', figsize=(10, 5), title='Tích điểm của khách hàng (thang điểm từ 0 - 100)', xlabel='Số điểm', ylabel='Số lượng')
            plt.show()
        elif selected_bar_output in ['Work Experience']:
            self.data_hghan27['Work Experience'].value_counts().plot(kind='bar', figsize=(10,5), title='Kinh nghiệm làm việc của khách hàng',xlabel='kinh nghiệm', ylabel='Số lượng' )
            plt.show()
        else:
            self.data_hghan27['Family Size'].value_counts().plot(kind='bar', figsize=(10,5), title='Thành viên trong gia đình của khách hàng',xlabel='Số lượng thành viên', ylabel='Số lượng' )
            plt.show()
        
    def hghan27_VeBieuDoNgang(self):
        selected_bar_output = self.BieuDoNgang.get()
        if selected_bar_output in ['Age']:
            bins_Age = [0,10,20,30,40,50,60,70,80,90,100]
            df_Age = pd_hghan27.cut(self.data_hghan27['Age'],bins_Age).value_counts().sort_index(ascending=True)
            df_Age.plot(kind='barh', figsize=(10, 5), title='Độ tuổi của khách hàng', xlabel='Độ tuổi', ylabel='Số lượng')
            plt.show()
        elif selected_bar_output in ['Annual Income ($)']:
            bins_ThuNhap = [0,20000,40000,60000,80000,100000,150000,200000,300000]
            df_ThuNhap = pd_hghan27.cut(self.data_hghan27['Annual Income ($)'],bins_ThuNhap).value_counts().sort_index(ascending=True)
            df_ThuNhap.plot(kind='barh', figsize=(10, 5), title='Thu nhập hàng năm của khách hàng', xlabel='Thu nhập hàng năm ($)', ylabel='Số lượng')
            plt.show()
        elif selected_bar_output in ['Spending Score (1-100)']:
            bins_diem = [0,10,20,30,40,50,60,70,80,90,100]
            df_diem = pd_hghan27.cut(self.data_hghan27['Spending Score (1-100)'],bins_diem).value_counts().sort_index(ascending=True)
            df_diem.plot(kind='barh', figsize=(10, 5), title='Tích điểm của khách hàng (thang điểm từ 0 - 100)', xlabel='Số điểm', ylabel='Số lượng')
            plt.show()
        elif selected_bar_output in ['Work Experience']:
            self.data_hghan27['Work Experience'].value_counts().plot(kind='barh', figsize=(10,5), title='Kinh nghiệm làm việc của khách hàng',xlabel='kinh nghiệm', ylabel='Số lượng' )
            plt.show()
        else:
            self.data_hghan27['Family Size'].value_counts().plot(kind='barh', figsize=(10,5), title='Thành viên trong gia đình của khách hàng',xlabel='Số lượng thành viên', ylabel='Số lượng' )
            plt.show()   

    def hghan27_DoThiHaiCot(self):
        x_list = self.data_hghan27[self.DoThiHaiCotX.get()]
        y_list = self.data_hghan27[self.DoThiHaiCotY.get()]
        plt.plot(x_list,y_list)
        plt.xlabel(self.DoThiHaiCotX.get())
        plt.ylabel(self.DoThiHaiCotY.get())
        plt.title('Biểu đồ hai cột')
        plt.show()
        
    def hghan27_Thoat(self):
        self.destroy()
        
if __name__=="__main__":
    app=App()
    app.mainloop()