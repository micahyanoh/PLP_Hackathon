import tkinter as tk
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


"""creating the application window """
class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #app properties
        self.title('Career Choice Challenge')
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
        self.label1=customtkinter.CTkLabel(master=self.frame,text=self)
        self.label.configure(   text='**PLEASE FILL IN THE ENTRY**\n(TO IDENTIFY YOUR CAREER)',
                                font=('ariel',15,'bold'),foreground='white'   )
        self.label.pack(pady=20)
        self.label1.configure(text='SELECT ONE:\nCOOKING,WRITING,PAINTING,CODING,RUNNING')
        self.label1.pack(pady=20)
    #creating entries
        self.hobby_entry=customtkinter.CTkEntry(    master=self.frame,
                                                    width=300,
                                                    placeholder_text='  TALENT/HOBBY      ( e.g cooking  )',
                                                    corner_radius=20    )
        self.hobby_entry.pack(pady=20)
    #creating button
        self.button=customtkinter.CTkButton(    master=self.frame,text='CALCULATE POINTS',corner_radius=15,
                                                 command=self.disp )
        self.button.pack(pady=20)
    """calculating costs"""
    def decision(self):
        #defining constants
        self.choices=['CHEF','JOURNALIST','GRAPIC DESIGNER','SOFTWARE ENGINEER','ATHLETE']#career options
        self.advice=[   'Enroll for a Food Science course',
                        'Consider any multimedia programme',
                        'Learn more about Photoshop,Illustrator \nand Indesign',
                        'Enroll for a Certification course\n and join a community',
                        'Practice,practice\n and practice'    ]#advices
        self.questions=['COOKING','WRITING','PAINTING','CODING','RUNNING']#questions
        self.hobby=self.hobby_entry.get()
        self.hobby=self.hobby.upper()
    
        #loop to decide on choice
        if self.hobby==self.questions[0]:
            self.career=self.choices[0]
            self.my_advice=self.advice[0]
        elif self.hobby==self.questions[1]:
            self.career=self.choices[1]
            self.my_advice=self.advice[1]
        elif self.hobby==self.questions[2]:
            self.career=self.choices[2]
            self.my_advice=self.advice[2]
        elif self.hobby==self.questions[3]:
            self.career=self.choices[3]
            self.my_advice=self.advice[3]
        elif self.hobby==self.questions[4]:
            self.career=self.choices[4]
            self.my_advice=self.advice[4]
        else:
            self.career='We can not place you at the moment'
            self.my_advice='PLEASE ENTER A VALID HOBBY!'
    
    """creating pop up window for displaying results"""
    def disp(self):
        self.decision()
        #destroying initial frame
        self.frame.destroy()
        #creating new frame
        self.frame1=customtkinter.CTkFrame(master=self,corner_radius=20,width=300,height=200)
        self.frame1.pack(fill=tk.Y,expand=1,pady=30,padx=30)
        #creating output labels
        self.label1=customtkinter.CTkLabel(master=self.frame1,text='CONSIDER THIS PROFESSION: ')
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        self.label1=customtkinter.CTkLabel(master=self.frame1,text=f'Your hobby/talent is {self.hobby}')
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        self.label1=customtkinter.CTkLabel(master=self.frame1,text=f'Career: {self.career}')
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        self.label1=customtkinter.CTkLabel(master=self.frame1,text=f'You should: {self.my_advice}')
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        self.label1=customtkinter.CTkLabel(master=self.frame1,text='This window terminates in 5 seconds')
        self.label1.pack(pady=20,padx=50,side=tk.TOP)
        self.after(5_000,self.destroy)
        #creating exit button
        self.exit=customtkinter.CTkButton(master=self,text='EXIT',command=self.destroy)
        self.exit.pack(pady=30)
        

""" Initialize the application to start"""
if __name__ == '__main__':
    app=Window()
    app.mainloop()