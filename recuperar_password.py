import tkinter as tk

ventana = tk.Tk()
ventana.title("Recuperar contraseña")
ventana.geometry("350x200")

tk.Label(ventana, text="Recuperar contraseña").pack(pady=10)
tk.Entry(ventana).pack(pady=5)
tk.Button(ventana, text="Enviar recuperación").pack(pady=10)

ventana.mainloop()