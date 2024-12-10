import tkinter as tk

def enviar():
    mensaje = entry.get()
    print(f"Mensaje ingresado: {mensaje}")

root = tk.Tk()
root.title("Ejemplo Tkinter")

tk.Label(root, text="Hola Mundo").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Enviar", command=enviar).pack(pady=10)

root.mainloop()
