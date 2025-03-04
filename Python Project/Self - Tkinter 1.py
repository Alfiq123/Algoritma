import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import tkinter.messagebox

# count = 0
# def show_text():
    # global count
    # count += 1
    # print(f"Red Alert {count}")

window = tkinter.Tk()



# 🪟 | 1. Window
window.config(background="#E8E8E8") # #191919
window.title("My Tkinter")
# window.geometry("256x256")



# 🏷️ | 2. Label
# photo = tkinter.PhotoImage(file="Image_DarkComputer.png")
# label = tkinter.Label(window, text="Welcome To Atlas", font=("Times New Roman", 40, "bold"), foreground="#F5F5F5", background="#000000", relief="raised", borderwidth=10, padx=20, pady=20, image=photo,compound="bottom")
# label.pack()
# label.place(x=128, y=128)



# 🕹️ | 3. Button
# photo = tkinter.PhotoImage(file="Image_DarkComputer.png")
# button = tkinter.Button(window, text="Send", command=submit, font=("Times New Roman", 30, "bold"), background="#191919", foreground="#E8E8E8", activeforeground="#E8E8E8", activebackground="#191919", state="disable")
# button.pack()



# 🚪 | 4. Entry
# def submit():
    # name = entry.get()
    # print(f"Whatsupp {name}")
    # entry.config(state="disabled", disabledbackground="#191919")

# def delete():
    # entry.delete(0, tkinter.END)

# def backspace():
    # entry.delete(len(entry.get())-1, tkinter.END)

# entry = tkinter.Entry(window,font=("Times New Roman", 32), background="#191919", foreground="#E8E8E8", show="*")
# entry.insert(0, "Arsenal")
# entry.pack(side="left")

# entry_button_submit = tkinter.Button(window, text="Submit", command=submit, background="#191919", foreground="#E8E8E8")
# entry_button_submit.pack(side="right")

# entry_button_delete = tkinter.Button(window, text="Delete", command=delete,background="#191919", foreground="#E8E8E8")
# entry_button_delete.pack(side="right")

# entry_button_backspace = tkinter.Button(window, text="Backspace", command=backspace, background="#191919", foreground="#E8E8E8")
# entry_button_backspace.pack(side="right")



# ✅ | 5. Checkbutton
# def display():
    # if (check.get()):
        # print("Very clever")
    # else:
        # print("Good choice")

# check = tkinter.BooleanVar()
# # check = tkinter.IntVar()
# # check = tkinter.StringVar()

# checkbutton_photo = tkinter.PhotoImage(file="Icon_Python.png")
# checkbutton = tkinter.Checkbutton(window, text="I agree", variable=check, onvalue=True, offvalue=False, command=display, font=("Times New Roman", 20), foreground="#191919", background="#E8E8E8", activeforeground="#191919", activebackground="#E8E8E8", padx=20, pady=10, image=checkbutton_photo, compound="left")
# checkbutton.pack()



# 📻 | 6. Radiobutton
# def order():
    # if (radio.get() == 0):
        # print("Hamburger Selected")
    # elif (radio.get() == 1):
        # print("Pizza Selected")
    # elif (radio.get() == 2):
        # print("Hotdog Selected")
    # elif (radio.get() == 3):
        # print("Croissant Selected")
    # else:
        # print("What?")

# foods = ("Hamburger", "Pizza", "Hotdog", "Croissant")
# radio = tkinter.IntVar()

# radiobutton_hamburger = tkinter.PhotoImage(file="Icon_Hamburger.png")
# radiobutton_pizza = tkinter.PhotoImage(file="Icon_Pizza.png")
# radiobutton_hotdog = tkinter.PhotoImage(file="Icon_Hotdog.png")
# radiobutton_croissant = tkinter.PhotoImage(file="Icon_Croissant.png")
# radiobutton_list = (radiobutton_hamburger, radiobutton_pizza, radiobutton_hotdog, radiobutton_croissant)

# for food in range(len(foods)):
    # radiobutton = tkinter.Radiobutton(window, text=foods[food], variable=radio, value=food, padx=25, font=("Times New Roman", 12), foreground="#191919", background="#E8E8E8", activeforeground="#E8E8E8", activebackground="#191919", image=radiobutton_list[food], compound="left", command=order)
    # radiobutton.pack(anchor="w")



# ⚖️ | 7. Scale
# def scaling():
    # print(f"The temperature is {scale.get()} degree celcius")

# scale_fire = tkinter.PhotoImage(file="Icon_Fire.png")
# scale_fire_label = tkinter.Label(image=scale_fire)
# scale_fire_label.pack()

# scale = tkinter.Scale(window, from_=100, to=0, length=300, orient="vertical", font=("Times New Roman", 12), tickinterval=10, showvalue=1, resolution=5, troughcolor="#E8E8E8", foreground="#191919")
# scale.set(20)
# # scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"]) # Middle of the Road
# scale.pack()

# scale_ice = tkinter.PhotoImage(file="Icon_Ice-Cube.png")
# scale_ice_label = tkinter.Label(image=scale_ice)
# scale_ice_label.pack()

# scale_button = tkinter.Button(window, text="Accept", command=scaling)
# scale_button.pack()



# 📝 | 8. Listbox
# def order_list():
    # print("\nSelected:")
    # print(listbox.get(listbox.curselection()))

# def add_list():
    # listbox.insert(listbox.size(), listbox_entrybox.get())
    # listbox.config(height=listbox.size())

