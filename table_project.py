import tkinter as tk
from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkComboBox
from tkinter.ttk import Treeview, Style
from tkinter import messagebox


WIDTH = 1010
HEIGHT = 700
AGE_COMBO = [str(age) for age in range(6, 19)]
STUDENTS = [
    [15, 'akbari', 'milad', 1], [16, 'deldar', 'mohsen', 2], [14, 'babaei', 'masoud', 3],
    [14, 'mamadi', 'pedram', 4], [16, 'deli', 'poria', 5], [14, 'masoudy', 'ali', 6],
    [17, 'khareji', 'milad', 7], [16, 'abavar', 'mohsen', 8], [14, 'moradi', 'reza', 9],
    [10, 'babazadeh', 'milad', 10], [16, 'hanifeh', 'mohammad', 11], [14, 'daldari', 'bahar', 12],
]
CODE_SELECTION = 0

def add_default_students():
    table_.delete(*table_.get_children())
    for student in STUDENTS:
        table_.insert('', tk.END, values=(student[0], student[1], student[2], student[3]))

def add_student():

    code_ = STUDENTS[-1][3] + 1
    txt_fname = txt_fname_add.get()
    txt_lname = txt_lname_add.get()
    txt_age = txt_age_add.get()

    if txt_fname != '' and txt_fname.isalpha() and txt_lname != '' and txt_lname.isalpha():
        STUDENTS.append([txt_age, txt_lname, txt_fname, code_])
        table_.delete(*table_.get_children())
        add_default_students()
        txt_fname_add.delete('0', tk.END)
        txt_lname_add.delete('0', tk.END)
        txt_age_add.set('6')
    else:
        messagebox.showerror('Error', 'Please enter the requested items')

def selection_edit(event):
    global CODE_SELECTION

    selection_ = table_.selection()
    if selection_:
        value_ = table_.item(selection_, 'values')
        CODE_SELECTION = int(value_[3])
        txt_fname_edit.delete('0', tk.END)
        txt_fname_edit.insert('0', value_[2])

        txt_lname_edit.delete('0', tk.END)
        txt_lname_edit.insert('0', value_[1])

        txt_age_edit.set(value_[0])

def edit_student():
    code_ = CODE_SELECTION
    txt_fname = txt_fname_edit.get()
    txt_lname = txt_lname_edit.get()
    txt_age = txt_age_edit.get()

    if txt_fname != '' and txt_fname.isalpha() and txt_lname != '' and txt_lname.isalpha():
        student_index = None
        for index in range(len(STUDENTS)):
            if code_ == STUDENTS[index][-1]:
                student_index = index
                break
        if student_index != None:
            STUDENTS[student_index] = [txt_age, txt_lname, txt_fname, code_]
            add_default_students()
            txt_fname_edit.delete('0', tk.END)
            txt_lname_edit.delete('0', tk.END)
            messagebox.showinfo('Edit', 'Edit Student Successfully')
    else:
        messagebox.showerror('Error', 'Please enter the requested items')

def delete_student():
    selection_ = table_.selection()
    if selection_:
        code_ = int(table_.item(selection_, 'values')[3])

        student_index = None
        for index in range(len(STUDENTS)):
            if code_ == STUDENTS[index][-1]:
                student_index = index
                break
        if student_index != None:
            STUDENTS.remove(STUDENTS[student_index])
            add_default_students()


window = tk.Tk()

