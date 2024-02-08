import tkinter as tk
from tkinter import filedialog, messagebox


root = tk.Tk()


root.title("Code Editor")
root.geometry("800x600")


bar_menu = tk.Menu(root)
menu_options = tk.Menu(bar_menu, tearoff=0)

root.config(bg="black")

menu_options.add_command(label="New")
menu_options.add_command(label="Open")
menu_options.add_command(label="Save")
menu_options.add_command(label="Exit", command=root.quit)

root.config(menu=bar_menu)
bar_menu.add_cascade(label="File", menu=menu_options)

root.mainloop()
