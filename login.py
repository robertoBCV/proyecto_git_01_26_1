from tkinter import ttk
import tkinter as tk

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
        self.ven.overrideredirect(True)

        def Salir():
            self.ven.destroy()

        self.boton_salir = tk.Button(self.ven, text="X", 
                                     command=Salir, width="6", height="3")
        self.boton_salir.place(x=290,y=10)
        self.boton_salir.config(bg="#ee99aa")

        #variables
        self.user = tk.StringVar()
        self.clave = tk.StringVar()

        #Imagnes
        self.logo = tk.PhotoImage(file="imagenes/logo1.png")

        #Etiquetas
        self.lblimgLogo = tk.Label(self.ven, image=self.logo)
        self.lblimgLogo.place(x=100,y=50)
        self.lblimgLogo.config(bg="#aaccff")

        self.lblLogo = tk.Label(self.ven, text="Acceso",font=("Arial",18))
        self.lblLogo.place(x=140,y=200)
        self.lblLogo.config(bg="#aaccff")

        