# def delete_list():
    # listbox.delete(listbox.curselection())
    # listbox.config(height=listbox.size())

# def many_order():
    # ordered = []
    # for order1 in listbox.curselection():
        # ordered.insert(order1, listbox.get(order1))
    # print("Your Orders:")
    # for order2 in ordered:
        # print(order2)

# def many_delete():
    # for deleted in reversed(listbox.curselection()):
        # listbox.delete(deleted)
    # listbox.config(height=listbox.size())

# listbox = tkinter.Listbox(window, background="#E8E8E8", foreground="#191919", font=("Times New Roman", 14), width=20, selectmode="multiple")
# listbox.pack()

# listbox.insert(1, "Pizza")
# listbox.insert(2, "Hamburger")
# listbox.insert(3, "Hotdog")
# listbox.insert(4, "Croissant")
# listbox.insert(5, "Spaghetti")

# listbox.config(height=listbox.size())

# listbox_entrybox = tkinter.Entry(window)
# listbox_entrybox.pack()

# listbox_submitbutton = tkinter.Button(window, text="Order", command=many_order)
# listbox_submitbutton.pack()

# listbox_addbutton = tkinter.Button(window, text="Add", command=add_list)
# listbox_addbutton.pack()

# listbox_deletebutton = tkinter.Button(window, text="Delete", command=many_delete)
# listbox_deletebutton.pack()



# ✉️ | 9. Messagebox
# def message_click():
    # tkinter.messagebox.showinfo(title="Info message box", message="I don't know what is this")
    # tkinter.messagebox.showwarning(title="WARNING", message="Virus Detected")
    # tkinter.messagebox.showerror(title="Error", message="Unkown Anomalies Initiated")
    
    # if tkinter.messagebox.askokcancel(title="Ask Ok Cancel", message="Pop Os Detected"):
        # print("Nice to meet you")
    # else:
        # print("You cancelled it")

    # if tkinter.messagebox.askretrycancel(title="Ask Retry Cancel", message="Retrying Initialized"):
        # print("Retrying...")
    # else:
        # print("Forgeting...")

    # if tkinter.messagebox.askyesnocancel(title="Ask Yes No Cancel", message="Cake is the best"):
        # print("I Agree, cake is delicious")
    # else:
        # print("I Disagree, cake is the worst dessert")

    # message_answer = tkinter.messagebox.askquestion(title="Ask Question", message="Do you like pie?")
    # if message_answer == "yes":
        # print("Yes i do")
    # else:
        # print("No i don't")

    # message_answer2 = tkinter.messagebox.askyesnocancel(title="Ask Yes No Cancel", message="Python is the best language!")
    # if message_answer2 == True:
        # print("Hell, Yeah!")
    # elif message_answer2 == False:
        # print("Definitely No!")
    # else:
        # print("Let me think for a moment!")

# message_button = tkinter.Button(window, command=message_click, text="Click Me!")
# message_button.pack()



# 🔴 | 10. Colorhooser
# def colorhooser_click():
    # window.config(background=tkinter.colorchooser.askcolor()[1])

    # # ch_color = tkinter.colorchooser.askcolor()
    # # window.config(background=ch_color[1])

    # # ch_color = tkinter.colorchooser.askcolor()
    # # ch_color_hex = ch_color[1]
    # # window.config(background=ch_color_hex)

# colorhooser_button = tkinter.Button(text="Color Hooser", command=colorhooser_click)
# colorhooser_button.pack()



# 📍 | 11. Text Area
# def textarea_button_submit():
    # ta_input = textarea.get("1.0", tkinter.END)
    # print(ta_input)

# textarea = tkinter.Text(window, background="#ECDFCC", foreground="#181C14", font=("Times New Roman", 12), height=8, width=24, padx=20, pady=20)
# textarea.pack()

# textarea_button = tkinter.Button(window, text="The Button", command=textarea_button_submit)
# textarea_button.pack()



# 📄 | 12. Filedialog Open
# def filedialog_openfile():
    # fd_open_filepath = tkinter.filedialog.askopenfilename(initialdir="/home/inferno/Documents/Python Course", title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    # fd_open_file = open(fd_filepath, "r")
    # print(fd_file.read())
    # fd_file.close()

# fd_open_button = tkinter.Button(text="Open", command=filedialog_openfile)
# fd_open_button.pack()



# 💾 | 13. Filedialog Save
# def filedialog_savefile():
    # fd_save_file = tkinter.filedialog.asksaveasfile(initialdir="/home/inferno/Documents/Github Repository/Latihan-Algoritma/Python Project", defaultextension=".txt", filetypes=[("Text File", ".txt"), ("HTML FIle", ".html"),("All Files", ".*")])

    # if fd_save_file == None:
        # return

    # fd_save_filetext = str(fd_save_text.get(1.0, tkinter.END))
    # # fd_save_filetext = input("Enter some text: ")

    # fd_save_file.write(fd_save_filetext)
    # fd_save_file.close()

# fd_save_button = tkinter.Button(text="Save", command=filedialog_savefile)
# fd_save_button.pack()

# fd_save_text = tkinter.Text(window)
# fd_save_text.pack()



icon = tkinter.PhotoImage(file="/home/inferno/Documents/Github Repository/Latihan-Algoritma/Python Project/Icon_Python.png")
window.iconphoto(True, icon)

window.mainloop()

#E8E8E8 - White
#191919 - Black