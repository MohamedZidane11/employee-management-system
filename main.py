import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


app = customtkinter.CTk()
app.title("Employees Management System")
app.after(201, lambda: app.iconbitmap('J:\Python Projects\employee management system tkinter\manage-employee.ico'))
app.geometry('800x420')
app.config(bg='#161c25')
app.resizable(False, False)


font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')


app.mainloop()


