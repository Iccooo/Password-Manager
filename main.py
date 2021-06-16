from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def populate_list():
    programs_list.delete(0, END)
    for row in db.fetch():
        programs_list.insert(END, row)


def add_item():
    db.insert(program_text.get(), password_text.get(), email_text.get(), info_text.get())
    programs_list.delete(0, END)
    programs_list.insert(END, (program_text.get(), password_text.get(),  email_text.get(), info_text.get()))
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = programs_list.curselection()[0]
        selected_item = programs_list.get(index)

        program_entry.delete(0, END)
        program_entry.insert(END, selected_item[1])
        password_entry.delete(0, END)
        password_entry.insert(END, selected_item[2])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_item[3])
        info_entry.delete(0, END)
        info_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    populate_list()


def update_item():
    db.update(selected_item[0], program_text.get(), password_text.get(), email_text.get(), info_text.get())
    populate_list()
 
input_text = ""

master = "somepass"

input_text = input ("Enter Master Password \n ")
if input_text == master:
    app = Tk()
    app.title('Password Manager')
    app.geometry('540x380')

    program_text = StringVar()
    program_label = Label(app, text='Program', font=('bold', 14), pady=20)
    program_label.grid(row=0, column=0, sticky=W)
    program_entry = Entry(app, textvariable=program_text)
    program_entry.grid(row=0, column=1)



    password_text = StringVar()
    password_label = Label(app, text='Password', font=('bold', 14))
    password_label.grid(row=0, column=2, sticky=W)
    password_entry = Entry(app, textvariable=password_text)
    password_entry.grid(row=0, column=3)



    email_text = StringVar()
    email_label = Label(app, text='Email', font=('bold', 14))
    email_label.grid(row=1, column=0, sticky=W)
    email_entry = Entry(app, textvariable=email_text)
    email_entry.grid(row=1, column=1)



    info_text = StringVar()
    info_label = Label(app, text='Info', font=('bold', 14))
    info_label.grid(row=1, column=2, sticky=W)
    info_entry = Entry(app, textvariable=info_text)
    info_entry.grid(row=1, column=3)



    programs_list = Listbox(app, height=8, width=60, border=0)
    programs_list.grid(row=3, column=0, columnspan=3, rowspan=6,)



    programs_list.bind('<<ListboxSelect>>', select_item)



    add_btn = Button(app, text='Add Password', width=18, command=add_item)
    add_btn.grid(row=2, column=0, pady =50)

    remove_btn = Button(app, text='Remove Password', width=18, command=remove_item)
    remove_btn.grid(row=2, column=1)

    update_btn = Button(app, text='Update Password', width=18, command=update_item)
    update_btn.grid(row=2, column=2)

    check_btn = Button(app, text='Check Password', width=18)
    check_btn.grid(row=2, column=3)




    populate_list()
    app.mainloop()
    print("Working")