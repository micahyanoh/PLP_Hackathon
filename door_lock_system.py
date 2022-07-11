import tkinter as tk
import customtkinter
import datetime

from sympy import expand


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


"""creating the application window """
class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #app properties
        self.title('Door Lock System Challenge')
        self.geometry(f"{800}x{500}")
        self.resizable(0, 0)

           
        self.commands=['OPEN','CLOSE','QUIT']
        self.log_time=[]
        self.pass_word=None

    #creating frame to hold widgets
          # creating frames
        self.frame1 = customtkinter.CTkFrame(master=self, width=200)
        self.frame1.configure()
        self.frame1.pack(side=customtkinter.LEFT, expand=0, fill=tk.Y)

        self.frame2 = customtkinter.CTkFrame(
            master=self, width=320, height=80, corner_radius=10
        )
        self.frame2.configure()
        self.frame2.pack(fill=customtkinter.BOTH, pady=20, padx=20)

        self.frame3 = customtkinter.CTkFrame(
            master=self, width=320, height=700, corner_radius=10
        )
        self.frame3.pack(fill=customtkinter.BOTH, padx=20)
         # command bar
        self.command_b = customtkinter.CTkButton(
            master=self.frame2, width=2, text="EXECUTE", corner_radius=20,
        )
        self.command_b.pack(side=tk.RIGHT, pady=15, padx=10)
        self.command_e = customtkinter.CTkEntry(
            master=self.frame2,
            width=200,
            placeholder_text="Input COMMAND",
            corner_radius=30,
        )
        self.command_e.pack(side=tk.RIGHT, pady=15, padx=10)
        #frame 1 buttons
        self.fee = customtkinter.CTkButton(master=self.frame1, text="BED-ROOM")
        self.fee.pack(pady=20, padx=20)
        self.exams = customtkinter.CTkButton(master=self.frame1, text="SITTING-ROOM")
        self.exams.pack(pady=20, padx=20)
        self.lib = customtkinter.CTkButton(master=self.frame1, text="BATH-ROOM")
        self.lib.pack(pady=20, padx=20)
        self.staff = customtkinter.CTkButton(master=self.frame1, text="DINING")
        self.staff.pack(pady=20, padx=20)
    

    
    """setting password"""
    def pass_set(self):
        self.frame11=customtkinter.CTkFrame(master=self.frame3)
        self.frame11.pack(expand=1,fill=tk.BOTH,padx=20,pady=20)
        self.enter_pass = customtkinter.CTkEntry(
            master=self.frame11,
            width=200,
            placeholder_text="ENTER PASSWORD",
            corner_radius=30,
            show="**"
        )
        self.enter_pass.pack(pady=15, padx=10)
        self.confirm_pass = customtkinter.CTkEntry(
            master=self.frame11,
            width=200,
            placeholder_text="CONFIRM PASSWORD",
            corner_radius=30,
            show='**'
        )
        self.confirm_pass.pack(pady=15, padx=10)
        self.set_b = customtkinter.CTkButton(
            master=self.frame11, width=2, text="SET", corner_radius=20,command=self.set_pass
        )
        self.set_b.pack(pady=15, padx=10)
    def set_pass(self):
        self.lab=customtkinter.CTkLabel(master=self.frame11)
        self.lab.pack()
        if self.enter_pass.get()==self.confirm_pass.get():
            self.pass_word=self.enter_pass.get()
            self.lab.configure(text='  SUCCESS!\n OPEN THE DOOR NOW!')
            self.after(2_000,self.frame11.destroy)
            self.after(2_001,self.unlock)
        else:
            self.lab.configure(text='  Passwords DO NOT Match!\n  Try again!')
            



    """creating actions function"""
    def actions(self):
        self.command_me=self.command_e.get()
        self.command_me=self.command_me.upper()
        if self.command_me==self.commands[0]:
            self.lab14.configure(text=f'The door is now open{self.now}')
            self.lab14.configure(text=f'The door is already open,{self.now}')

        elif self.command_me==self.commands[1]:
             self.lab14.configure(text=f'The door is already open{self.now}')
        elif self.command_me==self.commands[2]:
            self.after(1_000,self.destroy)
            self.lab14.configure(text='process has been terminated')
            print(f'The door is now locked{self.now}')
        else:
            self.lab14.configure(text='Invalid Input')
            print('Invalid Input')
        


    """creating a lock function"""
    def lock(self):
        pass


    """creating unlock function"""
    def unlock(self):
        self.now=datetime.datetime.now()
        self.log_time.append(self.now)
        self.frame12=customtkinter.CTkFrame(master=self.frame3,height=200,width=200)
        self.frame12.pack(expand=1,fill=tk.BOTH,padx=20,pady=20)
        self.enter_pas = customtkinter.CTkEntry(
            master=self.frame12,
            width=200,
            placeholder_text="ENTER PASSWORD",
            corner_radius=30,
            show='**'
        )
        self.enter_pas.pack(pady=15, padx=10)
        self.log_b = customtkinter.CTkButton(
            master=self.frame12, width=2, text="OPEN", corner_radius=20,command=self.verify_pass
        )
        self.log_b.pack(pady=15, padx=10)

    def verify_pass(self):
        if self.enter_pas.get()==str(self.pass_word):
                self.open_now()
                self.lab14=customtkinter.CTkLabel(master=self.frame3,text=f'The door is now open\n{self.now}')
                self.lab14.pack()
        else:
            self.lab13=customtkinter.CTkLabel(master=self.frame12,text='  Wrong Password!\nPlease Try Again')
            self.lab13.pack()
            
    def open_now(self):
        self.frame12.destroy()
        self.command_b.configure(command=self.actions)
        self.frame13=customtkinter.CTkFrame(master=self.frame3)
        self.frame13.pack(expand=1,fill=tk.BOTH,padx=20,pady=20)
        self.lab13=customtkinter.CTkLabel(master=self.frame13)
        self.lab13.pack()
        self.lab13.configure(text='  WELCOME HOME\n ALL ROOMS ARE OPEN NOW!\n FEEL FREE TO EXPLORE',
                            font=('ariel',20,'bold'))




""" Initialize the application to start"""
if __name__ == '__main__':
    app=Window()
    app.pass_set()
    app.mainloop()