import tkinter
from tkinter import ttk
import time


root = tkinter.Tk()
root.config(background="#E8E8E8")
root.title("My Tkinter")





# ☰ | 14. Menubar
# def menubar_open():
    # print("File has been opened")
    # root.quit()

# def menubar_save():
    # print("File has been saved")
    # root.quit()

# def menubar_undo():
    # print("Undo Changes")

# def menubar_redo():
    # print("Redo Changes")

# def menubar_cut():
    # print("Cut the text")

# def menubar_copy():
    # print("Copy the text")

# def menubar_paste():
    # print("Paste the text")

# menubar_photo_open = tkinter.PhotoImage(file="Python Project/Icon_Open.png")
# menubar_photo_save = tkinter.PhotoImage(file="Python Project/Icon_Save.png")
# menubar_photo_exit = tkinter.PhotoImage(file="Python Project/Icon_Exit.png")

# menubar = tkinter.Menu(root)
# root.config(menu=menubar)

# menubar_filemenu = tkinter.Menu(menubar, tearoff=False, font=("Times New Roman", 12))
# menubar.add_cascade(label="File", menu=menubar_filemenu)
# menubar_filemenu.add_command(label=" Open", command=menubar_open, image=menubar_photo_open, compound="left")
# menubar_filemenu.add_command(label=" Save", command=menubar_save, image=menubar_photo_save, compound="left")
# menubar_filemenu.add_separator() # Add Separator
# menubar_filemenu.add_command(label=" Exit", command=root.destroy, image=menubar_photo_exit, compound="left")

# menubar_editmenu = tkinter.Menu(menubar, tearoff=False, font=("Times New Roman", 12))
# menubar.add_cascade(label="Edit", menu=menubar_editmenu)
# menubar_editmenu.add_command(label="Undo", command=menubar_undo)
# menubar_editmenu.add_command(label="Redo", command=menubar_redo)
# menubar_editmenu.add_separator()
# menubar_editmenu.add_command(label="Cut", command=menubar_cut)
# menubar_editmenu.add_command(label="Copy", command=menubar_copy)
# menubar_editmenu.add_command(label="Paste", command=menubar_paste)





# 🖼️ | 15. Frames
# frame = tkinter.Frame(root, background="#E8E8E8", border=5, relief="sunken")
# frame.pack()
# # frame.pack(side="bottom")
# # frame.place(x=0, y=0)

# tkinter.Button(frame, text="W", font=("Consolas", 25), width=3).pack(side="top")
# tkinter.Button(frame, text="A", font=("Consolas", 25), width=3).pack(side="left")
# tkinter.Button(frame, text="S", font=("Consolas", 25), width=3).pack(side="left")
# tkinter.Button(frame, text="D", font=("Consolas", 25), width=3).pack(side="left")





# 🪟 | 16. Open New Window
# def create_window():
    # # new_window = tkinter.Tk() # Individual window
    # new_window = tkinter.Toplevel() # Linked to the base window
    # new_window.title("Another Window")
    # new_window.geometry("300x200")

    # def do_something():
        # new_window_button.config(text="Clicked")

    # new_window_button = tkinter.Button(new_window, text="Ambassador", command=do_something)
    # new_window_button.pack()

# tkinter.Button(root, text="Create New Window", command=create_window).pack()





# 🗂️ | 17. Window Tabs
# notebook = ttk.Notebook(root) # Widget that manages a collection of windows / displays.

# notebook_tab1 = tkinter.Frame(notebook) # New frame for tab 1
# notebook_tab2 = tkinter.Frame(notebook) # New frame for tab 2

# notebook.add(notebook_tab1, text="Tab 1")
# notebook.add(notebook_tab2, text="Tab 2")
# notebook.pack(expand=True, fill="both") # Expand to fill any space not otherwise used. - # fill = Fill space on X and Y axis.

# tkinter.Label(notebook_tab1, text="Tab number 1 served", width=50, height=25).pack()
# tkinter.Label(notebook_tab2, text="Tab number 2 restored", width=50, height=25).pack()





# ᚙ | 18. Grid Geometry Manager
# titlelabel = tkinter.Label(root, text="Enter Your Information", font=("Times New Roman", 12)).grid(row=0, column=0, columnspan=2)

