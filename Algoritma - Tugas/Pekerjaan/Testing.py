import tkinter as tk

root = tk.Tk()
root.title("LabelFrame Text Centering")

labelframe = tk.LabelFrame(root, text="My Centered Label")
labelframe.pack(padx=20, pady=20)

#Method 1 using anchor.
labelframe.config(labelanchor="n") #this positions the entire label at the top of the frame.
labelframe.config(text="Centered Text")

#Method 2 using justify.
labelframe2 = tk.LabelFrame(root, text="Multi-line centering")
labelframe2.pack(padx=20, pady=20)
labelframe2.config(text="Multi line\nCentered Text")
labelframe2.config(justify=tk.CENTER)

root.mainloop()