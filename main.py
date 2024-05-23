import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

# ================= main window settings =================
app = customtkinter.CTk()
app.title("Employees Management System")
app.after(201, lambda: app.iconbitmap('J:\Python Projects\employee management system tkinter\manage-employee.ico'))
app.geometry('860x420')
app.config(bg='#161c25')
app.resizable(False, False)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

bg_color1 = '#161c25'
fg_color1 = '#fff'
hover_color1 = '#00850b'

# ================= labels and entry fields =================

id_label = customtkinter.CTkLabel(app, font=font1, text='ID', text_color='#fff', bg_color=bg_color1)
id_label.place(x=20, y=20)
id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
id_entry.place(x=100, y=20)

name_label = customtkinter.CTkLabel(app, font=font1, text='Name', text_color='#fff', bg_color='#161c25')
name_label.place(x=20, y=80)
name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
name_entry.place(x=100, y=80)

role_label = customtkinter.CTkLabel(app, font=font1, text='Role', text_color='#fff', bg_color='#161c25')
role_label.place(x=20, y=140)
role_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
role_entry.place(x=100, y=140)

gender_label = customtkinter.CTkLabel(app, font=font1, text='Gender', text_color='#fff', bg_color='#161c25')
gender_label.place(x=20, y=200)

options = ['Male', 'Female']
variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#0c9295', button_hover_color='#0c9295', border_color='#0c9295', width=180, variable=variable1, values=options, state='readonly')
gender_options.set('Male')
gender_options.place(x=100, y=200)

status_label = customtkinter.CTkLabel(app, font=font1, text='Status', text_color='#fff', bg_color='#161c25')
status_label.place(x=20, y=260)
status_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
status_entry.place(x=100, y=260)


# ================= action buttons =================

add_button = customtkinter.CTkButton(app, font=font1, text='Add Employee', text_color='#fff', fg_color='#05a312', hover_color=hover_color1, bg_color=bg_color1, cursor='hand2', corner_radius=15, width=260)
add_button.place(x=20, y=310)
clear_button = customtkinter.CTkButton(app, font=font1, text='New Employee', text_color='#fff', fg_color='#161c25', hover_color='#ff5002', bg_color=bg_color1, border_width=2, border_color='#f15704', cursor='hand2', corner_radius=15, width=260)
clear_button.place(x=20, y=360)
update_button = customtkinter.CTkButton(app, font=font1, text='Update Employee', text_color='#fff', fg_color='#161c25', hover_color='#ff5002', bg_color=bg_color1, border_width=2, border_color='#f15704', cursor='hand2', corner_radius=15, width=260)
update_button.place(x=300, y=360)
delete_button = customtkinter.CTkButton(app, font=font1, text='Delete Employee', text_color='#fff', fg_color='#e40404', hover_color='#ae0000', bg_color=bg_color1, border_color='#e40404', cursor='hand2', corner_radius=15, width=260)
delete_button.place(x=580, y=360)


# ================= Tree View =================

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1a8f2d')])

tree = ttk.Treeview(app, height=15)
tree.place(x=300, y=20)

# ================= Mainloop =================
app.mainloop()


