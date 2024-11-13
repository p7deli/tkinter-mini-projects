import tkinter as tk
from customtkinter import CTkButton, CTkLabel


WIDTH = 600
HEIGHT = 700


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        # --------------------------- Var -----------------------------
        self.x = ((self.winfo_screenwidth() // 2) - (WIDTH // 2))
        self.y = ((self.winfo_screenheight() // 2) - (HEIGHT // 2))
        self.Buttons = []
        self.board_ = ["", "", "", "", "", "", "", "", ""]
        self.turn_ = 'X'
        self.x_point, self.o_point = 0, 0
        self.colors = ['#e588f7', '#9de0fc', '#ff94a6', '#f5f0a9']
        self.index_color = 0
        # -------------------------------------------------------------

        self.title('Tic Tac Toe')
        self.geometry(f'{WIDTH}x{HEIGHT}+{self.x}+{self.y}')
        self.resizable(False, False)
        self.config(bg='black')
        self.iconbitmap('')

        # ----------------------------------------------------------------
        self.lbl_player_x = CTkLabel(self, text='X: 0', font=('Comic Sans MS', 40, 'bold'),
                                     text_color='#a2eafa')
        self.lbl_player_x.place(x=100, y=20)

        self.lbl_title = CTkLabel(self, text='TicTacToe', font=('Comic Sans MS', 30, 'bold'),
                                     text_color='#a2eafa')
        self.lbl_title.place(x=220, y=32)

        self.lbl_player_o = CTkLabel(self, text='O: 0', font=('Comic Sans MS', 40, 'bold'),
                                     text_color='#32d6fa')
        self.lbl_player_o.place(x=400, y=20)
        # ----------------------------------------------------------------
        self.lbl_win_x = CTkLabel(self, font=('Comic Sans MS', 40, 'bold'), text='Player X Win',
                                  text_color='red')
        self.lbl_win_x.place_forget()

        self.lbl_win_o = CTkLabel(self, font=('Comic Sans MS', 40, 'bold'), text='Player O Win',
                                  text_color='#32d6fa')
        self.lbl_win_o.place_forget()

        self.lbl_win_equal = CTkLabel(self, font=('Comic Sans MS', 40, 'bold'), text='Equal Game ...',
                                  text_color='#32d6fa')
        self.lbl_win_equal.place_forget()

        self.btn_restart = CTkButton(self, text='Restart', font=('Comic Sans MS', 40, 'bold'), fg_color='black', border_width=0,
                                     hover=False, text_color='white', command=self.end_game)
        self.btn_restart.place_forget()
        self.btn_restart.bind('<Enter>', self.on_enter)
        self.btn_restart.bind("<Leave>", self.on_leave)
        # ----------------------------------------------------------------
        self.canvas_ = tk.Canvas(self, width=450, height=450, bg='black', highlightbackground='black')
        self.canvas_.place(x=70, y=130)
        self.canvas_.create_line(0, 150, 450, 150, fill='white', width=5)
        self.canvas_.create_line(0, 310, 450, 310, fill='white', width=5)
        self.canvas_.create_line(150, 0, 150, 450, fill='white', width=5)
        self.canvas_.create_line(310, 0, 310, 450, fill='white', width=5)

        self.create_button()
        # ---------------------------------------------------------------
    def on_enter(self, event):
        self.btn_restart.configure(text_color='red')
    
    def on_leave(self, event):
        self.btn_restart.configure(text_color='white')

    def change_color(self):
        if self.index_color == 4:
            self.index_color = 0
        
        self.lbl_title.configure(text_color=self.colors[self.index_color])
        self.index_color += 1
        self.after(1000, self.change_color)

    def create_button(self):
        counter, x, y = 1, 0, 0
        for i in range(9):
            self.Buttons.append(i)
            self.Buttons[i] = CTkButton(self.canvas_, text=f"", width=145, height=145,
            font=("Comic Sans MS", 20, "bold"), text_color="black", fg_color="black", hover=False,
            command=lambda x=i: self.move(x))
            self.Buttons[i].place(x=x, y=y)
            x += 158
            if counter == 3:
                y += 158
                counter = 1
                x = 0
            else:
                counter += 1
    
    def move(self, x):
        if self.board_[x] == "":
            if self.turn_ == "X":
                self.board_[x] = "X"
                self.Buttons[x].configure(text="X", text_color="#a2eafa", font=("Comic Sans MS", 80, "bold"))
                self.turn_ = "O"
            else:
                self.board_[x] = "O"
                self.Buttons[x].configure(text="O", text_color="#32d6fa", font=("Comic Sans MS", 80, "bold"))
                self.turn_ = "X"
        self.win()
    
    def win(self):
        if (self.board_[0] == self.board_[1] == self.board_[2]) and self.board_[0] != "":
            self.change_btns(0, 1, 2)
            self.Show_info(self.board_[0])
        elif (self.board_[3] == self.board_[4] == self.board_[5]) and self.board_[3] != "":
            self.change_btns(3, 4, 5)
            self.Show_info(self.board_[3])
        elif (self.board_[6] == self.board_[7] == self.board_[8]) and self.board_[6] != "":
            self.change_btns(6, 7, 8)
            2000, self.Show_info(self.board_[6])

        elif (self.board_[0] == self.board_[3] == self.board_[6]) and self.board_[0] != "":
            self.change_btns(0, 3, 6)
            self.Show_info(self.board_[0])
        elif (self.board_[1] == self.board_[4] == self.board_[7]) and self.board_[1] != "":
            self.change_btns(1, 4, 7)
            self.Show_info(self.board_[1])
        elif (self.board_[2] == self.board_[5] == self.board_[8]) and self.board_[2] != "":
            self.change_btns(2, 5, 8)
            self.Show_info(self.board_[2])
        
        elif (self.board_[0] == self.board_[4] == self.board_[8]) and self.board_[4] != "":
            self.change_btns(0, 4, 8)
            self.Show_info(self.board_[0])
        elif (self.board_[2] == self.board_[4] == self.board_[6]) and self.board_[2] != "":
            self.change_btns(2, 4, 6)
            self.Show_info(self.board_[2])

        elif "" not in self.board_:
            self.lbl_win_equal.place(x=50, y=600)
            self.btn_restart.place(x=410, y=600)
    
    def change_btns(self, x, y, z):
        for i in [x, y, z]:
            self.Buttons[i].configure(text_color='#ff000d', font=("Comic Sans MS", 100, "bold"))

    def Show_info(self, x):
        if x == "X":
            self.lbl_win_x.place(x=50, y=600)
            self.x_point += 1
            self.lbl_player_x.configure(text=f'X: {self.x_point}')
            self.btn_restart.place(x=410, y=600)
        else:
            self.lbl_win_o.place(x=50, y=600)
            self.o_point += 1
            self.lbl_player_o.configure(text=f'O: {self.o_point}')
            self.btn_restart.place(x=410, y=600)
    
    def end_game(self):
        for btn in self.Buttons:
            btn.destroy()
        
        self.Buttons = []
        self.lbl_win_equal.place_forget()
        self.lbl_win_o.place_forget()
        self.lbl_win_x.place_forget()
        self.btn_restart.place_forget()

        self.board_ = ["", "", "", "", "", "", "", "", ""]
        self.turn_ = 'X'
        
        self.create_button()
        

if __name__ == '__main__':

    game = TicTacToe()
    game.change_color()
    game.mainloop()