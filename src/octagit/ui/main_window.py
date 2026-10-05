import customtkinter as ctk

class MainWindow(ctk.CTk): # creating a window.
    def __init__(self):
        super().__init__() # Open the window
        self.title("OctaGit") # Set title for window
        self.geometry("1024x768") # Set window-size

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

# mainloop() is an infinite loop that keeps the window open.