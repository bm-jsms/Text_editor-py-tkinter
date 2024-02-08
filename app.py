import tkinter as tk
from tkinter import filedialog, messagebox


root = tk.Tk()


class simpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root, bg="black", fg="white")
        self.text_area.pack(expand=True, fill="both")

    def quit_confirm(self):
        if messagebox.askokcancel("Exit", "Do you want to quit?"):
            root.quit()


root.title("Code Editor")
root.geometry("800x600")


editor = simpleTextEditor(root)


bar_menu = tk.Menu(root)
menu_options = tk.Menu(bar_menu, tearoff=0)

root.config(bg="black")

menu_options.add_command(label="New")
menu_options.add_command(label="Open")
menu_options.add_command(label="Save")
menu_options.add_command(label="Exit", command=editor.quit_confirm)

root.config(menu=bar_menu)
bar_menu.add_cascade(label="File", menu=menu_options)

root.mainloop()
