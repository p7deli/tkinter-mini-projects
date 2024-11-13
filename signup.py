from customtkinter import CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkFrame
import tkinter as tk
from tkinter import messagebox


WIDTH = 700
HEIGHT = 670

class SignUp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --------------------------------------- نحوه قراردادن پنجره در وسط اسکرین
        self.x = ((self.winfo_screenwidth() // 2) - (WIDTH // 2))
        self.y = ((self.winfo_screenheight() // 2) - (HEIGHT // 2)) - 30

        # --------------------------------------- Var
        self.state_txt = [False, False, False, False, False]
        # --------------------------------------- Setting
        self.title('SignUp')
        self.geometry(f'{WIDTH}x{HEIGHT}+{self.x}+{self.y}')
        self.resizable(False, False)
        self.config(bg='#30302f')
        # --------------------------------------- Widget
        self.fstart_ = CTkFrame(self, width=550, height=620,
                 fg_color='white', corner_radius=15)
        self.fstart_.place(x=75, y=25)
        
        CTkLabel(self.fstart_, text='Sign Up', width=540, height=50, font=('Comic Sans Ms', 50, 'bold'),
                 fg_color='white', corner_radius=15, anchor='center', text_color='black').place(x=5, y=50)
        
        
        CTkLabel(self.fstart_, text='First Name', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
                 fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=170)
        self.txt_fname = CTkEntry(self.fstart_, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                                  bg_color='black', border_width=4)
        self.txt_fname.place(x=265, y=180)
        self.txt_fname.bind('<KeyRelease>', self.check_fname)
        
        CTkLabel(self.fstart_, text='Last Name', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
                 fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=240)
        self.txt_lname = CTkEntry(self.fstart_, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                                  bg_color='black', border_width=4)
        self.txt_lname.place(x=265, y=250)
        self.txt_lname.bind('<KeyRelease>', self.check_lname)
        
        CTkLabel(self.fstart_, text='Email', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
                 fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=310)
        self.txt_email = CTkEntry(self.fstart_, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                                  bg_color='black', border_width=4)
        self.txt_email.place(x=265, y=320)
        self.txt_email.bind('<KeyRelease>', self.check_email)
        
        CTkLabel(self.fstart_, text='Password', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
                 fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=380)
        self.txt_pass1 = CTkEntry(self.fstart_, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                                  bg_color='black', show='*', border_width=4)
        self.txt_pass1.place(x=265, y=390)
        self.txt_pass1.bind('<KeyRelease>', self.check_pass1)
        
        CTkLabel(self.fstart_, text='Confirm Password', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
                 fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=450)
        self.txt_pass2 = CTkEntry(self.fstart_, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                                  bg_color='black', show='*', border_width=4)
        self.txt_pass2.place(x=265, y=460)
        self.txt_pass2.bind('<KeyRelease>', self.check_pass2)

        self.show_pass = CTkCheckBox(self.fstart_, text="SHOW", font=("Arial", 20, "bold"),
                                           text_color="black", fg_color="#00558f", hover_color='gray',
                                           border_color="black", bg_color='white', command=self.show_hide_pass)
        self.show_pass.place(x=240, y=520)

        self.btn_sub = CTkButton(self.fstart_, text='Sign Up', font=('Comic Sans Ms', 20, 'bold'), width=500, height=50,
                                 fg_color='black', border_width=2, border_color='#616161', hover_color='#616161',
                                 bg_color='white', corner_radius=10, command=self.sub_)
        self.btn_sub.place(x=20, y=550)
        
        # -------------------------------------------------------------------------------------------
        self.frame_ = CTkFrame(self, width=690, height=660,
                 fg_color='#3d3d3d', corner_radius=15)
        self.frame_.place_forget()
        
        CTkLabel(self.frame_, text='Hello Welcome To My App', width=690, height=50, font=('Comic Sans Ms', 50, 'bold'),
                 fg_color='#3d3d3d', corner_radius=15, text_color='black').place(x=5, y=250)
        
        # --------------------------------- Functions
    
    def check_fname(self, event):
        fname_ = self.txt_fname.get()

        if fname_.isalpha():
            self.txt_fname.configure(border_color='green')
            self.state_txt[0] = True
        else:
            self.txt_fname.configure(border_color='red')
            self.state_txt[0] = False
    
    def check_lname(self, event):
        lname_ = self.txt_lname.get()

        if lname_.isalpha():
            self.txt_lname.configure(border_color='green')
            self.state_txt[1] = True
        else:
            self.txt_lname.configure(border_color='red')
            self.state_txt[1] = False
    
    def check_email(self, event):
        email = self.txt_email.get()

        if '@' in email and email[email.index('@')+1:] == 'gmail.com':
            self.txt_email.configure(border_color='green')
            self.state_txt[2] = True
        else:
            self.txt_email.configure(border_color='red')
            self.state_txt[2] = False
    
    def check_pass1(self, event):
        pass1 = self.txt_pass1.get()

        if len(pass1) >= 8 and pass1.isnumeric() == False and pass1.isalpha() == False and \
        pass1.isupper() == False and pass1.islower() == False:
            self.txt_pass1.configure(border_color='green')
            self.state_txt[3] = True
        else:
            self.txt_pass1.configure(border_color='red')
            self.state_txt[3] = False
    
    def check_pass2(self, event):
        pass2 = self.txt_pass2.get()

        if pass2 == self.txt_pass1.get():
            self.txt_pass2.configure(border_color='green')
            self.state_txt[4] = True
        else:
            self.txt_pass2.configure(border_color='red')
            self.state_txt[4] = False
        
    def show_hide_pass(self):
        state_ = self.show_pass.get()

        if state_:
            self.txt_pass1.configure(show='')
            self.txt_pass2.configure(show='')
            self.show_pass.configure(text='Hide')
        else:
            self.txt_pass1.configure(show='*')
            self.txt_pass2.configure(show='*')
            self.show_pass.configure(text='Show')

    def sub_(self):
        if self.state_txt[0]:
            if self.state_txt[1]:
                if self.state_txt[2]:
                    if self.state_txt[3]:
                        if self.state_txt[4]:
                            messagebox.showinfo('Signup', 'Signup seccussfully!!')
                            self.fstart_.place_forget()
                            self.frame_.place(x=5, y=5)
                        else:
                            messagebox.showerror('Error', 'confirm password is nut currect!!!')
                    else:
                        messagebox.showerror('Error', 'password is nut currect!!!')
                else:
                    messagebox.showerror('Error', 'email is nut currect!!!')
            else:
                messagebox.showerror('Error', 'last name is nut currect!!!')
        else:
            messagebox.showerror('Error', 'first name is nut currect!!!')


if __name__ == '__main__':
    app = SignUp()
    app.mainloop()