x = ((window.winfo_screenwidth() // 2) - (WIDTH // 2))
y = ((window.winfo_screenheight() // 2) - (HEIGHT // 2))
window.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
window.title('Table App')
window.resizable(False, False)
window.config(bg='black')

style = Style()
style.theme_use('default')

# Frame Left ------------------------------------------------
# Frame Add ------------------------------
frame_left = CTkFrame(window, width=500, height=690, border_width=3, border_color='white', fg_color='#c5d7fc',
                      corner_radius=0)
frame_left.place(x=5, y=5)

f_add_ = tk.LabelFrame(frame_left, width=480, height=330, text='Add Student', fg='black',
                       font=('Arial', 30, 'bold'), bg='#c5d7fc', border=5)
f_add_.place(x=10, y=10)

CTkLabel(f_add_, width=450, height=60, fg_color='#78a3ff', text='First Name',
         anchor='w', text_color='black', font=('Comic Sans Ms', 20, 'bold'),
         corner_radius=10).place(x=5, y=10)
txt_fname_add = CTkEntry(f_add_, width=280, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                         bg_color='#78a3ff', border_color='black')
txt_fname_add.place(x=150, y=20)

CTkLabel(f_add_, width=450, height=60, fg_color='#78a3ff', text='Last Name',
         anchor='w', text_color='black', font=('Comic Sans Ms', 20, 'bold'),
         corner_radius=10).place(x=5, y=80)
txt_lname_add = CTkEntry(f_add_, width=280, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                         bg_color='#78a3ff', border_color='black')
txt_lname_add.place(x=150, y=90)

CTkLabel(f_add_, width=450, height=60, fg_color='#78a3ff', text='Age',
         anchor='w', text_color='black', font=('Comic Sans Ms', 20, 'bold'),
         corner_radius=10).place(x=5, y=150)
txt_age_add = CTkComboBox(f_add_, width=280, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                         bg_color='#78a3ff', border_color='black', values=AGE_COMBO, button_color='#8a87ff',
                         hover=False)
txt_age_add.place(x=150, y=160)

btn_add = CTkButton(f_add_, text='Add Student', font=('Arial', 20, 'bold'), width=450, height=50,
                    border_width=2, border_color='#6764fa', fg_color='#817efc', hover_color='#6764fa',
                    corner_radius=15, command=add_student)
btn_add.place(x=5, y=220)

# Frame Edit ------------------------------
f_edit_ = tk.LabelFrame(frame_left, width=480, height=330, text='Edit Student',
                       font=('Arial', 30, 'bold'), bg='#c5d7fc', bd=5)
f_edit_.place(x=10, y=345)

CTkLabel(f_edit_, width=450, height=60, fg_color='#78a3ff', text='First Name',
         anchor='w', text_color='black', font=('Comic Sans Ms', 20, 'bold'),
         corner_radius=10).place(x=5, y=10)
txt_fname_edit = CTkEntry(f_edit_, width=280, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                         bg_color='#78a3ff', border_color='black')
txt_fname_edit.place(x=150, y=20)

CTkLabel(f_edit_, width=450, height=60, fg_color='#78a3ff', text='Last Name',
         anchor='w', text_color='black', font=('Comic Sans Ms', 20, 'bold'),
         corner_radius=10).place(x=5, y=80)
txt_lname_edit = CTkEntry(f_edit_, width=280, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                         bg_color='#78a3ff', border_color='black')
txt_lname_edit.place(x=150, y=90)

CTkLabel(f_edit_, width=450, height=60, fg_color='#78a3ff', text='Age',
         anchor='w', text_color='black', font=('Comic Sans Ms', 20, 'bold'),
         corner_radius=10).place(x=5, y=150)
txt_age_edit = CTkComboBox(f_edit_, width=280, height=40, font=('Arial', 20, 'bold'), corner_radius=10,
                         bg_color='#78a3ff', border_color='black', values=AGE_COMBO, button_color='#8a87ff',
                         hover=False)
txt_age_edit.place(x=150, y=160)

btn_edit = CTkButton(f_edit_, text='Edit Student', font=('Arial', 20, 'bold'), width=450, height=50,
                    border_width=2, border_color='#6764fa', fg_color='#817efc', hover_color='#6764fa',
                    corner_radius=15, command=edit_student)
btn_edit.place(x=5, y=220)


# Frame Right ------------------------------------------------
frame_right = CTkFrame(window, width=500, height=690, border_width=3, border_color='white', fg_color='#c5d7fc',
                       corner_radius=0)
frame_right.place(x=505, y=5)

# Frame Table
f_table_ = tk.LabelFrame(frame_right, text='Table',
                       font=('Arial', 30, 'bold'), bg='#c5d7fc', bd=5)
f_table_.place(x=10, y=10)

scrollbar_1 = tk.Scrollbar(f_table_, orient="vertical")
scrollbar_1.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

scrollbar_2 = tk.Scrollbar(f_table_, orient="horizontal")
scrollbar_2.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
columns = ['age', 'lname', 'fname', 'code']
table_ = Treeview(f_table_, columns=columns, height=25, show='headings',
                  xscrollcommand=scrollbar_2.set, yscrollcommand=scrollbar_1.set)

for column in columns:
    if column == 'code':
        table_.heading(column, text=column, anchor="center")
        table_.column(column, anchor="center", width=50)
    else:
        table_.heading(column, text=column, anchor="center")
        table_.column(column, anchor="center", width=127)

table_.pack(padx=5, pady=5)
table_.bind('<Double-1>', selection_edit)
scrollbar_1.config(command=table_.yview)
scrollbar_2.config(command=table_.xview)
add_default_students()

btn_delete = CTkButton(frame_right, text='Delete Student', font=('Arial', 20, 'bold'), width=450, height=50,
                    border_width=2, border_color='#ff0f0f', fg_color='#ff5757', hover_color='#ff0f0f',
                    corner_radius=15, text_color='white', command=delete_student)
btn_delete.place(x=25, y=630)

window.mainloop()