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
        #self.ven.overrideredirect(True)

        """def Salir():
            self.ven.destroy()

        self.boton_salir = tk.Button(self.ven, text="X", 
                                     command=Salir, width="6", height="3")
        self.boton_salir.place(x=290,y=10)
        self.boton_salir.config(bg="#ee99aa")
        """

        #variables
        self.user = tk.StringVar()
        self.clave = tk.StringVar()

        #Imagnes
        self.logo = tk.PhotoImage(file="imagenes/logo1.png")

        #Etiquetas
        self.lblimgLogo = tk.Label(self.ven, image=self.logo)
        self.lblimgLogo.place(x=100,y=50)
        self.lblimgLogo.config(bg="#aaccff")

        self.lblUser = tk.Label(self.ven, text="ACCESO",font=("Arial",16))
        self.lblUser.place(x=130,y=170)
        self.lblUser.config(bg="#aaccff")

        #Usuario, label y caja
        self.lblUser = tk.Label(self.ven, text="Usuario",font=("Arial",16))
        self.lblUser.place(x=30,y=220)
        self.lblUser.config(bg="#aaccff")

        self.txtLogo = tk.Entry(self.ven, textvariable=self.user, font=("Arial",18),
                                width="22")
        self.txtLogo.place(x=30,y=260)
        self.txtLogo.config(bg="#ffeeff")

        self.lblPass = tk.Label(self.ven, text="Constraseña",font=("Arial",16))
        self.lblPass.place(x=30,y=300)
        self.lblPass.config(bg="#aaccff")

        self.txtPass = tk.Entry(self.ven, textvariable=self.clave, font=("Arial",18),
                                width="22")
        self.txtPass.place(x=30,y=330)
        self.txtPass.config(bg="#ffeeff")

        self.btnIngresar = tk.Button(self.ven, text="Ingresar",width="23",height="2")
        self.btnIngresar.place(x=33,y=370)
        self.btnIngresar.config(bg="#ee99aa",font=("Arial",16))
        