# firstnamelabel = tkinter.Label(root, text="First Name: ").grid(row=1, column=0)
# firstnameentry = tkinter.Entry(root).grid(row=1,column=1)

# Lastnamelabel = tkinter.Label(root, text="Last Name: ").grid(row=2, column=0)
# Lastnameentry = tkinter.Entry(root).grid(row=2,column=1)

# Emailnamelabel = tkinter.Label(root, text="Email: ").grid(row=3, column=0)
# Emailnameentry = tkinter.Entry(root).grid(row=3,column=1)

# submitbutton = tkinter.Button(root, text="Submit").grid(row=4, column=0, columnspan=2)





# 🚀 | 19. Progress Bar
# def pb_start():
    # pb_gb = 100
    # pb_download = 0
    # pb_speed = 1

#     while pb_download < pb_gb:
        # time.sleep(0.05)

        # pb_bar["value"] += (pb_speed / pb_gb) * 100
        # pb_download += pb_speed

        # pb_percent.set(str(int((pb_download / pb_gb) * 100)) + "%")
        # pb_text.set(str(pb_download) + " / " + str(pb_gb) + " GB Completed")

        # root.update_idletasks()

# pb_percent = tkinter.StringVar()
# pb_text = tkinter.StringVar()

# pb_bar = ttk.Progressbar(root, orient="horizontal", length=300)
# pb_bar.pack(pady=10)

# pb_percentlabel = tkinter.Label(root, textvariable=pb_percent).pack()
# pb_gblabel = tkinter.Label(root, textvariable=pb_text).pack()

# pb_button = tkinter.Button(root, text="Download", command=pb_start).pack()





# 🎨 | 20. Canvas
# canvas = tkinter.Canvas(root, height=500, width=500)

# canvas.create_line(0, 0, 500, 500, fill="#2C3930", width=5)
# canvas.create_line(0, 500, 500, 0, fill="#3F4F44", width=5)
# canvas.create_rectangle(50, 50, 450, 450, fill="#A27B5C", width=5)
# canvas_points = [250, 0, 500, 500, 0, 500]
# canvas.create_polygon(canvas_points, fill="#B3C8CF", outline="#E5DDC5", width=5)
# # canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="#B3C8CF", outline="#E5DDC5", width=5)
# canvas.create_arc(0, 0, 500, 500, style="pieslice", start=270, extent=180)
# canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=10)
# canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, start=180, width=10)
# canvas.create_oval(190, 190, 310, 310, fill="white", width=10)

# canvas.pack()





# 🔑 | 21. Key Events
# def dosomething(event):
    # # print(f"You press {event.keysym}")
    # key_label.config(text=event.keysym)

# root.bind("<Key>", dosomething)

# key_label = tkinter.Label(root, font=("Helvetica", 100))
# key_label.pack()





# 🖱️ | 22. Mouse Events
# def dosomething(event):
    # print(f"Coordinate: {event.x}, {event.y}")

# root.bind("<Button-1>", dosomething) # Left mouse click
# root.bind("<Button-2>", dosomething) # Middle mouse click
# root.bind("<Button-3>", dosomething) # Right mouse click
# root.bind("<ButtonRelease>", dosomething) # Release the mouse
# root.bind("<Enter>", dosomething) # Enter the window
# root.bind("<Leave>", dosomething) # Leave the window
# root.bind("<Motion>", dosomething) # Where the mouse moved





# 🧲 | 23. Drag & Drop
# def drag_start(event):
    # widget = event.widget # Get the widget that triggered the event

    # widget.startX = event.x # Store the starting X coordinate (relative to the widget)
    # widget.startY = event.y # Store the starting Y coordinate (relative to the widget)

# def drag_motion(event):
    # widget = event.widget # Get the widget that triggered the event

    # dd_x = widget.winfo_x() - widget.startX + event.x # Calculate new X position
    # dd_y = widget.winfo_y() - widget.startY + event.y # Calculate new Y position
    # widget.place(x=dd_x, y=dd_y) # Move the widget to the new position

