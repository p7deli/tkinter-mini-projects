from customtkinter import CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkFrame
import tkinter as tk
from tkinter import messagebox
from database_ import add_user, check_user


def show_hide_pass():
    
    state_ = show_pass1.get()

    if state_:
        txt_pass1.configure(show='')
        txt_pass2.configure(show='')
        show_pass1.configure(text='Hide')
    else:
        txt_pass1.configure(show='*')
        txt_pass2.configure(show='*')
        show_pass1.configure(text='Show')

def show_hide_pass_log():
    state_ = show_pass2.get()

    if state_:
        txt_pass_log.configure(show='')
        show_pass2.configure(text='Hide')
    else:
        txt_pass_log.configure(show='*')
        show_pass2.configure(text='Show')

def signup():
    fname = txt_fname.get()
    lname = txt_lname.get()
    email = txt_email.get()
    password1_ = txt_pass1.get()
    password2_ = txt_pass2.get()

    if fname != '' and lname != '' and email != '' and password1_ != '' and password2_ != '':
        if password1_ == password2_:
            add_user(fname, lname, email, password1_)
            messagebox.showinfo('Successfully', 'add user successfully!!!')
            txt_fname.delete('0', tk.END)
            txt_lname.delete('0', tk.END)
            txt_email.delete('0', tk.END)
            txt_pass1.delete('0', tk.END)
            txt_pass2.delete('0', tk.END)
        else:
            messagebox.showerror('Error', 'The passwords do not match')
    else:
        messagebox.showerror('Error', 'please enter all txt')

def go_login():
    frame_login.place(x=5, y=5)
    frame_sign_up.place_forget()

def go_signup():
    frame_login.place_forget()
    frame_sign_up.place(x=5, y=5)

def login():
    email_ = txt_email_log.get()
    password_ = txt_pass_log.get()

    result_ = check_user(email_, password_)
    if result_:
        messagebox.showinfo('Login', 'Login Successfully!!')
    else:
        messagebox.showerror('Login', 'email or password not curect!!!')


window = tk.Tk()

window.geometry('540x640')
window.config(bg='black')

frame_sign_up = CTkFrame(window, fg_color='white', width=530, height=630)
frame_sign_up.place(x=5, y=5)

CTkLabel(frame_sign_up, text='Sign Up', width=540, height=50, font=('Comic Sans Ms', 50, 'bold'),
            fg_color='white', corner_radius=15, anchor='center', text_color='black').place(x=5, y=50)

CTkLabel(frame_sign_up, text='First Name', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
            fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=170)
txt_fname = CTkEntry(frame_sign_up, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                            bg_color='black', border_width=4)
txt_fname.place(x=265, y=180)

CTkLabel(frame_sign_up, text='Last Name', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
            fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=240)
txt_lname = CTkEntry(frame_sign_up, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                            bg_color='black', border_width=4)
txt_lname.place(x=265, y=250)

CTkLabel(frame_sign_up, text='Email', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
            fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=310)
txt_email = CTkEntry(frame_sign_up, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                            bg_color='black', border_width=4)
txt_email.place(x=265, y=320)

CTkLabel(frame_sign_up, text='Password', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
            fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=380)
txt_pass1 = CTkEntry(frame_sign_up, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                            bg_color='black', show='*', border_width=4)
txt_pass1.place(x=265, y=390)

CTkLabel(frame_sign_up, text='Confirm Password', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
            fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=450)
txt_pass2 = CTkEntry(frame_sign_up, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                            bg_color='black', show='*', border_width=4)
txt_pass2.place(x=265, y=460)

show_pass1 = CTkCheckBox(frame_sign_up, text="SHOW", font=("Arial", 20, "bold"),
                                    text_color="black", fg_color="#00558f", hover_color='gray',
                                    border_color="black", bg_color='white', command=show_hide_pass)
show_pass1.place(x=240, y=520)

# ------------------------------------------------------------------
CTkButton(frame_sign_up, text='Sign Up', font=('Comic Sans Ms', 20, 'bold'), width=240, height=50,
                            fg_color='black', border_width=2, border_color='#616161', hover_color='#616161',
                            bg_color='white', corner_radius=10, command=signup).place(x=20, y=550)


CTkButton(frame_sign_up, text='Login', font=('Comic Sans Ms', 20, 'bold'), width=240, height=50,
                            fg_color='black', border_width=2, border_color='#616161', hover_color='#616161',
                            bg_color='white', corner_radius=10, command=go_login).place(x=270, y=550)


# ----------------------------------------------------------------- Login
frame_login = CTkFrame(window, fg_color='white', width=530, height=630)
frame_login.place_forget()

CTkLabel(frame_login, text='Login', width=540, height=50, font=('Comic Sans Ms', 50, 'bold'),
            fg_color='white', corner_radius=15, anchor='center', text_color='black').place(x=5, y=50)

CTkLabel(frame_login, text='Email', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
            fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=210)
txt_email_log = CTkEntry(frame_login, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                            bg_color='black', border_width=4)
txt_email_log.place(x=265, y=220)

CTkLabel(frame_login, text='Password', width=500, height=60, font=('Comic Sans Ms', 20, 'bold'),
            fg_color='black', corner_radius=10, anchor='w', text_color='white', bg_color='white').place(x=20, y=280)
txt_pass_log = CTkEntry(frame_login, width=250, height=40, font=('Arial', 20, 'bold'), corner_radius=10, show='*',
                            bg_color='black', border_width=4)
txt_pass_log.place(x=265, y=290)

show_pass2 = CTkCheckBox(frame_login, text="SHOW", font=("Arial", 20, "bold"),
                                    text_color="black", fg_color="#00558f", hover_color='gray',
                                    border_color="black", bg_color='white', command=show_hide_pass_log)
show_pass2.place(x=240, y=350)

CTkButton(frame_login, text='Login', font=('Comic Sans Ms', 20, 'bold'), width=240, height=50,
                            fg_color='black', border_width=2, border_color='#616161', hover_color='#616161',
                            bg_color='white', corner_radius=10, command=login).place(x=20, y=380)


CTkButton(frame_login, text='Signup', font=('Comic Sans Ms', 20, 'bold'), width=240, height=50,
                            fg_color='black', border_width=2, border_color='#616161', hover_color='#616161',
                            bg_color='white', corner_radius=10, command=go_signup).place(x=270, y=380)

window.mainloop()
