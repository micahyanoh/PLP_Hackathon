import tkinter as tk
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


"""creating the application window """
class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #app properties
        self.title('Personality Test Challenge')
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
        self.label.configure(   text='**PLEASE FILL IN THE ENTRY**\n(TO CALCULATE YOUR POINTS)',
                                font=('ariel',15,'bold'),foreground='white'   )
        self.label.pack(pady=20)
    #creating entries
        self.books_entry=customtkinter.CTkEntry(    master=self.frame,
                                                    width=300,
                                                    placeholder_text='N.O BOOKS PUARCHASED (This Month)',
                                                    corner_radius=20    )
        self.books_entry.pack(pady=20)
    #creating button
        self.button=customtkinter.CTkButton(    master=self.frame,text='CALCULATE POINTS',corner_radius=15,
                                                 command=self.disp   )
        self.button.pack(pady=20)


    """calculating costs"""
    def calculate(self):
        #defining constants
        self.books_purchased=int(self.books_entry.get())
        #loop to decide on lost
        if self.books_purchased==0:
            self.points=0
        elif self.books_purchased==1:
            self.points=6
        elif self.books_purchased==2:
            self.points=16
        elif self.books_purchased==3:
            self.points=32
        elif self.books_purchased>=4:
            self.points=60


    """creating pop up window for displaying results"""
    def disp(self):
        self.calculate()
        self.text=f'YOU HAVE EARNED\n\n\n{self.points}\n\nPOINTS'
        #destroying initial frame
        self.frame.destroy()
        #creating new frame
        self.frame1=customtkinter.CTkFrame(master=self,corner_radius=20,width=300,height=200)
        self.frame1.pack(fill=tk.Y,expand=1,pady=30,padx=30)
        #creating display labels
        self.label1=customtkinter.CTkLabel(master=self.frame1,text=self.text)
        self.label1.pack(pady=30,padx=30)
        #creating exit button
        self.exit=customtkinter.CTkButton(master=self,text='EXIT',command=self.destroy)
        self.exit.pack(pady=30)



""" Initialize the application to start"""
if __name__ == '__main__':
    app=Window()
    app.mainloop()