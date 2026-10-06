import customtkinter as ctk
import os

class MainWindow(ctk.CTk): # creating a window.
    def __init__(self):
        super().__init__() # Open the window
        self.title("OctaGit") # Set title for window
        self.geometry("1024x768") # Set window-size

        icon_path = os.path.join( # gluing a path from parts
            os.path.dirname(__file__), # reuturns 'ui/'.
            "..", "..", "..", "assets", "icons", "octagit_icon.ico" # up three levels, and then down them, gluing them together.
        )
        self.iconbitmap(icon_path) # Set window icon.

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

# mainloop() is an infinite loop that keeps the window open.