# dd_label = tkinter.Label(root, background="#222831", width=10, height=5)
# dd_label.place(x=0, y=0)

# dd_label2 = tkinter.Label(root, background="#393E46", width=10, height=5)
# dd_label2.place(x=100, y=100)

# dd_label.bind("<Button-1>", drag_start)
# dd_label.bind("<B1-Motion>", drag_motion)

# dd_label2.bind("<Button-1>", drag_start)
# dd_label2.bind("<B1-Motion>", drag_motion)





# 🏞️ | 24.A. Move Image
# root.geometry("500x500")

# def move_up(event):
    # mi_Label.place(x = mi_Label.winfo_x(), y = mi_Label.winfo_y() - 10)

# def move_down(event):
    # mi_Label.place(x = mi_Label.winfo_x(), y = mi_Label.winfo_y() + 10)

# def move_left(event):
    # mi_Label.place(x = mi_Label.winfo_x() - 10, y = mi_Label.winfo_y())

# def move_right(event):
    # mi_Label.place(x = mi_Label.winfo_x() + 10, y = mi_Label.winfo_y())

# root.bind("<w>", move_up)
# root.bind("<s>", move_down)
# root.bind("<a>", move_left)
# root.bind("<d>", move_right)

# root.bind("<Up>", move_up)
# root.bind("<Down>", move_down)
# root.bind("<Left>", move_left)
# root.bind("<Right>", move_right)

# mi_MyImage = tkinter.PhotoImage(file = "Python Project/Image_Sport-Car.png")
# mi_Label = ttk.Label(master = root, image = mi_MyImage, background = "#E8E8E8")
# mi_Label.place(x=0, y=0)





# 🏞️ | 24.B. Move Image on Canvas
# def move_up(event):
    # mi_canvas.move(mi_MyImage2, 0, -10)

# def move_down(event):
    # mi_canvas.move(mi_MyImage2, 0, 10)

# def move_left(event):
    # mi_canvas.move(mi_MyImage2, -10, 0)

# def move_right(event):
    # mi_canvas.move(mi_MyImage2, 10, 0)

# root.bind("<w>", move_up)
# root.bind("<s>", move_down)
# root.bind("<a>", move_left)
# root.bind("<d>", move_right)

# root.bind("<Up>", move_up)
# root.bind("<Down>", move_down)
# root.bind("<Left>", move_left)
# root.bind("<Right>", move_right)

# mi_canvas = tkinter.Canvas(master = root, width = 500, height = 500)
# mi_canvas.pack()

# mi_PhotoImage = tkinter.PhotoImage(file = "Python Project/Image_Sport-Car.png")
# mi_MyImage2 = mi_canvas.create_image(0, 0, image = mi_PhotoImage, anchor = "nw")





# 🎬 | 25. Animation
# a_Width = 500
# a_Height = 500

# xVelocity = 3
# yVelocity = 2

# a_Canvas = tkinter.Canvas(master = root, width = a_Width, height = a_Height)
# a_Canvas.pack()

# a_BackgroundPhoto = tkinter.PhotoImage(file = "Python Project/Image_Sky.png")
# a_a_Background = a_Canvas.create_image(0, 0, image = a_BackgroundPhoto, anchor = "nw")

# a_PhotoImage = tkinter.PhotoImage(file = "Python Project/Image_Airplane.png")
# a_MyImage = a_Canvas.create_image(0, 0, image = a_PhotoImage, anchor = "nw")

# a_ImageWidth = a_PhotoImage.width()
# a_ImageHeight = a_PhotoImage.height()

# while True:
    # a_coordinate = a_Canvas.coords(a_MyImage)
    # print(a_coordinate)

    # if a_coordinate[0] >= a_Width - a_ImageWidth or a_coordinate[0] < 0:
        # xVelocity = -xVelocity

    # if a_coordinate[1] >= a_Height - a_ImageHeight or a_coordinate[1] < 0:
        # yVelocity = -yVelocity


    # a_Canvas.move(a_MyImage, xVelocity, yVelocity)
    # root.update()
    # time.sleep(0.01)





root_icon = tkinter.PhotoImage(file="Python Project/Icon_Python.png")
root.iconphoto(True, root_icon)
root.mainloop()
