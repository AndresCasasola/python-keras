
from tkinter import *
from tkinter import ttk

def right_button_clicked():
	print (right_name.get())

def left_button_clicked():
	print (left_name.get())

# Window
window = Tk()
window.title("ImageEncryptor")
window.geometry('400x300')

##### Encryptor
# Main label
left_label = Label(window, text="Ecryptor")
left_label.grid(column=0, row=0, padx=55, pady=10)

# Entries
left_name = Entry(window, width=10)
left_name.grid(column=0, row=1, padx=55, pady=10)
left_key = Entry(window,width=10)
left_key.grid(column=0, row=2, padx=55, pady=10)

# Button
left_button = Button(window, text="Encrypt", command=left_button_clicked)
left_button.grid(column=0, row=3, padx=55, pady=10)

##### Decryptor
# Main label
right_label = Label(window, text="Decryptor")
right_label.grid(column=1, row=0, padx=55, pady=10)

# Entries
right_name = Entry(window,width=10)
right_name.grid(column=1, row=1, padx=55, pady=10)
right_key = Entry(window,width=10)
right_key.grid(column=1, row=2, padx=55, pady=10)
right_iv = Entry(window,width=10)
right_iv.grid(column=1, row=3, padx=55, pady=10)

# Button
right_button = Button(window, text="Decrypt", command=right_button_clicked)
right_button.grid(column=1, row=4, padx=55, pady=10)

window.mainloop()


