import tkinter as tk
from customtkinter import CTkLabel, CTkButton, CTkFrame


WIDTH = 555
HEIGHT = 580


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.x = ((self.winfo_screenwidth() // 2) - (WIDTH // 2))
        self.y = ((self.winfo_screenheight() // 2) - (HEIGHT // 2))
        
        self.title('App')
        self.resizable(False, False)
        self.geometry(f'{WIDTH}x{HEIGHT}+{self.x}+{self.y}')
        self.config(bg='white')
        
        # -----------------------------------------------------
        # -----------------------------------------------------
        self.selection_btns = [False, False, False]
        # -----------------------------------------------------
        # -----------------------------------------------------
        
        self.frame_btns = CTkFrame(self, width=100, height=570, corner_radius=10)
        self.frame_btns.place(x=5, y=5)

        self.btn_1 = CTkButton(self.frame_btns, text='btn 1', width=70, height=30, fg_color='white', border_width=2,
                               border_color='black', text_color='black', hover=False, text_color_disabled='gray', command=self.click_btn_1)
        self.btn_1.place(x=15, y=10)
        self.btn_1.bind('<Enter>', self.enter_btn_1)
        self.btn_1.bind('<Leave>', self.leave_btn_1)

        self.btn_2 = CTkButton(self.frame_btns, text='btn 2', width=70, height=30, fg_color='white', border_width=2,
                               border_color='black', text_color='black', hover=False, text_color_disabled='gray', command=self.click_btn_2)
        self.btn_2.place(x=15, y=60)
        self.btn_2.bind('<Enter>', self.enter_btn_2)
        self.btn_2.bind('<Leave>', self.leave_btn_2)

        self.btn_3 = CTkButton(self.frame_btns, text='btn 3', width=70, height=30, fg_color='white', border_width=2,
                               border_color='black', text_color='black', hover=False, text_color_disabled='gray', command=self.click_btn_3)
        self.btn_3.place(x=15, y=110)
        self.btn_3.bind('<Enter>', self.enter_btn_3)
        self.btn_3.bind('<Leave>', self.leave_btn_3)

        # -----------------------------------------------------

        self.lbl_tex_ = CTkLabel(self, text='Hover Btns And Edit Selection', width=440, height=570,
                 fg_color='gray', text_color='white', corner_radius=10, font=('Arial', 25, 'bold'))
        self.lbl_tex_.place(x=110, y=5)

        # ------------------------------------------- Functions
    def enter_btn_1(self, event):
        self.btn_1.configure(width=90, height=40, fg_color='#ff1cff')
        self.btn_1.place(x=5, y=10)
    def leave_btn_1(self, event):
        if self.selection_btns[0]:
            self.btn_1.configure(width=90, height=40, fg_color='#ff1cff', state=tk.DISABLED)
            self.btn_2.configure(width=70, height=30, fg_color='white', state=tk.NORMAL)
            self.btn_3.configure(width=70, height=30, fg_color='white', state=tk.NORMAL)
            self.btn_1.place(x=5, y=10)
            self.btn_2.place(x=15, y=60)
            self.btn_3.place(x=15, y=110)
        else:
            self.btn_1.configure(width=70, height=30, fg_color='white')
            self.btn_1.place(x=15, y=10)

    def enter_btn_2(self, event):
        self.btn_2.configure(width=90, height=40, fg_color='#fc60fc')
        self.btn_2.place(x=5, y=60)
    def leave_btn_2(self, event):
        if self.selection_btns[1]:
            self.btn_1.configure(width=70, height=30, fg_color='white', state=tk.NORMAL)
            self.btn_2.configure(width=90, height=40, fg_color='#fc60fc', state=tk.DISABLED)
            self.btn_3.configure(width=70, height=30, fg_color='white', state=tk.NORMAL)
            self.btn_1.place(x=15, y=10)
            self.btn_2.place(x=5, y=60)
            self.btn_3.place(x=15, y=110)
        else:
            self.btn_2.configure(width=70, height=30, fg_color='white')
            self.btn_2.place(x=15, y=60)

    def enter_btn_3(self, event):
        self.btn_3.configure(width=90, height=40, fg_color='#fc60fc')
        self.btn_3.place(x=5, y=110)
    def leave_btn_3(self, event):
        if self.selection_btns[2]:
            self.btn_1.configure(width=70, height=30, fg_color='white', state=tk.NORMAL)
            self.btn_2.configure(width=70, height=30, fg_color='white', state=tk.NORMAL)
            self.btn_3.configure(width=90, height=40, fg_color='#fc60fc', state=tk.DISABLED)
            self.btn_1.place(x=15, y=10)
            self.btn_2.place(x=15, y=60)
            self.btn_3.place(x=5, y=110)
        else:
            self.btn_3.configure(width=70, height=30, fg_color='white')
            self.btn_3.place(x=15, y=110)
    
    def click_btn_1(self):
        self.selection_btns[0] = True
        self.selection_btns[1] = False
        self.selection_btns[2] = False

        self.lbl_tex_.configure(text='Btn 1 Select', fg_color='#ff1cff')
    def click_btn_2(self):
        self.selection_btns[0] = False
        self.selection_btns[1] = True
        self.selection_btns[2] = False

        self.lbl_tex_.configure(text='Btn 2 Select', fg_color='#fc60fc')
    def click_btn_3(self):
        self.selection_btns[0] = False
        self.selection_btns[1] = False
        self.selection_btns[2] = True

        self.lbl_tex_.configure(text='Btn 3 Select', fg_color='#fa91fa')


if __name__ == '__main__':
    app = App()
    app.mainloop()
