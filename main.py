import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

import database

# ================= main window settings =================

app = customtkinter.CTk()
app.title("Employees Management System V1.0")
app.after(201, lambda: app.iconbitmap('J:\Python Projects\employee management system tkinter\manage-employee.ico'))
app.geometry('900x440')
app.config(bg='#161c25')
app.resizable(False, False)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

bg_color1 = '#161c25'
fg_color1 = '#fff'
hover_color1 = '#00850b'


# ================= TreeView Functions =================

def add_to_treeview():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)


def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    role_entry.delete(0, END)
    variable1.set('Male')
    status_entry.delete(0, END)


def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        data_row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0, data_row[0])
        name_entry.insert(0, data_row[1])
        role_entry.insert(0, data_row[2])
        variable1.set(data_row[3])
        status_entry.insert(0, data_row[4])


def insert():
    emp_id = id_entry.get()
    name = name_entry.get()
    role = role_entry.get()
    gender = variable1.get()
    status = status_entry.get()
    if not (emp_id and name and role and gender and status):
        messagebox.showerror('Error', 'All fields are required\nPlease enter all fields.')
    elif database.id_exists(emp_id):
        messagebox.showerror('Error', 'ID already exists.')
    else:
        database.insert_employee(emp_id, name, role, gender, status)
        add_to_treeview()
        messagebox.showinfo('Success', 'Data has been inserted.')


# ================= labels and entry fields =================

id_label = customtkinter.CTkLabel(app, font=font1, text='ID *', text_color='#fff', bg_color=bg_color1)
id_label.place(x=15, y=20)
id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
id_entry.place(x=105, y=20)

name_label = customtkinter.CTkLabel(app, font=font1, text='Name *', text_color='#fff', bg_color='#161c25')
name_label.place(x=15, y=80)
name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
name_entry.place(x=105, y=80)

role_label = customtkinter.CTkLabel(app, font=font1, text='Role *', text_color='#fff', bg_color='#161c25')
role_label.place(x=15, y=140)
role_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
role_entry.place(x=105, y=140)

gender_label = customtkinter.CTkLabel(app, font=font1, text='Gender *', text_color='#fff', bg_color='#161c25')
gender_label.place(x=15, y=200)

options = ['Male', 'Female']
variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#0c9295', button_hover_color='#0c9295', border_color='#0c9295', width=180, variable=variable1, values=options, state='readonly')
gender_options.set('Male')
gender_options.place(x=105, y=200)

status_label = customtkinter.CTkLabel(app, font=font1, text='Status *', text_color='#fff', bg_color='#161c25')
status_label.place(x=15, y=260)
status_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
status_entry.place(x=105, y=260)

copy_label = customtkinter.CTkLabel(app, font=('Comic Sans MS', 15, 'bold'), text='Developed by', text_color='#ce7e00', bg_color='#161c25')
copy_label.place(x=340, y=400)

dev_label = customtkinter.CTkLabel(app, font=('DS-Digital', 20, 'bold', 'italic'), text='M.Zidane', text_color='#3d85c6', bg_color='#161c25')
dev_label.place(x=440, y=400)


# ================= action buttons =================

add_button = customtkinter.CTkButton(app, command=insert, font=font1, text='Add Employee', text_color='#fff', fg_color='#05a312', hover_color=hover_color1, bg_color=bg_color1, cursor='hand2', corner_radius=15, width=260)
add_button.place(x=20, y=310)
clear_button = customtkinter.CTkButton(app, command=lambda:clear(True), font=font1, text='New Employee', text_color='#fff', fg_color='#161c25', hover_color='#ff5002', bg_color=bg_color1, border_width=2, border_color='#f15704', cursor='hand2', corner_radius=15, width=260)
clear_button.place(x=20, y=360)
update_button = customtkinter.CTkButton(app, font=font1, text='Update Employee', text_color='#fff', fg_color='#161c25', hover_color='#ff5002', bg_color=bg_color1, border_width=2, border_color='#f15704', cursor='hand2', corner_radius=15, width=260)
update_button.place(x=300, y=360)
delete_button = customtkinter.CTkButton(app, font=font1, text='Delete Employee', text_color='#fff', fg_color='#e40404', hover_color='#ae0000', bg_color=bg_color1, border_color='#e40404', cursor='hand2', corner_radius=15, width=260)
delete_button.place(x=580, y=360)


# ================= Tree View =================

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#000', background='#fff', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1a8f2d')])

tree = ttk.Treeview(app, height=15)
tree.place(x=300, y=20)

tree['column'] = ('ID', 'Name', 'Role', 'Gender', 'Status')

tree.column('#0', width=0, stretch=tk.NO)  # Hide Default Column First
tree.column('ID', anchor=tk.CENTER, width=120)
tree.column('Name', anchor=tk.CENTER, width=120)
tree.column('Role', anchor=tk.CENTER, width=120)
tree.column('Gender', anchor=tk.CENTER, width=100)
tree.column('Status', anchor=tk.CENTER, width=120)

tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Status', text='Status')

# ================= Mainloop func =================
tree.bind('<ButtonRelease>', display_data)
add_to_treeview()
app.mainloop()