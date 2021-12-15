import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x300")

principal_frame= tk.Frame(ventana)
principal_frame.config(bg='gray')
principal_frame.pack(expand=True, fill=tk.BOTH)

cuadro1 = tk.Frame(principal_frame)
cuadro1.config(bg='blue', bd=5, relief=tk.SUNKEN , width='100', height='60')
cuadro1.pack()

leon_image = tk.PhotoImage(file = r"leon.png")
image = leon_image.subsample(6,6)
label_image = tk.Label(cuadro1, image = image)
label_image.config(bg='blue', fg='black')
label_image.pack()

cuadro2 = tk.Frame(principal_frame)
cuadro2.pack()

mini_cuadro21 =tk.Frame(cuadro2)
mini_cuadro21.config(bg='lightblue', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro21.pack(side=tk.LEFT)


mini_cuadro22 =tk.Frame(cuadro2)
mini_cuadro22.config(bg='lightblue', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro22.pack(side=tk.LEFT)

cuadro3 = tk.Frame(principal_frame)
cuadro3.pack()

mini_cuadro31 =tk.Frame(cuadro3)
mini_cuadro31.config(bg='red', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro31.pack(side=tk.LEFT)

mini_cuadro32 =tk.Frame(cuadro3)
mini_cuadro32.config(bg='red', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro32.pack(side=tk.LEFT)

mini_cuadro33 =tk.Frame(cuadro3)
mini_cuadro33.config(bg='red', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro33.pack(side=tk.LEFT)

cuadro4 = tk.Frame(principal_frame)
cuadro4.pack()

mini_cuadro41 =tk.Frame(cuadro4)
mini_cuadro41.config(bg='green', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro41.pack(side=tk.LEFT)

mini_cuadro42 =tk.Frame(cuadro4)
mini_cuadro42.config(bg='green', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro42.pack(side=tk.LEFT)

mini_cuadro43 =tk.Frame(cuadro4)
mini_cuadro43.config(bg='green', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro43.pack(side=tk.LEFT)

mini_cuadro44 =tk.Frame(cuadro4)
mini_cuadro44.config(bg='green', bd=5, relief=tk.SUNKEN , width='100', height='60')
mini_cuadro44.pack(side=tk.LEFT)



ventana.mainloop()