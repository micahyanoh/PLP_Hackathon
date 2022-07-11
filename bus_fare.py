import tkinter as tk
import customtkinter
import datetime


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


"""creating the application window """
class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #app properties
        self.title('Bus Fare Challenge')
        self.geometry(f"{500}x{300}")
        self.resizable(0, 0)
        
        #keyboard shortcuts
        self.bind('<Q>',exit)
        self.bind('<q>',exit)

        #creating frame to hold widgets
        self.frame=customtkinter.CTkFrame(master=self,corner_radius=20)
        self.frame.pack(expand=1,fill=tk.BOTH,pady=30,padx=30)

        #creating labels for display text
        self.date_label=customtkinter.CTkLabel(master=self.frame,text='Press button')
        self.date_label.pack(pady=10)
        self.day_label=customtkinter.CTkLabel(master=self.frame,text='To Display')
        self.day_label.pack(pady=10)
        self.fare_label=customtkinter.CTkLabel(master=self.frame,text='Q to exit')
        self.fare_label.pack(pady=10)
        #creating 'GENERATE FARE' button

        self.button=customtkinter.CTkButton(    master=self.frame,text='GENERATE FARE',
                                                command=self.disp,fg_color='#3d6466'    )
        self.button.pack(side=tk.BOTTOM,pady=20)


    """generating system date,day and storing them in variables"""
    def today_fare(self):
        #default fare
        self.fare=100 
        #date
        self.today=datetime.date.today() 
        #day
        self.day=self.today.strftime('%a')

        #a loop to decide on fare to charge
        if self.day=='Sat':
            self.fare=60
        elif self.day=='Sun':
            self.fare=80
        else:
            self.fare=self.fare


    """creating button command"""
    def disp(self):
        self.today_fare()
        self.date_label.configure(  text=f'Date:{self.today}',
                                    font=('ariel',20,'bold'),foreground='red'   )
        self.day_label.configure(   text=f'Day:{self.day}              ',
                                    font=('ariel',20,'bold'),foreground='red'   )
        self.fare_label.configure(  text=f'Fare:{self.fare}            ',
                                    font=('ariel',20,'bold'),foreground='red'   )
       
        
 
""" Initialize the application to start"""
if __name__ == '__main__':
    app=Window()
    app.mainloop()