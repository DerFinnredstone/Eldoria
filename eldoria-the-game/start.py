import tkinter as tk
from lib import start_command

def start_mode():
    start_command()

def open_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Spielmodus auswählen")

    button_mode1 = tk.Button(menu_window, text="Survival", command=start_mode)
    button_mode1.pack()

    button_mode2 = tk.Button(menu_window, text="Hardcore", command=start_mode)
    button_mode2.pack()

    button_mode3 = tk.Button(menu_window, text="Sandbox", command=start_mode)
    button_mode3.pack()

root = tk.Tk()

# Erstellen einer Schaltfläche für das Menü
button_menu = tk.Button(root, text="Menü", command=open_menu)
button_menu.pack()

root.mainloop()
