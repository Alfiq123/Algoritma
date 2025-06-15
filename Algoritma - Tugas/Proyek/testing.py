import tkinter as tk
from tkinter import ttk

def increase(index):
    current = int(tree.set(index, "Quantity"))
    tree.set(index, "Quantity", str(current + 1))

def decrease(index):
    current = int(tree.set(index, "Quantity"))
    if current > 0:
        tree.set(index, "Quantity", str(current - 1))

root = tk.Tk()
tree = ttk.Treeview(root, columns=("Item", "Quantity", "Control"), show="headings")
tree.heading("Item", text="Item")
tree.heading("Quantity", text="Quantity")
tree.heading("Control", text="Control")

data = [("Apple", 1), ("Banana", 3)]

for item, qty in data:
    index = tree.insert("", "end", values=(item, qty, ""))
    btn_frame = tk.Frame(root)
    tk.Button(btn_frame, text="+", command=lambda i=index: increase(i)).pack(side="left")
    tk.Button(btn_frame, text="-", command=lambda i=index: decrease(i)).pack(side="left")
    tree.item(index, tags=(index,))

tree.pack()

root.mainloop()
