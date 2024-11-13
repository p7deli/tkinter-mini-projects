from customtkinter import CTkLabel, CTkButton
import tkinter as tk


WIDTH = 600
HEIGHT = 500


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.x = ((self.winfo_screenwidth() // 2) - (WIDTH // 2))
        self.y = ((self.winfo_screenheight() // 2) - (HEIGHT // 2))

        self.title('Timer')
        self.geometry(f'{WIDTH}x{HEIGHT}+{self.x}+{self.y}')
        self.resizable(False, False)

        # ------------------------------------
        self.milliseconds = 0
        # ------------------------------------

        self.lbl_timer = CTkLabel(self, text='00:00:00', font=('Comic Sans Ms', 60, 'bold'),
                                  width=590, height=200)
        self.lbl_timer.place(x=5, y=5)

        self.btn_start = CTkButton(self, text='start', font=('Comic Sans Ms', 20, 'bold'), fg_color='#92f587',
                                   hover_color='#80fc32', border_width=2, border_color='#80fc32', width=150, height=50,
                                   text_color='black', command=self.update_timer)
        self.btn_start.place(x=50, y=250)

        self.btn_pause = CTkButton(self, text='Pause', font=('Comic Sans Ms', 20, 'bold'), fg_color='#fa645f',
                                   hover_color='#f52e27', border_width=2, border_color='#f52e27', width=150, height=50,
                                   text_color='black', command=self.pause_time)
        self.btn_pause.place(x=210, y=250)

        self.btn_rest = CTkButton(self, text='Reset', font=('Comic Sans Ms', 20, 'bold'), fg_color='#f7ab6d',
                                   hover_color='#f79545', border_width=2, border_color='#fc9e51', width=150, height=50,
                                   text_color='black',command=self.reset_time)
        self.btn_rest.place(x=370, y=250)


    def update_timer(self):
        minutes = (self.milliseconds // 1000) // 60
        seconds = (self.milliseconds // 1000) % 60
        centiseconds = (self.milliseconds // 10) % 100

        self.lbl_timer.configure(text=f'{minutes:02}:{seconds:02}:{centiseconds:02}')
        self.after_timer = self.after(10, self.update_timer)
        self.milliseconds += 10
    
    def pause_time(self):
        self.after_cancel(self.after_timer)
        self.btn_start.configure(text='Resume')
    
    def reset_time(self):
        self.after_cancel(self.after_timer)
        self.milliseconds = 0
        minutes = (self.milliseconds // 1000) // 60
        seconds = (self.milliseconds // 1000) % 60
        centiseconds = (self.milliseconds // 10) % 100

        self.lbl_timer.configure(text=f'{minutes:02}:{seconds:02}:{centiseconds:02}')
        self.btn_start.configure(text='Start')


if __name__ == '__main__':
    app = App()
    app.mainloop()