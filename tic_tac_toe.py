from tkinter import *
import random

class Game:
    def __init__(self, root):
        #==================== Display ====================#
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x500+200+50")
        self.root.resizable(False, False)
        self.root.config(bg='white')

        #==================== Title ====================#
        title = Label(root, text="Tic Tac Toe", font=('times new roman', 30), bg="#262626", fg='white').pack(side=TOP, fill=X)

        #==================== Result ====================#
        self.result = Label(self.root, text="", font=('times new roman', 20), bg="white", fg='black')
        self.result.place(x=20,y=410)

        #==================== Box ====================#
        line_1 = Label(self.root, bg='black').place(x=0,y=100, height=2, width=1250)
        line_6 = Label(self.root, bg='black').place(x=0,y=98, height=2, width=1250)
        line_2 = Label(self.root, bg='black').place(x=0,y=200, height=2, width=1250)
        line_3 = Label(self.root, bg='black').place(x=0,y=300, height=2, width=1250)
        line_4 = Label(self.root, bg='black').place(x=100,y=100, height=100, width=2)
        line_5 = Label(self.root, bg='black').place(x=200,y=100, height=100, width=2)

        #==================== Button ====================#
        self.btn_1 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.one)
        self.btn_1.place(x=0,y=100,height=100,width=100)

        self.btn_4 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.four)
        self.btn_4.place(x=0,y=200,height=100,width=100)

        self.btn_7 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.seven)
        self.btn_7.place(x=0,y=300,height=100,width=100)
        
        self.btn_2 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.two)
        self.btn_2.place(x=100,y=100,height=100,width=100)

        self.btn_5 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.five)
        self.btn_5.place(x=100,y=200,height=100,width=100)

        self.btn_8 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.eight)
        self.btn_8.place(x=100,y=300,height=100,width=100)

        self.btn_3 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.three)
        self.btn_3.place(x=200,y=100,height=100,width=100)

        self.btn_6 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.six)
        self.btn_6.place(x=200,y=200,height=100,width=100)

        self.btn_9 = Button(self.root,text="",font=("times new roman", 100),bg="white",fg="white",cursor='hand2', command=self.nine)
        self.btn_9.place(x=200,y=300,height=100,width=100)

        self.btn_reset = Button(self.root,text="Reset",font=("times new roman", 13),bg="red",fg="white",cursor='hand2', command=self.reset)
        self.btn_reset.place(x=100,y=450,height=40,width=100)

        # =============variable ===============
        self.number_list = ["1","2","3","4","5","6","7","8","9"]
        self.computer_list = []
        self.user_list = []
        
    # ==================== Functions ====================
    # ==================== Buttons ====================
    def one(self):
        self.user_list.append("1")
        self.number_list.remove("1")
        self.backend()
        self.btn_1.config(text="X")
        self.btn_1.config(state=DISABLED)

    def two(self):
        self.user_list.append("2")
        self.number_list.remove("2")
        self.backend()
        self.btn_2.config(text="X")
        self.btn_2.config(state=DISABLED)

    def three(self):
        self.user_list.append("3")
        self.number_list.remove("3")
        self.backend()
        self.btn_3.config(text="X")
        self.btn_3.config(state=DISABLED)

    def four(self):
        self.user_list.append("4")
        self.number_list.remove("4")
        self.backend()
        self.btn_4.config(text="X")
        self.btn_4.config(state=DISABLED)

    def five(self):
        self.user_list.append("5")
        self.number_list.remove("5")
        self.backend()
        self.btn_5.config(text="X")
        self.btn_5.config(state=DISABLED)

    def six(self):
        self.user_list.append("6")
        self.number_list.remove("6")
        self.backend()
        self.btn_6.config(text="X")
        self.btn_6.config(state=DISABLED)

    def seven(self):
        self.user_list.append("7")
        self.number_list.remove("7")
        self.backend()
        self.btn_7.config(text="X")
        self.btn_7.config(state=DISABLED)

    def eight(self):
        self.user_list.append("8")
        self.number_list.remove("8")
        self.backend()
        self.btn_8.config(text="X")
        self.btn_8.config(state=DISABLED)

    def nine(self):
        self.user_list.append("9")
        self.number_list.remove("9")
        self.backend()
        self.btn_9.config(text="X")
        self.btn_9.config(state=DISABLED)

    def reset(self):
        self.btn_8.config(text="")
        self.btn_7.config(text="")
        self.btn_6.config(text="")
        self.btn_9.config(text="")
        self.btn_5.config(text="")
        self.btn_4.config(text="")
        self.btn_3.config(text="")
        self.btn_2.config(text="")
        self.btn_1.config(text="")
        self.btn_1.config(state=NORMAL)
        self.btn_2.config(state=NORMAL)
        self.btn_3.config(state=NORMAL)
        self.btn_4.config(state=NORMAL)
        self.btn_5.config(state=NORMAL)
        self.btn_6.config(state=NORMAL)
        self.btn_7.config(state=NORMAL)
        self.btn_8.config(state=NORMAL)
        self.btn_9.config(state=NORMAL)
        self.result.config(text="")
        self.computer_list = []
        self.user_list = []
        self.number_list = ["1","2","3","4","5","6","7","8","9"]
    
    def computer_won(self):
        self.result.config(text = "Computer Won")
        self.result.config(fg="red")
        self.disable_btn()
    
    def user_won(self):
        self.result.config(text = "User Won")
        self.result.config(fg="green")
        self.disable_btn()

    def disable_btn(self):
        self.btn_1.config(state=DISABLED)
        self.btn_2.config(state=DISABLED)
        self.btn_3.config(state=DISABLED)
        self.btn_4.config(state=DISABLED)
        self.btn_5.config(state=DISABLED)
        self.btn_6.config(state=DISABLED)
        self.btn_7.config(state=DISABLED)
        self.btn_8.config(state=DISABLED)
        self.btn_9.config(state=DISABLED)

    # ==================== Backend Logic ====================
    def backend(self):
        if len(self.number_list) != 0:
            
            # ========== Computer's choice ==========
            self.computer_choice = random.choice(self.number_list)
            self.computer_list.append(self.computer_choice)

            if self.computer_choice == "1":
                self.btn_1.config(text="O")
                self.btn_1.config(state=DISABLED)

            elif self.computer_choice == "2":
                self.btn_2.config(text="O")
                self.btn_2.config(state=DISABLED)

            elif self.computer_choice == "3":
                self.btn_3.config(text="O")
                self.btn_3.config(state=DISABLED)

            elif self.computer_choice == "4":
                self.btn_4.config(text="O")
                self.btn_4.config(state=DISABLED)

            elif self.computer_choice == "5":
                self.btn_5.config(text="O")
                self.btn_5.config(state=DISABLED)

            elif self.computer_choice == "6":
                self.btn_6.config(text="O")
                self.btn_6.config(state=DISABLED)

            elif self.computer_choice == "7":
                self.btn_7.config(text="O")
                self.btn_7.config(state=DISABLED)

            elif self.computer_choice == "8":
                self.btn_8.config(text="O")
                self.btn_8.config(state=DISABLED)

            elif self.computer_choice == "9":
                self.btn_9.config(text="O")
                self.btn_9.config(state=DISABLED)
                
            self.number_list.remove(str(self.computer_choice))

            # ==================== Permutation and Combinations ====================
            # ========== Computer ==========
            # ===== 1 =====
            if "1" in self.computer_list:
                if "4" in self.computer_list:
                    if "7" in self.computer_list:
                        self.computer_won()
                           
                if "7" in self.computer_list:
                    if "4" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "9" in self.computer_list:
                        self.computer_won()
                        
                if "9" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
                if "2" in self.computer_list:
                    if "3" in self.computer_list:
                        self.computer_won()
                        
                if "3" in self.computer_list:
                    if "2" in self.computer_list:
                        self.computer_won()
                        
            # ===== 2 =====
            if "2" in self.computer_list:
                if "1" in self.computer_list:
                    if "3" in self.computer_list:
                        self.computer_won()
                        
                if "3" in self.computer_list:
                    if "1" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "8" in self.computer_list:
                        self.computer_won()
                        
                if "8" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
            # ===== 3 =====
            if "3" in self.computer_list:
                if "2" in self.computer_list:
                    if "1" in self.computer_list:
                        self.computer_won()
                        
                if "1" in self.computer_list:
                    if "2" in self.computer_list:
                        self.computer_won()
                        
                if "6" in self.computer_list:
                    if "9" in self.computer_list:
                        self.computer_won()
                        
                if "9" in self.computer_list:
                    if "6" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "7" in self.computer_list:
                        self.computer_won()
                        
                if "7" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
            # ===== 4 ====
            if "4" in self.computer_list:
                if "1" in self.computer_list:
                    if "7" in self.computer_list:
                        self.computer_won()
                        
                if "7" in self.computer_list:
                    if "1" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "6" in self.computer_list:
                        self.computer_won()
                        
                if "6" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
            # ==== 5 ====
            if "5" in self.computer_list:
                if "7" in self.computer_list:
                    if "3" in self.computer_list:
                        self.computer_won()
                        
                if "3" in self.computer_list:
                    if "7" in self.computer_list:
                        self.computer_won()
                        
                if "2" in self.computer_list:
                    if "8" in self.computer_list:
                        self.computer_won()
                        
                if "8" in self.computer_list:
                    if "2" in self.computer_list:
                        self.computer_won()
                        
                if "1" in self.computer_list:
                    if "9" in self.computer_list:
                        self.computer_won()
                        
                if "9" in self.computer_list:
                    if "1" in self.computer_list:
                        self.computer_won()
                        
                if "4" in self.computer_list:
                    if "6" in self.computer_list:
                        self.computer_won()
                        
                if "6" in self.computer_list:
                    if "4" in self.computer_list:
                        self.computer_won()
                        
            # ===== 6 =====
            if "6" in self.computer_list:
                if "3" in self.computer_list:
                    if "9" in self.computer_list:
                        self.computer_won()
                        
                if "9" in self.computer_list:
                    if "3" in self.computer_list:
                        self.computer_won()
                        
                if "4" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "4" in self.computer_list:
                        self.computer_won()
                         
            # ===== 7 =====
            if "7" in self.computer_list:
                if "4" in self.computer_list:
                    if "1" in self.computer_list:
                        self.computer_won()
                        
                if "1" in self.computer_list:
                    if "4" in self.computer_list:
                        self.computer_won()
                         
                if "8" in self.computer_list:
                    if "9" in self.computer_list:
                        self.computer_won()
                        
                if "9" in self.computer_list:
                    if "8" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "3" in self.computer_list:
                        self.computer_won()
                        
                if "3" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
            # ===== 8 =====
            if "8" in self.computer_list:
                if "9" in self.computer_list:
                    if "7" in self.computer_list:
                        self.computer_won()
                        
                if "7" in self.computer_list:
                    if "9" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "2" in self.computer_list:
                        self.computer_won()
                        
                if "2" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
            # ===== 9 =====
            if "9" in self.computer_list:
                if "8" in self.computer_list:
                    if "7" in self.computer_list:
                        self.computer_won()
                        
                if "7" in self.computer_list:
                    if "8" in self.computer_list:
                        self.computer_won()
                        
                if "5" in self.computer_list:
                    if "1" in self.computer_list:
                        self.computer_won()
                        
                if "1" in self.computer_list:
                    if "5" in self.computer_list:
                        self.computer_won()
                        
                if "6" in self.computer_list:
                    if "3" in self.computer_list:
                        self.computer_won()
                        
                if "3" in self.computer_list:
                    if "6" in self.computer_list:
                        self.computer_won()
                        
            # ========== User ==========
            # ===== 1 =====
            if "1" in self.user_list:
                if "4" in self.user_list:
                    if "7" in self.user_list:
                        self.user_won()
                       
                if "7" in self.user_list:
                    if "4" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "9" in self.user_list:
                        self.user_won()
                        
                if "9" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
                if "2" in self.user_list:
                    if "3" in self.user_list:
                        self.user_won()
                        
                if "3" in self.user_list:
                    if "2" in self.user_list:
                        self.user_won()
                        
            # ===== 2 =====
            if "2" in self.user_list:
                if "1" in self.user_list:
                    if "3" in self.user_list:
                        self.user_won()
                        
                if "3" in self.user_list:
                    if "1" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "8" in self.user_list:
                        self.user_won()
                        
                if "8" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
            # ===== 3 =====
            if "3" in self.user_list:
                if "2" in self.user_list:
                    if "1" in self.user_list:
                        self.user_won()
                        
                if "1" in self.user_list:
                    if "2" in self.user_list:
                        self.user_won()
                        
                if "6" in self.user_list:
                    if "9" in self.user_list:
                        self.user_won()
                        
                if "9" in self.user_list:
                    if "6" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "7" in self.user_list:
                        self.user_won()
                        
                if "7" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
            # ===== 4 =====
            if "4" in self.user_list:
                if "1" in self.user_list:
                    if "7" in self.user_list:
                        self.user_won()
                        
                if "7" in self.user_list:
                    if "1" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "6" in self.user_list:
                        self.user_won()
                        
                if "6" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
            # ===== 5 =====
            if "5" in self.user_list:
                if "7" in self.user_list:
                    if "3" in self.user_list:
                        self.user_won()
                        
                if "3" in self.user_list:
                    if "7" in self.user_list:
                        self.user_won()
                        
                if "2" in self.user_list:
                    if "8" in self.user_list:
                        self.user_won()
                         
                if "8" in self.user_list:
                    if "2" in self.user_list:
                        self.user_won()
                        
                if "1" in self.user_list:
                    if "9" in self.user_list:
                        self.user_won()
                        
                if "9" in self.user_list:
                    if "1" in self.user_list:
                        self.user_won()
                        
                if "4" in self.user_list:
                    if "6" in self.user_list:
                        self.user_won()
                        
                if "6" in self.user_list:
                    if "4" in self.user_list:
                        self.user_won()
                        
            # ===== 6 =====
            if "6" in self.user_list:
                if "3" in self.user_list:
                    if "9" in self.user_list:
                        self.user_won()
                        
                if "9" in self.user_list:
                    if "3" in self.user_list:
                        self.user_won()
                        
                if "4" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "4" in self.user_list:
                        self.user_won()
                        
            # ===== 7 =====
            if "7" in self.user_list:
                if "4" in self.user_list:
                    if "1" in self.user_list:
                        self.user_won()
                        
                if "1" in self.user_list:
                    if "4" in self.user_list:
                        self.user_won()
                        
                if "8" in self.user_list:
                    if "9" in self.user_list:
                        self.user_won()
                        
                if "9" in self.user_list:
                    if "8" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "3" in self.user_list:
                        self.user_won()
                        
                if "3" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
            # ===== 8 =====
            if "8" in self.user_list:
                if "9" in self.user_list:
                    if "7" in self.user_list:
                        self.user_won()
                        
                if "7" in self.user_list:
                    if "9" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "2" in self.user_list:
                        self.user_won()
                        
                if "2" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
            # ===== 9 =====
            if "9" in self.user_list:
                if "8" in self.user_list:
                    if "7" in self.user_list:
                        self.user_won()
                        
                if "7" in self.user_list:
                    if "8" in self.user_list:
                        self.user_won()
                        
                if "5" in self.user_list:
                    if "1" in self.user_list:
                        self.user_won()
                        
                if "1" in self.user_list:
                    if "5" in self.user_list:
                        self.user_won()
                        
                if "6" in self.user_list:
                    if "3" in self.user_list:
                        self.user_won()
                        
                if "3" in self.user_list:
                    if "6" in self.user_list:
                        self.user_won()

        else:
            self.result.config(text='Game Draw')
            self.result.config(fg='black')

root = Tk()
obj = Game(root)
root.mainloop()