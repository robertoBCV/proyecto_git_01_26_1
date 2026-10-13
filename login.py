from tkinter import ttk

class Login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ven = ventana
        self.ven.title("Login")
        self.ven.geometry("350x450+650+150")
        self.ven.iconbitmap("iconos/icono.ico")
        self.ven.resizable(False,False)
        self.ven.config(bg="#aaccff")
        self.ven.wm_attributes("-alpha",0.8)
        #self.ven.overrideredirect(True)

        