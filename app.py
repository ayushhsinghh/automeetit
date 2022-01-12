import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoMeetit")
        # self.geometry("500x500")
        
        UserInputFrame(self).pack()

class UserInputFrame(tk.Tk):
    def __init__(self , frame):
        super().__init__(frame)
        
        self.email = tk.StringVar()
        
        label = ttk.Label(self, text="Email")
        entry = ttk.Entry(self , textvariable=self.email)
        button = ttk.Button(self, text="Submit", command=self.submit)
        
        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")
        
        
        
    def submit(self):
        print(f"Submitted {self.email.get()}")
        
    
    
    

if __name__ == "__main__":
    app = App()
    app.mainloop()