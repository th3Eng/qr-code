import pyqrcode
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser

FONT = ("Tahoma", 15, "normal")

# integrate the tkinter
root = tk.Tk()
root.geometry('600x150+250+250')
root.title('QR code generator')
root.iconbitmap(r'./logo.ico')

link = tk.StringVar()
status = tk.StringVar()


def onClick():
	status.set('')
	_link = link.get()
	if _link == '':
		messagebox.showerror('Error', 'No link detected')
	elif _link.find('.') == -1:
		messagebox.showerror('Error', 'Invalid link')
	else:
		global url
		url = pyqrcode.create(_link)
		url.svg(f'{_link}.svg', scale=8)
		status.set(f'{_link} QR code created successfully!')
		# open the file
		webbrowser.open_new(f'{_link}.svg')


# image = Image.open(f'koko.svg')
# test = ImageTk.PhotoImage(image)
# label1 = ttk.Label(image=test)
# label1.image = test
# label1.grid(row=2, column=1)


label = ttk.Label(root, text='Enter the link', font=FONT, padding=10).grid(row=0, column=0)

# String which represent the QR code
entry = ttk.Entry(root, font=FONT, width=40, textvariable=link).grid(row=0, column=1)
button = ttk.Button(root, text='Generate', command=onClick).grid(row=1, column=0)
label2 = tk.Label(root, textvariable=status, font=("Tahoma", 15, "normal"), fg='blue').grid(row=1, column=1)

# make the program working while manually close
root.mainloop()
