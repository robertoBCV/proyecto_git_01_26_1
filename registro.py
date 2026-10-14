import tkinter as tk

ventana = tk.Tk()
ventana.title("Registro de usuario")
ventana.geometry("350x250")

tk.Label(ventana, text="Registro de usuarios").pack(pady=10)
tk.Entry(ventana).pack(pady=5)
tk.Entry(ventana, show="*").pack(pady=5)
tk.Button(ventana, text="Registrar").pack(pady=10)

ventana.mainloop()