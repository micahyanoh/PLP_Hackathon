import tkinter as tk
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


"""creating the application window """
class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #app properties
        self.title('Calories Calculator Challenge')
        self.geometry(f"{600}x{500}")
        self.resizable(0, 0)

        #keyboard shortcuts
        self.bind('<Q>',exit)
        self.bind('<q>',exit)

    #creating frame to hold widgets
        self.frame=customtkinter.CTkFrame(master=self,corner_radius=20)
        self.frame.pack(expand=1,fill=tk.BOTH,pady=20,padx=20)

    #creating instruction labels
        self.label=customtkinter.CTkLabel(master=self.frame,text=self)
        self.label.configure(   text='**PLEASE FILL IN THE ENTRY**\n(TO CALCULATE YOUR CALORIES)',
                                font=('ariel',15,'bold'),foreground='white'   )
        self.label.pack(pady=20)

    #creating entries
        self.fat_entry=customtkinter.CTkEntry(    master=self.frame,
                                                    width=200,
                                                    placeholder_text='FAT(Grams Per Day)',
                                                    corner_radius=20    )
        self.fat_entry.pack(pady=20)
        self.cab_entry=customtkinter.CTkEntry(    master=self.frame,
                                                        width=200,
                                                        placeholder_text='CARBOHYDRATES  (G/Day)',
                                                        corner_radius=20    )
        self.cab_entry.pack(pady=20)

    #creating button
        self.button=customtkinter.CTkButton(    master=self.frame,text='GENERATE RESULTS',corner_radius=15,
                                                 command=self.disp )
        self.button.pack(pady=20)
    """calculating costs"""
    def calculate(self):
        #defining constants
        self.labour_price=20.00
        self.fat_cal=int(self.fat_entry.get())
        self.cab_cal=int(self.cab_entry.get())
        #generated values
        self.total_fat_cal=self.fat_cal*9
        self.total_cab_cal=self.cab_cal*4
        self.total_cal=self.total_cab_cal+self.total_fat_cal
        
        #creating a list to store output
        self.output=[
                        f'TOTAL FAT CALORIES:      {self.total_fat_cal} Calories',
                        f'TOTAL CARBOHYDRATES CALORIES:     {self.total_cab_cal} Calories',
                        f'TOTAL CALORIES CONSUMED:    {self.total_cal} Calories',
                         ]

    """creating pop up window for displaying results"""
    def disp(self):
        self.calculate()
        #destroying initial frame
        self.frame.destroy()
        #creating new frame
        self.frame1=customtkinter.CTkFrame(master=self,corner_radius=20,width=300,height=200)
        self.frame1.pack(fill=tk.Y,expand=1,pady=30,padx=30)
        #creating receipt labels
        self.label1=customtkinter.CTkLabel(master=self.frame1,text=self.output[0])
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        self.label1=customtkinter.CTkLabel(master=self.frame1,text=self.output[1])
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        self.label1=customtkinter.CTkLabel(master=self.frame1,text=self.output[2])
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        
        #creating exit button
        self.exit=customtkinter.CTkButton(master=self,text='EXIT',command=self.destroy)
        self.exit.pack(pady=30)
                

    



""" Initialize the application to start"""
if __name__ == '__main__':
    app=Window()
    app.mainloop()
