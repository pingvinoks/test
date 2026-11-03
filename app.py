import random
import tkinter as tk
from tkinter import messagebox


def on_yes():
  messagebox.showinfo(
      "Результат", "Мы так и знали"
  )
  root.destroy()


def move_no_button(event):

  new_x = random.randint(30, 320)
  new_y = random.randint(100, 240)
  btn_no.place(x=new_x, y=new_y)


root = tk.Tk()
root.title("Важный опрос")
root.geometry("400x300")
root.resizable(False, False)


label = tk.Label(root, text="Ты гей?", font=("Arial", 22, "bold"))
label.pack(pady=40)


btn_yes = tk.Button(
    root,
    text="Да",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    width=8,
    command=on_yes,
)
btn_yes.place(x=80, y=180)


btn_no = tk.Button(
    root, text="Нет", font=("Arial", 14, "bold"), bg="#f44336", fg="white", width=8
)
btn_no.place(x=220, y=180)


btn_no.bind("<Enter>", move_no_button)


root.mainloop()