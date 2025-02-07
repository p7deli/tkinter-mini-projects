import tkinter as tk
from customtkinter import CTkLabel, CTkFrame, CTkButton, CTkImage, CTkEntry
from PIL import Image


WIDTH, HEIGHT = 650, 450

class LoginRegisterForm(tk.Tk):
    def __init__(self):
        super().__init__()

        # ----------------------------
        self.x = ((self.winfo_screenwidth() // 2) - (WIDTH // 2))
        self.y = ((self.winfo_screenheight() // 2) - (HEIGHT // 2))
        self.state_login = True
        self.state_register = True
        self.fx_login = 0
        self.fx_register = 0
        # ---------------------------- Images
        self.img_background = Image.open('pictures/login.jpg')
        self.ph_background = CTkImage(self.img_background, size=(320, 320))

        self.img_username = Image.open('pictures/username.png')
        self.ph_username = CTkImage(self.img_username, size=(30, 30))

        self.img_password = Image.open('pictures/password.png')
        self.ph_password = CTkImage(self.img_password, size=(30, 30))

        self.img_show = Image.open('pictures/show.png')
        self.ph_show = CTkImage(self.img_show, size=(30, 30))

        self.img_hide = Image.open('pictures/hide.png')
        self.ph_hide = CTkImage(self.img_hide, size=(30, 30))

        self.img_fname_lname = Image.open('pictures/fname_lname.png')
        self.ph_fname_lname = CTkImage(self.img_fname_lname, size=(30, 30))
        # ----------------------------

        self.title('login Register Form')
        self.geometry(f'{WIDTH}x{HEIGHT}+{self.x}+{self.y}')
        self.resizable(False, False)
        self.config(bg='white')

        # ----------------------------
        CTkLabel(self, text='', image=self.ph_background).place(x=0, y=50)

        # ------------------------ login Form
        self.frame_login = CTkFrame(self, width=300, height=HEIGHT-20, fg_color='white')
        self.frame_login.place(x=345, y=10)

        CTkLabel(self.frame_login, text='login Form', font=('Comic Sans Ms', 35, 'bold'), fg_color='white',
                 text_color='#c069ff', width=290, height=60).place(x=5, y=40)

        self.frame_username_login = CTkFrame(self.frame_login, width=290, height=50, border_width=2,
                                             border_color='black', fg_color='white', corner_radius=10)
        self.frame_username_login.place(x=5, y=180)

        self.txt_username_login = CTkEntry(self.frame_username_login, width=180, height=40, font=('Comic Sans Ms', 20, 'bold'),
                                border_width=0, text_color='black', fg_color='white')
        self.txt_username_login.place(x=55, y=5)

        CTkLabel(self.frame_username_login, text='', image=self.ph_username).place(x=10, y=10)

        self.frame_password_login = CTkFrame(self.frame_login, width=290, height=50, border_width=2,
                                             border_color='black', fg_color='white', corner_radius=10)
        self.frame_password_login.place(x=5, y=250)

        CTkLabel(self.frame_password_login, text='', image=self.ph_password).place(x=10, y=10)

        self.txt_password_login = CTkEntry(self.frame_password_login, width=180, height=40, font=('Comic Sans Ms', 20, 'bold'),
                                border_width=0, text_color='black', fg_color='white')
        self.txt_password_login.place(x=55, y=5)

        self.btn_show_hide_password_login = CTkButton(self.frame_password_login, width=40, height=40, text='',
                                image=self.ph_show, fg_color='white', hover_color='#f28fff', command=self.Show_hide_login_password)
        self.btn_show_hide_password_login.place(x=240, y=5)

        CTkButton(self.frame_login, width=120, height=40, text='Login', text_color='white', border_width=2,
                                fg_color='#b858fc', hover_color='#f28fff', border_color='#f28fff',
                                font=('Comic Sans Ms', 15, 'bold'), corner_radius=10).place(x=25, y=320)
        CTkButton(self.frame_login, width=120, height=40, text='Register', text_color='white', border_width=2,
                                fg_color='#b858fc', hover_color='#f28fff', border_color='#f28fff',
                                font=('Comic Sans Ms', 15, 'bold'), corner_radius=10, command=self.go_register).place(x=150, y=320)

        # ------------------------ Register Form
        self.frame_register = CTkFrame(self, width=300, height=HEIGHT-20, fg_color='white')
        self.frame_register.place_forget()

        CTkLabel(self.frame_register, text='Register Form', font=('Comic Sans Ms', 35, 'bold'), fg_color='white',
                 text_color='#c069ff', width=290, height=60).place(x=5, y=40)

        self.frame_fname_register = CTkFrame(self.frame_register, width=290, height=50, border_width=2,
                                             border_color='black', fg_color='white', corner_radius=10)
        self.frame_fname_register.place(x=5, y=120)

        self.txt_fname_register = CTkEntry(self.frame_fname_register, width=180, height=40, font=('Comic Sans Ms', 20, 'bold'),
                                border_width=0, text_color='black', fg_color='white')
        self.txt_fname_register.place(x=55, y=5)

        CTkLabel(self.frame_fname_register, text='', image=self.ph_fname_lname).place(x=10, y=10)

        self.frame_lname_register = CTkFrame(self.frame_register, width=290, height=50, border_width=2,
                                             border_color='black', fg_color='white', corner_radius=10)
        self.frame_lname_register.place(x=5, y=180)

        CTkLabel(self.frame_lname_register, text='', image=self.ph_fname_lname).place(x=10, y=10)

        self.txt_lname_register = CTkEntry(self.frame_lname_register, width=180, height=40, font=('Comic Sans Ms', 20, 'bold'),
                                border_width=0, text_color='black', fg_color='white')
        self.txt_lname_register.place(x=55, y=5)

        self.frame_username_register = CTkFrame(self.frame_register, width=290, height=50, border_width=2,
                                             border_color='black', fg_color='white', corner_radius=10)
        self.frame_username_register.place(x=5, y=240)

        CTkLabel(self.frame_username_register, text='', image=self.ph_username).place(x=10, y=10)

        self.txt_username_register = CTkEntry(self.frame_username_register, width=180, height=40, font=('Comic Sans Ms', 20, 'bold'),
                                border_width=0, text_color='black', fg_color='white')
        self.txt_username_register.place(x=55, y=5)


        self.frame_password_register = CTkFrame(self.frame_register, width=290, height=50, border_width=2,
                                             border_color='black', fg_color='white', corner_radius=10)
        self.frame_password_register.place(x=5, y=300)

        CTkLabel(self.frame_password_register, text='', image=self.ph_password).place(x=10, y=10)

        self.txt_password_register = CTkEntry(self.frame_password_register, width=180, height=40, font=('Comic Sans Ms', 20, 'bold'),
                                border_width=0, text_color='black', fg_color='white')
        self.txt_password_register.place(x=55, y=5)

        self.btn_show_hide_password_register = CTkButton(self.frame_password_register, width=40, height=40, text='',
                                image=self.ph_show, fg_color='white', hover_color='#f28fff', command=self.Show_hide_register_password)
        self.btn_show_hide_password_register.place(x=240, y=5)

        CTkButton(self.frame_register, width=120, height=40, text='Register', text_color='white', border_width=2,
                                fg_color='#b858fc', hover_color='#f28fff', border_color='#f28fff',
                                font=('Comic Sans Ms', 15, 'bold'), corner_radius=10).place(x=25, y=360)
        CTkButton(self.frame_register, width=120, height=40, text='Login', text_color='white', border_width=2,
                                fg_color='#b858fc', hover_color='#f28fff', border_color='#f28fff',
                                font=('Comic Sans Ms', 15, 'bold'), corner_radius=10, command=self.go_login).place(x=150, y=360)

        
    def Show_hide_login_password(self):
        if self.state_login:
            self.btn_show_hide_password_login.configure(image=self.ph_hide)
            self.state_login = False
            self.txt_password_login.configure(show='*')
        else:
            self.btn_show_hide_password_login.configure(image=self.ph_show)
            self.state_login = True
            self.txt_password_login.configure(show='')
    
    def Show_hide_register_password(self):
        if self.state_register:
            self.btn_show_hide_password_register.configure(image=self.ph_hide)
            self.state_register = False
            self.txt_password_register.configure(show='*')
        else:
            self.btn_show_hide_password_register.configure(image=self.ph_show)
            self.state_register = True
            self.txt_password_register.configure(show='')
    
    def go_login(self):
        if self.fx_login == 320:
            self.fx_login = 0
            return
        self.frame_register.place_forget()
        self.fx_login += 1
        self.frame_login.place(x=self.fx_login, y=5)
        self.after(2, self.go_login)

    def go_register(self):
        if self.fx_register == 320:
            self.fx_register = 0
            return
        self.frame_login.place_forget()
        self.fx_register += 1
        self.frame_register.place(x=self.fx_register, y=5)
        self.after(2, self.go_register)




if __name__ == '__main__':
    app = LoginRegisterForm()
    app.mainloop()